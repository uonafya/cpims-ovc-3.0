from datetime import datetime
import uuid
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
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status

from .models import OVCMobileEvent, OVCMobileEventAttribute,CasePlanTemplateEvent,CasePlanTemplateService,OVCEvent, OVCServices,OVCMobileEventRejected,OVCEventRejected,OVCMobileEventAttributeRejected,OVCServicesRejected,CasePlanTemplateEventRejected,CasePlanTemplateServiceRejected
from rest_framework.permissions import IsAuthenticated,AllowAny 
from rest_framework.decorators import api_view, permission_classes
from django.db.models import F, CharField, Value
from django.db.models.functions import Concat
from django.db.models import OuterRef, Subquery

from cpovc_api.views import form_data

import requests
import json


from cpovc_forms.models import OVCCareQuestions, OVCCareQuestionss
from cpovc_main.functions import get_list, get_dict


class ApprovalStatus(Enum):
    NEUTRAL = auto() # stored as 1 in the DB
    TRUE = auto() # stored as 2 in the DB
    FALSE = auto() # stored as 3 in the DB

# Views for CPARA mobile
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_ovc_mobile_cpara_data(request):
    try:
        data = request.data
        is_accepted = ApprovalStatus.NEUTRAL.value
         # Check if the user is authenticated
        if not request.user.is_authenticated:
            return Response({'error': 'User is not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)

        user_id = request.user.id

        # Create an instance of OVCMobileEvent
        event = OVCMobileEvent.objects.create(
            ovc_cpims_id=data.get('ovc_cpims_id'),
            date_of_event=data.get('date_of_event'),
            is_accepted=is_accepted,
            user_id=user_id
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
            individual_ovc_id = ind_question.get('ovc_cpims_id', data.get('ovc_cpims_id'))
            OVCMobileEventAttribute.objects.create(
                event=event,
                ovc_cpims_id_individual=f"individual_ovc_id_{individual_ovc_id}",  # Add 'individual_ovc_id_' prefix
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
@permission_classes([IsAuthenticated])
def get_all_ovc_mobile_cpara_data(request):
    try:
        events = OVCMobileEvent.objects.all()
        data = []

        for event in events:
            event_data = {
                'ovc_cpims_id': event.ovc_cpims_id,
                'date_of_event': event.date_of_event,
                'is_accepted': event.is_accepted,
                'event_id': event.id,
                'questions': [],
                'individual_questions': [],
                'scores': {},  # Initialize scores as a dictionary
            }

            attributes = OVCMobileEventAttribute.objects.filter(event=event)

            for attribute in attributes:
                attribute_data = {
                    'question_name': attribute.question_name,
                    'answer_value': attribute.answer_value,
                    'ovc_cpims_id_individual': attribute.ovc_cpims_id_individual,
                }

                if attribute.question_name.startswith('question_'):
                    # Remove the 'question_' prefix
                    question_code = attribute.question_name[len('question_'):]
                    event_data['questions'].append({
                        'question_code': question_code,
                        'answer_id': attribute_data['answer_value'],
                    })
                elif attribute.question_name.startswith('individual_question_'):
                    # Remove 'individual_question_' prefix
                    question_code = attribute.question_name[len('individual_question_'):]
                    individual_question = {
                        'question_code': question_code,
                        'answer_id': attribute_data['answer_value'],
                    }
                    # Remove the prefixes
                    ovc_cpims_id_individual = attribute_data['ovc_cpims_id_individual']
                    if ovc_cpims_id_individual.startswith('individual_ovc_id_'):
                        ovc_cpims_id_individual = ovc_cpims_id_individual[len('individual_ovc_id_'):]
                    individual_question['ovc_cpims_id'] = ovc_cpims_id_individual
                    event_data['individual_questions'].append(individual_question)
                elif attribute.question_name.startswith('score_'):
                    # Remove the 'score_' prefix
                    key = attribute.question_name[len('score_'):]
                    event_data['scores'][key] = attribute_data['answer_value']

            data.append(event_data)

        return Response(data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_one_ovc_mobile_cpara_data(request, ovc_id):
    try:
        data = []

        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return Response({'error': 'User is not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)

        # Fetch by ovc id
        events = OVCMobileEvent.objects.filter(ovc_cpims_id=ovc_id, is_accepted=1)
        events_list = events.values('id')

        # Retrieve  event attributes
        attributes = OVCMobileEventAttribute.objects.filter(event__in=events_list)
        for event in events:
            event_data = {
                'ovc_cpims_id': event.ovc_cpims_id,
                'date_of_event': event.date_of_event,
                'event_id': event.id,
                'questions': [],
                'individual_questions': [],
                'scores': [],
            }


            for attribute in attributes:
                attribute_data = {
                    'question_name': attribute.question_name,
                    'answer_value': attribute.answer_value,
                    'ovc_cpims_id_individual': attribute.ovc_cpims_id_individual,  
                }

                if attribute.question_name.startswith('question_') and attribute.event_id == event.id:
                    # Remove the 'question_' prefix
                    question_code = attribute.question_name[len('question_'):]
                    event_data['questions'].append({
                        'question_code': question_code,
                        'answer_id': attribute_data['answer_value'],
                    })
                elif attribute.question_name.startswith('individual_question_') and attribute.event_id == event.id:
                    # Remove 'individual_question_' prefix
                    question_code = attribute.question_name[len('individual_question_'):]
                    individual_question = {
                        'question_code': question_code,
                        'answer_id': attribute_data['answer_value'],
                    }
                    # Aremove the prefixes
                    ovc_cpims_id_individual = attribute_data['ovc_cpims_id_individual']
                    if ovc_cpims_id_individual.startswith('individual_ovc_id_'):
                        ovc_cpims_id_individual = ovc_cpims_id_individual[len('individual_ovc_id_'):]
                    individual_question['ovc_cpims_id'] = ovc_cpims_id_individual
                    event_data['individual_questions'].append(individual_question)
                elif attribute.question_name.startswith('score_') and attribute.event_id == event.id:
                    # Remove the 'score_' prefix

                    event_data['scores'].append({attribute.question_name[len('score_'):] : attribute_data['answer_value']})

            data.append(event_data)

        return Response(data, status=status.HTTP_200_OK)
    except OVCMobileEvent.DoesNotExist:
        return Response({'error': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

def create_rejected_event(event, attributes, data):
    is_accepted = data.get('is_accepted')
    mobile_event_rejected = OVCMobileEventRejected.objects.create(
        user_id=event.user_id,
        ovc_cpims_id=event.ovc_cpims_id,
        date_of_event=event.date_of_event,
        is_accepted=is_accepted,
        message=data.get('message'),
        id=event.id
    )

    for attribute in attributes:
        OVCMobileEventAttributeRejected.objects.create(
            event=mobile_event_rejected,
            ovc_cpims_id_individual=attribute.ovc_cpims_id_individual,
            question_name=attribute.question_name,
            answer_value=attribute.answer_value
        )

def create_form_payload(attributes, event):
    form_payload = {
        'ovc_cpims_id': event.ovc_cpims_id,
        'date_of_event': event.date_of_event,
        'questions': [],
        'individual_questions': [],
        'scores': {},
    }

    for attribute in attributes:
        attribute_data = {
            'question_name': attribute.question_name,
            'answer_value': attribute.answer_value,
        }

        if attribute.question_name.startswith('question_'):
            question_code = attribute.question_name[len('question_'):]
            form_payload['questions'].append({
                'question_code': question_code,
                'answer_id': attribute_data['answer_value'],
            })
        elif attribute.question_name.startswith('individual_question_'):
            question_code = attribute.question_name[len('individual_question_'):]
            individual_question = {
                'question_code': question_code,
                'answer_id': attribute_data['answer_value'],
                'ovc_cpims_id': attribute.ovc_cpims_id_individual,
            }
            form_payload['individual_questions'].append(individual_question)
        elif attribute.question_name.startswith('score_'):
            key = attribute.question_name[len('score_'):]
            form_payload['scores'][key] = attribute_data['answer_value']

    return form_payload


@api_view(['PATCH', 'POST'])
@permission_classes([IsAuthenticated])
def update_cpara_is_accepted(request, event_id):
    try:
        event = OVCMobileEvent.objects.get(pk=event_id)
        attributes = OVCMobileEventAttribute.objects.filter(event=event)
        is_accepted = request.data.get('is_accepted')

        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return Response({'error': 'User is not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)

        # If is_accepted is false recreate it in the rejected tables
        if is_accepted == ApprovalStatus.FALSE.value:
            create_rejected_event(event, attributes, request.data)
         
        # # If is_accepted is true push it to main DB    
        # elif is_accepted == ApprovalStatus.TRUE.value:
            
        #     # create the payload
        #     form_payload = create_form_payload(attributes, event)
        #     request.data['form_payload'] = form_payload

        #     form_id = 'CPR'
            
        #     print("payload",request)
        #     response = form_data(request, form_id)
        #     print("response",response)


        # Update is_accepted field for the main event
        # for attribute in attributes:
        event.is_accepted = is_accepted
        event.save()

        return Response({'message': 'is_accepted updated successfully'}, status=status.HTTP_200_OK)
    except OVCMobileEvent.DoesNotExist:
        return Response({'error': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
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
@permission_classes([IsAuthenticated])
def create_ovc_event(request,form_id):
    try:
 
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return Response({'error': 'User is not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
        
        
        user_id = request.user.id
        form_type = form_id
        
        if form_type == 'F1A':
            form_type = form_type
        elif form_type == 'F1B':
            form_type = form_type
        else:
            return Response({'message': 'Invalid form type,(F1A,F1B)'})
        
        data = request.data
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return Response({'error': 'User is not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)

        user_id = request.user.id

        event = OVCEvent.objects.create(
            ovc_cpims_id=data.get('ovc_cpims_id'),
            date_of_event=data.get('date_of_event'),
            form_type=form_type,
            user_id=user_id

        )

        services = data.get('services', [])
        critical_events = data.get('critical_events',[])
        for service_data in services:
            OVCServices.objects.create(
                id=uuid.uuid4(),
                event=event,
                domain_id=service_data['domain_id'],
                service_id=service_data['service_id'],
                is_accepted=ApprovalStatus.NEUTRAL.value,
                # unique_service_id=uuid.uuid4()

            )

        for c_event in critical_events:
            domain_id=f'critical_key_{c_event["event_id"]}'
            service_id=f'critical_value_{c_event["event_date"]}'
            OVCServices.objects.create(
                id=uuid.uuid4(),
                event=event,
                domain_id=domain_id,
                service_id=service_id,
                is_accepted=ApprovalStatus.NEUTRAL.value,
                # unique_service_id=uuid.uuid4()

            )
        return Response({'message': 'Data stored successfully'}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_ovc_events(request, form_type):
    try:
        if form_type == 'F1A':
            events = OVCEvent.objects.filter(form_type='f1A')
        elif form_type == 'F1B':
            events = OVCEvent.objects.filter(form_type='f1B')
        else:
            return Response({'error': 'Enter valid form type: f1A or f1B'}),
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
@permission_classes([IsAuthenticated])
def get_ovc_event(request, form_type, ovc_id):
    ovc_id = int(ovc_id)
    event_data = []

    try:
        if form_type:
            all = OVCEvent.objects.all()
            # events = OVCEvent.objects.filter(ovc_cpims_id=ovc_id, form_type=form_type).order_by('id')
            services_data = OVCServices.objects.filter(event__form_type=form_type, event__ovc_cpims_id=ovc_id, is_accepted=1).values(
                'event_id', 'event__ovc_cpims_id', 'event__date_of_event', 'domain_id', 'service_id', 'is_accepted', 'id',
            ).order_by('event_id')
            # breakpoint()
        else:
            return Response({'error': 'Enter a valid form type: F1A or F1B'})

        # Create a dictionary to store event data
        event_dict = {}
        for service in services_data:
            # Check if we've already encountered this event
            event_id = service['event_id']
            if event_id not in event_dict:
                event_dict[event_id] = {
                    'ovc_cpims_id': service['event__ovc_cpims_id'],
                    'date_of_event': service['event__date_of_event'],
                    'event_id': event_id,
                    'services': [],
                    'critical_events':[],
                }
                
            # Check if the domain_id starts with 'critical_'
            if service['domain_id'].startswith('critical_'):
                critical_event_id = service['domain_id'][len('critical_key_'):]
                # Add the critical event to the critical_events list
                event_dict[event_id]['critical_events'].append({
                    'event_id': critical_event_id,
                    'event_date': service['event__date_of_event'],  # Use the date from the parent event
                })
            else:
                # Add service details to the event
                event_dict[event_id]['services'].append({
                    'event_id': service['event_id'],
                    'domain_id': service['domain_id'],
                    'service_id': service['service_id'],
                    'is_accepted': service['is_accepted'],
                    'id': service['id']
                })

        # Convert the dictionary into a list of event data
        event_data = list(event_dict.values())

        return Response(event_data, status=status.HTTP_200_OK)
    except OVCEvent.DoesNotExist:
        return Response({'error': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['PATCH', 'POST'])
@permission_classes([IsAuthenticated])
def update_is_accepted(request, id):
    try:
        # import pdb
        # pdb.set_trace()
        # Find the service using the id
        service = OVCServices.objects.get(id=id)

        is_accepted = request.data.get('is_accepted')

        if is_accepted == ApprovalStatus.FALSE.value:
            # If is_accepted is set to False (3), create corresponding rejected records
            rejected_event = OVCEventRejected.objects.create(
                user_id=service.event.user_id,
                ovc_cpims_id=service.event.ovc_cpims_id,
                date_of_event=service.event.date_of_event,
                form_type=service.event.form_type
            )

            # Create the corresponding rejected service
            OVCServicesRejected.objects.create(
                event=rejected_event,
                unique_service_id=service.id,
                domain_id=service.domain_id,
                service_id=service.service_id,
                is_accepted=is_accepted,
                message=request.data.get('message')
            )

        # Update the is_accepted field for the original service
        service.is_accepted = is_accepted
        service.save()

        return Response({'message': 'is_accepted updated successfully'}, status=status.HTTP_200_OK)
    except OVCEvent.DoesNotExist:
        return Response({'error': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
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
        'id': service.unique_service_id,
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
@permission_classes([IsAuthenticated])
def create_case_plan_template(request):
    try:
        payload = request.data
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return Response({'error': 'User is not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
        
        
        user_id = request.user.id

        # Create a new CasePlanTemplateEvent
        event = CasePlanTemplateEvent.objects.create(
            ovc_cpims_id=payload['ovc_cpims_id'],
            date_of_event=payload['date_of_event'],
            user_id = user_id
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
                is_accepted=ApprovalStatus.NEUTRAL.value  # Set to NEUTRAL by default
            )

        return Response({'message': 'Data stored successfully'}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
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
@permission_classes([IsAuthenticated])
def get_one_case_plan(request, ovc_id):
    try:
        events = CasePlanTemplateEvent.objects.filter(ovc_cpims_id=ovc_id)
        servicess = CasePlanTemplateService.objects.filter(event__in=events, is_accepted=1)

        event_data = []
        for event in events:
            services = servicess.filter(event=event)
            event_data.append({
            'event_id': event.id,
            'ovc_cpims_id': event.ovc_cpims_id,
            'date_of_event': event.date_of_event,
            'services': [service_serializer(service) for service in services]
        })

        return Response(event_data, status=status.HTTP_200_OK)
    except CasePlanTemplateEvent.DoesNotExist:
        return Response({'error': 'Case Plan Event not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH', 'POST'])
@permission_classes([IsAuthenticated])
def update_case_plan_is_accepted(request, unique_service_id):
    try:
        service = CasePlanTemplateService.objects.get(unique_service_id=unique_service_id)

        event = service.event

        new_is_accepted = request.data.get('is_accepted')
        if new_is_accepted is not None:
            # Check if is_accepted is set to False (3)
            if new_is_accepted == ApprovalStatus.FALSE.value:
                # Create a corresponding rejected record in CasePlanTemplateEventRejected
                rejected_event = CasePlanTemplateEventRejected.objects.create(
                    user_id=event.user_id,
                    ovc_cpims_id=event.ovc_cpims_id,
                    date_of_event=event.date_of_event
                )

                # Create the corresponding rejected service
                CasePlanTemplateServiceRejected.objects.create(
                    event=rejected_event,
                    domain_id=service.domain_id,
                    service_id=service.service_id,
                    goal_id=service.goal_id,
                    gap_id=service.gap_id,
                    priority_id=service.priority_id,
                    responsible_id=service.responsible_id,
                    results_id=service.results_id,
                    reason_id=service.reason_id,
                    completion_date=service.completion_date,
                    is_accepted=new_is_accepted,
                    message=request.data.get('message')
                )

            # Update the is_accepted field for the original service
            service.is_accepted = new_is_accepted
            service.save()

            return Response({'message': 'is_accepted updated successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'is_accepted field is required in the request body'}, status=status.HTTP_400_BAD_REQUEST)
    except CasePlanTemplateService.DoesNotExist:
        return Response({'error': 'Case Plan Service not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_case_plan_event(request, event_id):
    try:
        event = CasePlanTemplateEvent.objects.get(pk=event_id)
        event.delete()
        return Response({'message': 'Record  deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except CasePlanTemplateEvent.DoesNotExist:
        return Response({'error': 'Entry not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
       
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_unaccepted_records(request):
    try:

        data = []

        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return Response({'error': 'User is not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)

        # Fetch cpara records where is_accepted is FALSE (3) and user_id matches
        ovc_mobile_events_rejected = OVCMobileEvent.objects.filter(is_accepted=3, user_id=request.user.id)

        for rejected_event in ovc_mobile_events_rejected:
            event_data = {
                'ovc_cpims_id': rejected_event.ovc_cpims_id,
                'message':rejected_event.message,
                'date_of_event': rejected_event.date_of_event,
                'questions': [],
                'individual_questions': [],
                'scores': {},
            }

            # Retrieve  related rejected event
            attributes = OVCMobileEventAttribute.objects.filter(event=rejected_event)

            for attribute in attributes:
                attribute_data = {
                    'question_name': attribute.question_name,
                    'answer_value': attribute.answer_value,
                    'ovc_cpims_id_individual': attribute.ovc_cpims_id_individual,  
                }

                if attribute.question_name.startswith('question_'):
                    # Remove the 'question_' prefix
                    question_code = attribute.question_name[len('question_'):]
                    event_data['questions'].append({
                        'question_code': question_code,
                        'answer_id': attribute_data['answer_value'],
                    })
                elif attribute.question_name.startswith('individual_question_'):
                    # Remove 'individual_question_' prefix
                    question_code = attribute.question_name[len('individual_question_'):]
                    individual_question = {
                        'question_code': question_code,
                        'answer_id': attribute_data['answer_value'],
                    }
                    # Aremove the prefixes
                    ovc_cpims_id_individual = attribute_data['ovc_cpims_id_individual']
                    if ovc_cpims_id_individual.startswith('individual_ovc_id_'):
                        ovc_cpims_id_individual = ovc_cpims_id_individual[len('individual_ovc_id_'):]
                    individual_question['ovc_cpims_id'] = ovc_cpims_id_individual
                    event_data['individual_questions'].append(individual_question)
                elif attribute.question_name.startswith('score_'):
                    # Remove the 'score_' prefix
                    key = attribute.question_name[len('score_'):]
                    event_data['scores'][key] = attribute_data['answer_value']

            data.append(event_data)

        # Fetch Form 1A and B records where is_accepted is FALSE (3) and user_id matches
        ovc_services_rejected = OVCServices.objects.filter(is_accepted=3, event__user_id=request.user.id)

        for service_rejected in ovc_services_rejected:
            event_data = {
                'ovc_cpims_id': service_rejected.event.ovc_cpims_id,
                'date_of_event': service_rejected.event.date_of_event,
                'message': service_rejected.message,
                'services': {
                    'domain_id': service_rejected.domain_id,
                    'service_id': service_rejected.service_id,
                },
            }
            data.append(event_data)

        # Fetch CasePlanTemplate records where is_accepted is FALSE (3) and user_id matches
        case_plan_services_rejected = CasePlanTemplateService.objects.filter(is_accepted=3, event__user_id=request.user.id)

        for service_rejected in case_plan_services_rejected:
            event_data = {
                'ovc_cpims_id': service_rejected.event.ovc_cpims_id,
                'date_of_event': service_rejected.event.date_of_event,
                'message': service_rejected.message,
                'services': {
                    'domain_id': service_rejected.domain_id,
                    'service_id': service_rejected.service_id,
                    'goal_id': service_rejected.goal_id,
                    'priority_id':service_rejected.priority_id,
                    'responsible_id':service_rejected.responsible_id,
                    'results_id':service_rejected.results_id,
                    'reason_id':service_rejected.reason_id,
                    'completion_date':service_rejected.reason_id
                },
            }
            data.append(event_data)

        return Response(data, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


# Fetch unapproved records using query params
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def unaccepted_records(request, form_type):
    try:
        data = []
        
        if form_type == 'F1A' or form_type == 'F1B':
            # Fetch Form 1A and B records where is_accepted is FALSE (3) and user_id matches
           
            ovc_services = OVCServices.objects.filter(is_accepted=3, event__user_id=request.user.id, event__form_type=form_type)
            
            for service in ovc_services:
                event_data = {
                    'ovc_cpims_id': service.event.ovc_cpims_id,
                    'message': service.message,
                    'date_of_event': service.event.date_of_event,
                    'services': {
                        'domain_id': service.domain_id,
                        'service_id': service.service_id,
                    },
                }
                data.append(event_data)
        
        elif form_type == 'cpara':
            # Fetch cpara records where is_accepted is FALSE (3) and user_id matches
            cpara_events = OVCMobileEvent.objects.filter(is_accepted=3, user_id=request.user.id)
            
            for event in cpara_events:
                event_data = {
                    'ovc_cpims_id': event.ovc_cpims_id,
                    'date_of_event': event.date_of_event,
                    'questions': [],
                    'individual_questions': [],
                    'scores': {},
                }
                
                attributes = OVCMobileEventAttribute.objects.filter(event=event)
                
                for attribute in attributes:
                    attribute_data = {
                        'question_name': attribute.question_name,
                        'answer_value': attribute.answer_value,
                        'ovc_cpims_id_individual': attribute.ovc_cpims_id_individual,
                    }
                    
                    if attribute.question_name.startswith('question_'):
                        question_code = attribute.question_name[len('question_'):]
                        event_data['questions'].append({
                            'question_code': question_code,
                            'answer_id': attribute_data['answer_value'],
                        })
                    elif attribute.question_name.startswith('individual_question_'):
                        question_code = attribute.question_name[len('individual_question_'):]
                        individual_question = {
                            'question_code': question_code,
                            'answer_id': attribute_data['answer_value'],
                        }
                        
                        ovc_cpims_id_individual = attribute_data['ovc_cpims_id_individual']
                        
                        if ovc_cpims_id_individual.startswith('individual_ovc_id_'):
                            ovc_cpims_id_individual = ovc_cpims_id_individual[len('individual_ovc_id_'):]
                        
                        individual_question['ovc_cpims_id'] = ovc_cpims_id_individual
                        event_data['individual_questions'].append(individual_question)
                    elif attribute.question_name.startswith('score_'):
                        key = attribute.question_name[len('score_'):]
                        event_data['scores'][key] = attribute_data['answer_value']
                
                data.append(event_data)
        
        elif form_type == 'caseplan':
            # Fetch CasePlanTemplate records where is_accepted is FALSE (3) and user_id matches
            case_plan_services = CasePlanTemplateService.objects.filter(is_accepted=3, event__user_id=request.user.id)
            
            for service in case_plan_services:
                event_data = {
                    'ovc_cpims_id': service.event.ovc_cpims_id,
                    'date_of_event': service.event.date_of_event,
                    'message': service.message,
                    'services': {
                        'domain_id': service.domain_id,
                        'service_id': service.service_id,
                    },
                }
                data.append(event_data)
        else:
            return JsonResponse({'error': 'Unknown report type'}, status=400)
        
        return JsonResponse(data, status=200, safe=False)
    
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


  
 
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
        care_quiz = OVCCareQuestionss.objects.filter(is_void=False, code__startswith="CP")
        cpt_fields = ['case_plan_services_school', 'case_plan_services_safe', 'case_plan_services_stable', 'case_plan_services_health']
        cpt_list = get_dict(field_name=cpt_fields)
        f1b_fields = ['form1b_items']
        f1b_list = get_dict(field_name=f1b_fields)
        # f1a_list = get_dict([''])

        print(cpt_list, f1b_list)
   
        
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
                'lip_name': lip_name,
                'quizzes': care_quiz
             
            }
             )
    except Exception as e:
        raise e
    else:
        pass

def mobiledataapproval(request):
    if request.method == "POST":
        data = request.POST
        if(data):
            app_type = data.get('type')
            app_data = data.get('data[]')
            app_form = data.get('form')
            print(f">>>>>approval data{app_type} {app_data}, {app_form} {data}    {request.POST}")

            if app_form == 'CPR':
                if app_type == "approve":
                    pass
                elif app_type == 'reject':
                    pass
            if app_form == 'CPT':
                if app_type == "approve":
                    acccepted = CasePlanTemplateService.objects.get(id=app_data)
                    acce_event = CasePlanTemplateEvent.objects.get(id = acccepted.event_id)
                    acccepted.is_accepted = 2
                    acccepted.save()
                    
                    
                elif app_type == 'reject':
                    rejected = CasePlanTemplateService.objects.get(id=app_data)
                    rejected.is_accepted = 3
                    rejected.save()
                    

            if app_form == 'F1A':
                if app_type == "approve":
                    pass
                elif app_type == 'reject':
                    pass
            if app_form == 'F1B':
                if app_type == "approve":
                    pass
                elif app_type == 'reject':
                    pass
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
        print(request.POST)
        form_sel = request.POST.get('form')
        chv_sel = request.POST.getlist('chvs[]')
        child_sel = request.POST.getlist('child[]')

        formdata =[]
        if (form_sel == 'cpr'):

            events = OVCMobileEvent.objects.filter(ovc_cpims__in=child_sel, is_accepted = 1)
            form_datas = OVCMobileEventAttribute.objects.filter(event__in=events)
            dta = {}
            indx = 0
            for event in events:
                indx += 1
                for form_dta in form_datas.values():
                    if(event.id == form_dta['event_id']):
                        dta[form_dta['question_name']] = form_dta['answer_value']
                        dta['name'] = form_datas[indx].event.ovc_cpims.full_name
                        dta['date_of_event'] = form_datas[indx].event.date_of_event
                        dta['id'] = form_datas[indx].event.id
                        print(form_dta)
                formdata.append(dta)

            print(f"form_data {formdata}")
            # print(f"{form_sel} - {chv_sel} - {child_sel} -- {form_data}")
        elif((form_sel == 'cpt')):

            events = CasePlanTemplateEvent.objects.filter(ovc_cpims__in=child_sel)
            form_datas = CasePlanTemplateService.objects.filter(event__in=events, is_accepted=1)
            formdata = []
            indx = 0
            for form_dta in form_datas.values():
                dta = {}
                # breakpoint()
                for form_dt in form_dta.keys():
                    answer = form_dta[form_dt]
                    dta[form_dt] = answer
                dta['name'] = form_datas[indx].event.ovc_cpims.full_name
                dta['date_of_event'] = form_datas[indx].event.date_of_event
                indx += 1
                formdata.append(dta)
                
        elif((form_sel == 'form1a')):

            events = OVCEvent.objects.filter(ovc_cpims__in=child_sel)
            form_datas = OVCServices.objects.filter(event__in=events, is_accepted=1)
            formdata = []
            indx = 0
            for form_dta in form_datas.values():
                dta = {}
                # breakpoint()
                for form_dt in form_dta.keys():
                    answer = form_dta[form_dt]
                    dta[form_dt] = answer
                dta['name'] = form_datas[indx].event.ovc_cpims.full_name
                dta['date_of_event'] = form_datas[indx].event.date_of_event
                indx += 1
                formdata.append(dta)
        elif((form_sel == 'form1b')):

            events = OVCEvent.objects.filter(ovc_cpims__in=child_sel)
            form_datas = OVCServices.objects.filter(event__in=events, is_accepted=1)
            formdata = []
            indx = 0
            for form_dta in form_datas.values():
                dta = {}
                # breakpoint()
                for form_dt in form_dta.keys():
                    answer = form_dta[form_dt]
                    dta[form_dt] = answer
                dta['name'] = form_datas[indx].event.ovc_cpims.full_name
                dta['date_of_event'] = form_datas[indx].event.date_of_event
                indx += 1
                formdata.append(dta)
   
        response_data = {
            "status": "success",
            "message": "Data received and processed successfully."
            }
        return JsonResponse(formdata, safe=False)
    else:
        return JsonResponse({"error": "Invalid request method."}, safe=False)


def apiCall(payload, form_id):
    url = "http://127.0.0.1:8000/api/form/CPT/"

    payload = json.dumps(payload)
   
    headers = {
    'Content-Type': 'application/json',
    # 'Authorization': 'Basic dGVzdDoxMjM0NTZAQWI='
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    status_msg = response.text
    print(status_msg)

    return JsonResponse({"message": status_msg}, safe=False)

def update_mobile_forms():
    pass
    
