from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse

from cpovc_settings.forms import SettingsForm

from .forms import mobile_approve
from cpovc_forms.models import OVCCareF1B, OVCCareEAV

from cpovc_registry.models import RegPersonsOrgUnits, RegOrgUnit, RegPerson

from cpovc_ovc.models import OVCRegistration
# ---------------------------------------#
from enum import Enum, auto
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import OVCMobileEvent, OVCMobileEventAttribute,CasePlanTemplateEvent,CasePlanTemplateService,OVCEvent, OVCServices
from rest_framework.permissions import IsAuthenticated,AllowAny 
from django.db.models import F, CharField, Value
from django.db.models.functions import Concat
from django.db.models import OuterRef, Subquery


class ApprovalStatus(Enum):
    NEUTRAL = auto() # stored as 1 in the DB
    TRUE = auto() # stored as 2 in the DB
    FALSE = auto() # stored as 3 in the DB

# Views for CPARA mobile
@api_view(['POST'])
@permission_classes([AllowAny])
def create_ovc_mobile_cpara_data(request):
    try:
        data = request.data
        is_accepted = ApprovalStatus.FALSE.value

        # Create an instance of OVCMobileEvent
        event = OVCMobileEvent.objects.create(
            ovc_cpims_id=data.get('ovc_cpims_id'),
            date_of_event=data.get('date_of_event'),
            is_accepted=is_accepted,
        )

        # Handle questions
        questions = data.get('questions', [])
        for question in questions:
            question_name = f"question_{question['question_code']}"
            answer_value = question['answer_id']
            OVCMobileEventAttribute.objects.create(
                event=event,
                ovc_cpims_id_individual=data.get('ovc_cpims_id'),  # Use individual ovc_cpims_id if provided, otherwise use the main one
                question_name=question_name,
                answer_value=answer_value
            )

        # Handle individual questions
        individual_questions = data.get('individual_questions', [])
        for ind_question in individual_questions:
            question_name = f"individual_question_{ind_question['question_code']}"
            answer_value = ind_question['answer_id']
            OVCMobileEventAttribute.objects.create(
                event=event,
                # Use individual ovc_cpims_id for individual question 
                ovc_cpims_id_individual=ind_question.get('ovc_cpims_id', data.get('ovc_cpims_id')),  
                question_name=question_name,
                answer_value=answer_value
            )

        # Handle scores
        scores = data.get('scores', [])
        for score in scores:
            for key, value in score.items():
                question_name = f"score_{key}"
                answer_value = value
                OVCMobileEventAttribute.objects.create(
                    event=event,
                     # Use the main ovc_cpims_id
                    ovc_cpims_id_individual=data.get('ovc_cpims_id'), 
                    question_name=question_name,
                    answer_value=answer_value
                )

        return Response({'message': 'Data stored successfully'}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_ovc_mobile_cpara_data(request):
    try:
        events = OVCMobileEvent.objects.all()
        data = []

        for event in events:
            event_data = {
                'ovc_cpims_id': event.ovc_cpims_id,
                'date_of_event': event.date_of_event,
                'is_accepted': event.is_accepted,
                'questions': [],
                'individual_questions': [],
                'scores': [],
            }

            attributes = OVCMobileEventAttribute.objects.filter(event=event)

            for attribute in attributes:
                attribute_data = {
                    'question_name': attribute.question_name,
                    'answer_value': attribute.answer_value,
                }

                if attribute.question_name.startswith('question_'):
                    event_data['questions'].append(attribute_data)
                elif attribute.question_name.startswith('individual_question_'):
                    event_data['individual_questions'].append(attribute_data)
                elif attribute.question_name.startswith('score_'):
                    event_data['scores'].append(attribute_data)

            data.append(event_data)

        # Remove prefixes from attribute names
        for event_data in data:
            event_data['questions'] = [{k.replace('question_', ''): v for k, v in q.items()} for q in event_data['questions']]
            event_data['individual_questions'] = [{k.replace('individual_question_', ''): v for k, v in iq.items()} for iq in event_data['individual_questions']]
            event_data['scores'] = [{k.replace('score_', ''): v for k, v in s.items()} for s in event_data['scores']]

        return Response(data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_one_ovc_mobile_cpara_data(request, event_id):
    try:
        event = OVCMobileEvent.objects.get(pk=event_id)
        attributes = OVCMobileEventAttribute.objects.filter(event=event)
        event_data = {
            'id': event.id,
            'ovc_cpims_id': event.ovc_cpims_id,
            'date_of_event': event.date_of_event,
            'is_accepted': event.is_accepted
        }

        for attribute in attributes:
            event_data[attribute.question_name] = attribute.answer_value

        # Remove prefixes from attribute names
        for key in event_data.keys():
            if key.startswith('question_'):
                new_key = key.replace('question_', '')
                event_data[new_key] = event_data.pop(key)
            elif key.startswith('individual_question_'):
                new_key = key.replace('individual_question_', '')
                event_data[new_key] = event_data.pop(key)
            elif key.startswith('score_'):
                new_key = key.replace('score_', '')
                event_data[new_key] = event_data.pop(key)

        return Response(event_data, status=status.HTTP_200_OK)
    except OVCMobileEvent.DoesNotExist:
        return Response({'error': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
@permission_classes([AllowAny])
def update_cpara_is_accepted(request, event_id):
    try:
        event = OVCMobileEvent.objects.get(pk=event_id)
        is_accepted = request.data.get('is_accepted')
        event.is_accepted = is_accepted
        event.save()
        return Response({'message': 'is_accepted updated successfully'}, status=status.HTTP_200_OK)
    except OVCMobileEvent.DoesNotExist:
        return Response({'error': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_ovc_mobile_event(request, event_id):
    try:
        event = OVCMobileEvent.objects.get(pk=event_id)
        event.delete()
        return Response({'message': 'OVCMobileEvent deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except OVCMobileEvent.DoesNotExist:
        return Response({'error': 'OVCMobileEvent not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

# Views for Form1 A and B

@api_view(['POST'])
@permission_classes([AllowAny])
def create_ovc_event(request):
    try:
        data = request.data

        event = OVCEvent.objects.create(
            ovc_cpims_id=data.get('ovc_cpims_id'),
            date_of_event=data.get('date_of_event'),
        )

        services = data.get('services', [])
        for service_data in services:
            OVCServices.objects.create(
                event=event,
                domain_id=service_data['domain_id'],
                service_id=service_data['service_id'],
                is_accepted=ApprovalStatus.FALSE.value
            )

        return Response({'message': 'Data stored successfully'}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_ovc_events(request):
    try:
        events = OVCEvent.objects.all()
        data = []

        for event in events:
            services_data = OVCServices.objects.filter(event=event).values(
                'domain_id', 'service_id', 'is_accepted'
            )

            for service_data in services_data:
                event_data = {
                    'ovc_cpims_id': event.ovc_cpims_id,
                    'date_of_event': event.date_of_event,
                    'is_accepted': service_data['is_accepted'],
                    'services': {
                        'domain_id': service_data['domain_id'],
                        'service_id': service_data['service_id']
                    }
                }
                data.append(event_data)

        return Response(data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_ovc_event(request, event_id):
    try:
        event = OVCEvent.objects.get(pk=event_id)
        services_data = OVCServices.objects.filter(event=event).values(
            'domain_id', 'service_id', 'is_accepted'
        )
        event_data = {
            'ovc_cpims_id': event.ovc_cpims_id,
            'date_of_event': event.date_of_event,
            'services': []
        }

        for service_data in services_data:
            event_data['services'].append({
                'domain_id': service_data['domain_id'],
                'service_id': service_data['service_id'],
                'is_accepted': service_data['is_accepted']
            })

        return Response(event_data, status=status.HTTP_200_OK)
    except OVCEvent.DoesNotExist:
        return Response({'error': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
@permission_classes([AllowAny])
def update_is_accepted(request, event_id):
    try:
        event = OVCEvent.objects.get(pk=event_id)
        services = OVCServices.objects.filter(event=event)

        is_accepted = request.data.get('is_accepted')
        for service in services:
            service.is_accepted = is_accepted
            service.save()

        return Response({'message': 'is_accepted updated successfully'}, status=status.HTTP_200_OK)
    except OVCEvent.DoesNotExist:
        return Response({'error': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_ovc_event(request, event_id):
    try:
        event = OVCEvent.objects.get(pk=event_id)
        event.delete()
        return Response({'message': 'Event deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except OVCEvent.DoesNotExist:
        return Response({'error': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

# case plan template
# Helper function to serialize a service
def service_serializer(service):
    return {
        'id': service.id,
        'event_id': service.event_id,
        'domain_id': service.domain_id,
        'service_id': service.service_id,
        'goal_id': service.goal_id,
        'gap_id': service.gap_id,
        'priority_id': service.priority_id,
        'responsible_id': service.responsible_id,
        'results_id': service.results_id,
        'reason_id': service.reason_id,
        'completion_date': service.completion_date,
        'is_accepted': ApprovalStatus(service.is_accepted).name
    }

@api_view(['POST'])
@permission_classes([AllowAny])
def create_case_plan_template(request):
    try:
        payload = request.data

        # Create a new CasePlanTemplateEvent
        event = CasePlanTemplateEvent.objects.create(
            ovc_cpims_id=payload['ovc_cpims_id'],
            date_of_event=payload['date_of_event']
        )

        # Create a record for each service
        services = payload['services']
        for service in services:
            CasePlanTemplateService.objects.create(
                event=event,
                domain_id=service['domain_id'],
                service_id=service['service_id'],
                goal_id=service['goal_id'],
                gap_id=service['gap_id'],
                priority_id=service['priority_id'],
                responsible_id=service['responsible_id'],
                results_id=service['results_id'],
                reason_id=service['reason_id'],
                completion_date=service['completion_date'],
                is_accepted=ApprovalStatus.FALSE.value  # Set to NEUTRAL by default
            )

        return Response({'message': 'Data stored successfully'}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_case_plans(request):
    try:
        events = CasePlanTemplateEvent.objects.all()
        data = []

        for event in events:
            services = CasePlanTemplateService.objects.filter(event=event)
            event_data = {
                'event_id': event.id,
                'ovc_cpims_id': event.ovc_cpims_id,
                'date_of_event': event.date_of_event,
                'services': [service_serializer(service) for service in services]
            }
            data.append(event_data)

        return Response(data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_one_case_plan(request, event_id):
    try:
        event = CasePlanTemplateEvent.objects.get(id=event_id)
        services = CasePlanTemplateService.objects.filter(event=event)

        event_data = {
            'event_id': event.id,
            'ovc_cpims_id': event.ovc_cpims_id,
            'date_of_event': event.date_of_event,
            'services': [service_serializer(service) for service in services]
        }

        return Response(event_data, status=status.HTTP_200_OK)
    except CasePlanTemplateEvent.DoesNotExist:
        return Response({'error': 'Case Plan Event not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
@permission_classes([AllowAny])
def update_case_plan_is_accepted(request, event_id):
    try:
        event = CasePlanTemplateEvent.objects.get(id=event_id)
        services = CasePlanTemplateService.objects.filter(event=event)

        new_is_accepted = request.data.get('is_accepted')
        if new_is_accepted is not None:
            services.update(is_accepted=new_is_accepted)
            return Response({'message': 'is_accepted updated successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'is_accepted field is required in the request body'}, status=status.HTTP_400_BAD_REQUEST)
    except CasePlanTemplateEvent.DoesNotExist:
        return Response({'error': 'Case Plan Event not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_case_plan_event(request, event_id):
    try:
        event = CasePlanTemplateEvent.objects.get(pk=event_id)
        event.delete()
        return Response({'message': 'Record  deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except CasePlanTemplateEvent.DoesNotExist:
        return Response({'error': 'Entry not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    
#  Fetch all unapproved data
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_unaccepted_records(request):
    try:
        # Initialize an empty list to store the result data
        data = []

        # Fetch cpara records where is_accepted is FALSE (3)
        ovc_mobile_events = OVCMobileEvent.objects.filter(is_accepted=3)

        for event in ovc_mobile_events:
            event_data = {
                'ovc_cpims_id': event.ovc_cpims_id,
                'date_of_event': event.date_of_event,
                'is_accepted': event.is_accepted,
                'questions': [],
                'individual_questions': [],
                'scores': [],
            }

            attributes = OVCMobileEventAttribute.objects.filter(event=event)

            for attribute in attributes:
                attribute_data = {
                    'question_name': attribute.question_name,
                    'answer_value': attribute.answer_value,
                }

                if attribute.question_name.startswith('question_'):
                    event_data['questions'].append(attribute_data)
                elif attribute.question_name.startswith('individual_question_'):
                    event_data['individual_questions'].append(attribute_data)
                elif attribute.question_name.startswith('score_'):
                    event_data['scores'].append(attribute_data)

            # Remove prefixes from attribute names
            event_data['questions'] = [{k.replace('question_', ''): v for k, v in q.items()} for q in event_data['questions']]
            event_data['individual_questions'] = [{k.replace('individual_question_', ''): v for k, v in iq.items()} for iq in event_data['individual_questions']]
            event_data['scores'] = [{k.replace('score_', ''): v for k, v in s.items()} for s in event_data['scores']]

            data.append(event_data)

        # Fetch Form 1A and B records where is_accepted is FALSE (3)
        ovc_services = OVCServices.objects.filter(is_accepted=3)

        for service in ovc_services:
            event_data = {
                'ovc_cpims_id': service.event.ovc_cpims_id,
                'date_of_event': service.event.date_of_event,
                'is_accepted': service.is_accepted,
                'services': {
                    'domain_id': service.domain_id,
                    'service_id': service.service_id
                }
            }
            data.append(event_data)

        # Fetch CasePlanTemplate records where is_accepted is FALSE (3)
        case_plan_services = CasePlanTemplateService.objects.filter(is_accepted=3)

        for service in case_plan_services:
            event_data = {
                'ovc_cpims_id': service.event.ovc_cpims_id,
                'date_of_event': service.event.date_of_event,
                'is_accepted': service.is_accepted,
                'services': {
                    'domain_id': service.domain_id,
                    'service_id': service.service_id
                }
            }
            data.append(event_data)

        return Response(data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


#  Fetch unapproved records using query params
@api_view(['GET'])
@permission_classes([AllowAny])
def unaccepted_records(request):
    record_type = request.GET.get('record_type')
    
    data = []
    
    # Check the record and 
    if record_type == 'F1AB':
        # Fetch Form 1A and B records where is_accepted is FALSE (3)
        ovc_services = OVCServices.objects.filter(is_accepted=3)

        for service in ovc_services:
            event_data = {
                'ovc_cpims_id': service.event.ovc_cpims_id,
                'message': service.message,
                'date_of_event': service.event.date_of_event,
                'is_accepted': service.is_accepted,
                'services': {
                    'domain_id': service.domain_id,
                    'service_id': service.service_id
                }
            }
            data.append(event_data)
        
    elif record_type == 'cpara':
        # Fetch cpara records where is_accepted is FALSE (3)
        ovc_mobile_events = OVCMobileEvent.objects.filter(is_accepted=3)

        for event in ovc_mobile_events:
            event_data = {
                'ovc_cpims_id': event.ovc_cpims_id,
                'message': event.message,
                'date_of_event': event.date_of_event,
                'is_accepted': event.is_accepted,
                'questions': [],
                'individual_questions': [],
                'scores': [],
            }

            attributes = OVCMobileEventAttribute.objects.filter(event=event)

            for attribute in attributes:
                attribute_data = {
                    'question_name': attribute.question_name,
                    'answer_value': attribute.answer_value,
                }

                if attribute.question_name.startswith('question_'):
                    event_data['questions'].append(attribute_data)
                elif attribute.question_name.startswith('individual_question_'):
                    event_data['individual_questions'].append(attribute_data)
                elif attribute.question_name.startswith('score_'):
                    event_data['scores'].append(attribute_data)

            # Remove prefixes from attribute names
            event_data['questions'] = [{k.replace('question_', ''): v for k, v in q.items()} for q in event_data['questions']]
            event_data['individual_questions'] = [{k.replace('individual_question_', ''): v for k, v in iq.items()} for iq in event_data['individual_questions']]
            event_data['scores'] = [{k.replace('score_', ''): v for k, v in s.items()} for s in event_data['scores']]

            data.append(event_data)
        
    elif record_type == 'caseplan':

                # Fetch CasePlanTemplate records where is_accepted is FALSE (3)
        case_plan_services = CasePlanTemplateService.objects.filter(is_accepted=3)

        for service in case_plan_services:
            event_data = {
                'ovc_cpims_id': service.event.ovc_cpims_id,
                'date_of_event': service.event.date_of_event,
                'message': service.message,
                'is_accepted': service.is_accepted,
                'services': {
                    'domain_id': service.domain_id,
                    'service_id': service.service_id
                }
            }
            data.append(event_data)


    else:

        data = {'message': 'Unknown report type'}

    return Response(data, status=status.HTTP_200_OK)

  
  
  
# Front end validation login



@login_required
def mobile_home(request):
    """Method to do pivot reports."""

    form1b = OVCCareEAV.objects.filter(event = 'b4e0d636-34e8-11e9-9e13-e4a471adc5eb')
    currentUser = request.user.reg_person_id
    try:
        form = mobile_approve()
        lip_name = request.session.get('ou_primary_name')
        lip_id = request.session.get('ou_primary')

        chvss = OVCRegistration.objects.filter(is_void=False, child_cbo_id=lip_id).distinct('child_chv_id')
        chvs = []
        for chv in chvss:
            chvs.append({
                'cpims_chv_id': chv.child_chv.pk,
                'name': f"{chv.child_chv.full_name}"
            })

        return render(
            request, 'mobile/home.html',
            {
                'form': form,
                'formdata': form1b,
                'chvs': chvs,
                'lip_name': lip_name
             
            }
             )
    except Exception as e:
        raise e
    else:
        pass

def mobiledataapproval(request):
    if request.method == "POST":
        data = request.POST
        print(f">>>>>approval data{data.getlist('data[]')} {data.get('type')}")
        # Do something with the data, e.g., save to a database

        approval_type = data.get('type')
        approval_data = data.getlist('data[]')
        response_data = {
            "status": "success",
            "message": "Data received and processed successfully."
            }
        return JsonResponse(response_data, safe=False)
    else:
        return JsonResponse({"error": "Invalid request method."}, safe=False)
    
def fetchChildren(request):
    children = []
    if request.method == "POST":
        data = request.POST.getlist('data[]')
        childrens = OVCRegistration.objects.filter(is_void=False, child_chv_id__in = data).distinct('person')
        for child in childrens:
            children.append({
                'cpims_ovc_id': child.person.pk,
                'name': child.person.full_name
            })

        print(f"----- {data} >- {children} -  {childrens}")
        # Do something with the data, e.g., save to a database
        response_data = {"message": "Data received and processed successfully."}
        return JsonResponse(children, safe=False)
    else:
        return JsonResponse({"error": "Invalid request method."}, safe=False)
    
def fetchData(request):
    if request.method == "POST":
        data = request.POST
        # Do something with the data, e.g., save to a database

        form_sel = request.POST.get('form')
        chv_sel = request.POST.getlist('chvs[]')
        child_sel = request.POST.getlist('child[]')
        print(f"{form_sel} - {chv_sel} - {child_sel}")
   
        response_data = {
            "status": "success",
            "message": "Data received and processed successfully."
            }
        return JsonResponse(response_data, safe=False)
    else:
        return JsonResponse({"error": "Invalid request method."}, safe=False)
    
