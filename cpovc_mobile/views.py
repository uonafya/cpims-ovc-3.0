from datetime import timezone
import uuid
import base64
from django.forms import model_to_dict

from cpovc_auth.models import AppUser

from .functions import model_to_dict_custom

import requests
import json

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from enum import Enum, auto
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .forms import mobile_approve
from cpovc_forms.models import OVCCareEAV

from cpovc_ovc.models import OVCRegistration
# ---------------------------------------#

from rest_framework.response import Response
from rest_framework import status


from .models import (OVCMobileEvent, OVCMobileEventAttribute,CasePlanTemplateEvent,CasePlanTemplateService,
                    OVCEvent, OVCServices,
                    OVCMobileEventRejected,OVCEventRejected,
                    OVCMobileEventAttributeRejected,OVCServicesRejected, CasePlanTemplateEventRejected,CasePlanTemplateServiceRejected,
                    HIVManagementStaging,HIVManagementStagingRejected,RiskScreeningStaging,RiskScreeningStagingRejected
                    )
from rest_framework.permissions import IsAuthenticated,AllowAny 
from rest_framework.decorators import api_view, permission_classes
from django.db.models import F, CharField, Value
from django.db.models.functions import Concat
from django.db.models import OuterRef, Subquery
from django.core import serializers



from cpovc_forms.models import OVCCareQuestions
from cpovc_main.functions import get_dict

from cpovc_registry.models import RegPerson
from django.db.models import Count

from django.conf import settings
import os

def read_json_fixture(filename):
    # Get the path to the JSON file in the fixtures directory
    json_file_path = os.path.join(settings.BASE_DIR+'/cpovc_mobile', 'fixtures', filename)

    try:
        # Open and read the JSON file
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)
        return JsonResponse(data, safe=False)
    except FileNotFoundError:
        # Handle the case when the file is not found
        return JsonResponse({'error': 'JSON file not found'}, status=404)
    except json.JSONDecodeError:
        # Handle JSON decoding error
        return JsonResponse({'error': 'Error decoding JSON'}, status=500)


# from cpovc_auth.decorators import is_allowed_user_groups


# Functions
class ApprovalStatus(Enum):
    NEUTRAL = auto()  # stored as 1 in the DB
    TRUE = auto()  # stored as 2 in the DB
    FALSE = auto()  # stored as 3 in the DB

def delete_accepted_records(main_model, rejected_model, unique_id):
    try:
        print(rejected_model.objects.get(unique_id=unique_id).values())
        print(main_model.objects.get(unique_id=unique_id).values())
        
        rejected_model.objects.get(unique_id=unique_id).delete()
        main_model.objects.get(unique_id=unique_id).delete()

    except rejected_model.DoesNotExist:
        # If model record doesn't exist, delete only the main_model record
        main_model.objects.get(unique_id=unique_id).delete()
        return Response({'message': 'is_accepted updated successfully'}, status=status.HTTP_200_OK)

def serialize_string(app_form_metadata):
        app_form_metadata_str = app_form_metadata
        app_form_metadata = {}

        if app_form_metadata_str:
            try:
                app_form_metadata = json.loads(app_form_metadata_str)
                return app_form_metadata
            except json.JSONDecodeError as e:
                return app_form_metadata
                
def delete_parent_and_children(parent_model, child_model, parent_id):
    try:
        parent = parent_model.objects.get(id=parent_id)

        #
        if child_model.objects.filter(event=parent).exists():
            # Delete child records
            child_model.objects.filter(event=parent).delete()

        # Delete parent
        parent.delete()
        return True
    except parent_model.DoesNotExist:
        return False  # Parent not found
    except Exception as e:
        return str(e) 

hmf_field_mapping = {
    "hiv_confirmed_date": "HIV_MGMT_1_A",
    "treatment_initiated_date": "HIV_MGMT_1_B",
    "baseline_hei": "HIV_MGMT_1_C",
    "firstline_start_date": "HIV_MGMT_1_D",
    "substitution_firstline_arv": "HIV_MGMT_1_E",
    "substitution_firstline_date": "HIV_MGMT_1_E_DATE",
    "switch_secondline_arv": "HIV_MGMT_1_F",
    "switch_secondline_date": "HIV_MGMT_1_F_DATE",
    "switch_thirdline_arv": "HIV_MGMT_1_G",
    "switch_thirdline_date": "HIV_MGMT_1_G_DATE",
    "visit_date": "HIV_MGMT_2_A",
    "duration_art": "HIV_MGMT_2_B",
    "height": "HIV_MGMT_2_C",
    "muac": "HIV_MGMT_2_D",
    "adherence": "HIV_MGMT_2_E",
    "adherence_drugs_duration": "HIV_MGMT_2_F",
    "adherence_counselling": "HIV_MGMT_2_G",
    "treatment_supporter": "HIV_MGMT_2_H_2",
    "treatment_supporter_relationship": "HIV_MGMT_2_H_1",
    "treatment_supporter_gender": "HIV_MGMT_2_H_3",
    "treatment_supporter_age": "HIV_MGMT_2_H_4",
    "treatment_supporter_hiv": "HIV_MGMT_2_H_5",
    "viral_load_results": "HIV_MGMT_2_I_1",
    "viral_load_date": "HIV_MGMT_2_I_DATE",
    "detectable_viralload_interventions": "HIV_MGMT_2_J",
    "disclosure": "HIV_MGMT_2_K",
    "muac_score": "HIV_MGMT_2_L_1",
    "bmi": "HIV_MGMT_2_L_2",
    "nutritional_support": "HIV_MGMT_2_M",
    "support_group_status": "HIV_MGMT_2_N",
    "nhif_enrollment": "HIV_MGMT_2_O_1",
    "nhif_status": "HIV_MGMT_2_O_2",
    "referral_services": "HIV_MGMT_2_P",
    "nextappointment_date": "HIV_MGMT_2_Q",
    "peer_educator_name": "HIV_MGMT_2_R",
    "peer_educator_contact": "HIV_MGMT_2_S",
    "date_of_event": "HIV_MGMT_2_A"
}

hrs_field_mapping = {
    "date_of_event": "HIV_RA_1A",
    "test_done_when": "HIV_RS_03",
    "test_donewhen_result": "",
    "caregiver_know_status": "HIV_RS_01",
    "caregiver_knowledge_yes": "HIV_RS_02",
    "parent_PLWH": "HIV_RS_04",
    "child_sick_malnourished": "HIV_RS_05",
    "child_sexual_abuse": "HIV_RS_06",
    "traditional_procedure": "HIV_RS_06A",
    "adol_sick": "HIV_RS_07",
    "adol_had_tb": "HIV_RS_08",
    "adol_sexual_abuse": "HIV_RS_09",
    "sex": "HIV_RS_10",
    "sti": "HIV_RS_10A",
    "sharing_needles": "HIV_RS_10B",
    "hiv_test_required": "HIV_RS_11",
    "parent_consent_testing": "HIV_RS_14",
    "parent_consent_date": "HIV_RS_15",
    "referral_made": "HIV_RS_16",
    "referral_made_date": "HIV_RS_17",
    "referral_completed": "HIV_RS_18",
    "referral_completed_date": "HIV_RS_19",
    "not_completed": "HIV_RS_18A",
    "test_result": "HIV_RS_18B",
    "art_referral": "HIV_RS_21",
    "art_referral_date": "HIV_RS_22",
    "art_referral_completed": "HIV_RS_23",
    "art_referral_completed_date": "HIV_RS_24",
    "facility_code": "HIV_RA_3Q6",
}


def strip_prefix(to_strip):
    stripped = str(to_strip).split('_')
    if len(stripped) > 1:
        return stripped[1]
    else:
        return stripped
 
def create_form_payload(attributes, event):
    form_payload = {
        'ovc_cpims': event.ovc_cpims,
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
            question_code = attribute.question_name[len(
                'individual_question_'):]
            individual_question = {
                'question_code': question_code,
                'answer_id': attribute_data['answer_value'],
                'ovc_cpims_id': attribute.ovc_cpims,
            }
            form_payload['individual_questions'].append(individual_question)
        elif attribute.question_name.startswith('score_'):
            key = attribute.question_name[len('score_'):]
            form_payload['scores'][key] = attribute_data['answer_value']

    return form_payload   

def create_rejected_event(event, attributes, data):
    is_accepted = data.get('is_accepted')
    rejected_id=event.id
    mobile_event_rejected = OVCMobileEventRejected.objects.create(
        user=event.user,
        ovc_cpims=event.ovc_cpims,
        date_of_event=event.date_of_event,
        is_accepted=is_accepted,
        app_form_metadata=event.app_form_metadata,
        message=data.get('message'),
        id=rejected_id
    )

    rejected_event_id = mobile_event_rejected.id
    
    for attribute in attributes:
        print("doing it")
        OVCMobileEventAttributeRejected.objects.create(
            event=rejected_event_id,
            ovc_cpims=attribute.ovc_cpims_id_individual,
            question_name=attribute.question_name,
            answer_value=attribute.answer_value
        )

def service_serializer(service):
    return {
        'id': service.unique_service_id,
        'event_id': service.event_id,
        'domain_id': service.domain_id,
        'service_id': json.loads(service.service_id.replace("'", '"')),
        'goal_id': service.goal_id,
        'gap_id': service.gap_id,
        'priority_id': service.priority_id,
        'responsible_id': service.responsible_id,
        'results_id': service.results_id,
        'reason_id': service.reason_id,
        'completion_date': service.completion_date,
        'is_accepted': ApprovalStatus(service.is_accepted).name
    }

#convert yes_no to Boolean handle null
def handle_Null(answer):
    if type(answer) == str:
        if answer == 'AYES':
            return True
        elif answer == 'ANNO':
            return False
        elif len(answer.strip()) == 0:
            return None
        else:
            return answer
    else:
        return answer    

# Count unnapproved records
def count_unnapproved_records(request):
    
    cpara_rejected = OVCMobileEventRejected.objects.filter(
            is_accepted=3, user=request.user.id).count()
    f1A_rejected = OVCServicesRejected.objects.filter(
                is_accepted=3, event__user_id=request.user.id, event__form_type='F1A').count()
    f1B_rejected = OVCServicesRejected.objects.filter(
                is_accepted=3, event__user_id=request.user.id, event__form_type='F1B').count()
    caseplan_rejected = CasePlanTemplateServiceRejected.objects.filter(
                is_accepted=3, event__user_id=request.user.id).count()
    hiv_management_rejected = HIVManagementStagingRejected.objects.filter(
                is_accepted=3, user=request.user.id).count()
    hiv_screening_rejected = RiskScreeningStagingRejected.objects.filter(
                is_accepted=3, user=request.user.id).count()
    
    count_data = {
                'rejected_cpara':cpara_rejected,
                'f1A_rejected':f1A_rejected,
                'f1B_rejected':f1B_rejected,
                'caseplan_rejected':caseplan_rejected,
                'hiv_management_rejected':hiv_management_rejected,
                'hiv_screening_rejected':hiv_screening_rejected
                }
    print('hey',count_data)
    
    return JsonResponse(count_data, status=200, safe=False)

def count_neutral_records(request):
    
    cpara_neutral = OVCMobileEventRejected.objects.filter(
            is_accepted=1, user=request.user.id).count()
    f1A_neutral = OVCServicesRejected.objects.filter(
                is_accepted=1, event__user_id=request.user.id, event__form_type='F1A').count()
    f1B_neutral = OVCServicesRejected.objects.filter(
                is_accepted=1, event__user_id=request.user.id, event__form_type='F1B').count()
    caseplan_neutral = CasePlanTemplateServiceRejected.objects.filter(
                is_accepted=1, event__user_id=request.user.id).count()
    hiv_management_neutral = HIVManagementStagingRejected.objects.filter(
                is_accepted=1, user=request.user.id).count()
    hiv_screening_neutral = RiskScreeningStagingRejected.objects.filter(
                is_accepted=1, user=request.user.id).count()
    
    count_data = {
                'cpara_neutral':cpara_neutral,
                'f1A_neutral':f1A_neutral,
                'f1B_neutral':f1B_neutral,
                'caseplan_neutral':caseplan_neutral,
                'hiv_management_neutral':hiv_management_neutral,
                'hiv_screening_neutral':hiv_screening_neutral
                }
    print('hey',count_data)
    
    return JsonResponse(count_data, status=200, safe=False)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def check_saved_rejected(request):
    try:
        data = request.data
        form_type = data.get('form_type')
        saved = data.get('saved')
        record_id = data.get('record_id')
        
        if form_type and (saved == 1) and record_id:
            if form_type in ['F1A','F1B']:
                
                saved_event = OVCEventRejected.objects.filter(id=record_id)
                event_id = saved_event.first().id

                shared_event_id_rejected = OVCServicesRejected.objects.filter(event_id=event_id).count()
                shared_event_id = OVCServices.objects.filter(event_id=event_id).count()

                OVCServicesRejected.objects.filter(event_id=record_id).delete()
                OVCServices.objects.filter(event_id=record_id,is_accepted=3).delete()

                if shared_event_id_rejected == 1:
                    service_rejected_event = OVCEventRejected.objects.filter(id=event_id)
                    if service_rejected_event:
                        service_rejected_event.delete()

                if shared_event_id == 1:
                    service_event = OVCEvent.objects.filter(id=event_id)
                    if service_event:
                        service_event.delete()
                
            elif form_type == 'cpt':
                        
                saved_event = CasePlanTemplateEventRejected.objects.filter(id=record_id)
                event_id = saved_event.first().id

                shared_event_id_rejected = CasePlanTemplateServiceRejected.objects.filter(event_id=event_id).count()
                shared_event_id = CasePlanTemplateService.objects.filter(event_id=event_id).count()

                CasePlanTemplateServiceRejected.objects.filter(event_id=record_id).delete()
                CasePlanTemplateService.objects.filter(event_id=record_id,is_accepted=3).delete()

                if shared_event_id_rejected == 1:
                    service_rejected_event = CasePlanTemplateEventRejected.objects.filter(id=event_id)
                    if service_rejected_event:
                        service_rejected_event.delete()

                if shared_event_id == 1:
                    service_event = CasePlanTemplateEvent.objects.filter(id=event_id)
                    if service_event:
                        service_event.delete()
                    
            elif form_type == 'cpara':
                
                event = OVCMobileEvent.objects.get(pk=record_id)
                attributes = OVCMobileEventAttribute.objects.filter(event=event)
                event_rejected = OVCMobileEventRejected.objects.get(pk=record_id)
                OVCMobileEventAttributeRejected.objects.filter(event=event_rejected).delete()
                attributes.delete()
                event.delete()
                event_rejected.delete()
                
            elif form_type == 'hrs':
                
                RiskScreeningStagingRejected.objects.get(risk_id=record_id).delete()
                RiskScreeningStaging.objects.get(risk_id=record_id).delete()
                
            elif form_type == "hmf":
                
                HIVManagementStagingRejected.objects.get(adherence_id=record_id).delete()
                HIVManagementStaging.objects.get(adherence_id=record_id).delete()
            
            else:
                return(Response({'message':'incomplete/incorrect payload'},status=status.HTTP_400_BAD_REQUEST))
            
            return Response({'message': 'Record delted successfully'}, status=status.HTTP_200_OK)
        else:
            return(Response({'message':'Record not deleted..incomplete/incorrect payload'},status=status.HTTP_400_BAD_REQUEST))
               
    
    except Exception as e:
        return(Response({'error':str(e)}))

def get_sex_person(sex):
    if sex == 'SMAL':
        return 'Male'
    elif sex == 'SFEM':
        return 'Female'
    else:
        return 'invalid input'        
                
# Views for CPARA mobile
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_ovc_mobile_cpara_data(request):
    try:       
        data = request.data
        print(f"CPARA mobile data {data}")
        is_accepted = ApprovalStatus.NEUTRAL.value
        
        if not request.user.is_authenticated:
            return Response({'error': 'User is not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)

        user_id = AppUser.objects.get(pk=request.user.id)
        ovc_cpims_id = RegPerson.objects.get(pk=data.get('ovc_cpims_id')) 
        event_id = data.get('id')
        
        if event_id:
            try:
                event = OVCMobileEvent.objects.get(pk=event_id)
                OVCMobileEventAttribute.objects.filter(event=event).delete()
                event.delete()
            except OVCMobileEvent.DoesNotExist:
                return Response({'error': 'The id provided is not found in the models'}, status=status.HTTP_401_UNAUTHORIZED)
  
            # Create an instance of OVCMobileEvent
            event = OVCMobileEvent.objects.create(
                id = event_id,
                ovc_cpims=ovc_cpims_id,
                date_of_event=data.get('date_of_event'),
                is_accepted=is_accepted,
                signature=base64.b64encode(data.get('signature').encode("utf-8")),
                user=user_id,
                app_form_metadata=json.dumps(data.get('app_form_metadata'))
            )
        else:            
            event = OVCMobileEvent.objects.create(
                ovc_cpims=RegPerson.objects.get(pk=data.get('ovc_cpims_id')) ,
                date_of_event=data.get('date_of_event'),
                is_accepted=is_accepted,
                signature=base64.b64encode(data.get('signature').encode("utf-8")),
                user=user_id,
                app_form_metadata=json.dumps(data.get('app_form_metadata'))
            )
            

        # Handle questions
        questions = data.get('questions', [])
        for question in questions:
            question_name = f"question_{question['question_code']}"
            answer_value = question['answer_id']
            OVCMobileEventAttribute.objects.create(
                event=event,
                # Use individual ovc_cpims_id if provided, otherwise use the main one
                ovc_cpims=RegPerson.objects.get(pk=data.get('ovc_cpims_id')),
                question_name=question_name,
                answer_value=answer_value
            )

        # Handle individual questions
        individual_questions = data.get('individual_questions', [])
        for ind_question in individual_questions:
            question_name = f"individual_question_{ind_question['question_code']}"
            answer_value = ind_question['answer_id']
            individual_ovc_id = ind_question.get('ovc_cpims_id', data.get('ovc_cpims_id'))  
            individual_ovc_id = RegPerson.objects.get(pk=individual_ovc_id)
            OVCMobileEventAttribute.objects.create(
                event=event,
                # Add 'individual_ovc_id_' prefix
                ovc_cpims=individual_ovc_id,
                question_name=question_name,
                answer_value=answer_value
            )

        # Handle sub_population
        sub_population = data.get('sub_population', [])
        for sub_pop in sub_population:
            question_name = f"sub_population_{sub_pop['criteria']}"
            # answer_value = sub_pop['answer_id']
            sub_pop_ovc_id = int(sub_pop.get('ovc_cpims_id', data.get('ovc_cpims_id')))
            OVCMobileEventAttribute.objects.create(
                event=event,
                # Add 'individual_ovc_id_' prefix
                ovc_cpims_id=sub_pop_ovc_id,
                question_name=question_name,
                # answer_value=answer_value
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
                    ovc_cpims=RegPerson.objects.get(pk=data.get('ovc_cpims_id')),
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
                'ovc_cpims_id': event.ovc_cpims,
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
                    question_code = attribute.question_name[len(
                        'individual_question_'):]
                    individual_question = {
                        'question_code': question_code,
                        'answer_id': attribute_data['answer_value'],
                    }
                    # Remove the prefixes
                    ovc_cpims_id_individual = attribute_data['ovc_cpims_id_individual']
                    if ovc_cpims_id_individual.startswith('individual_ovc_id_'):
                        ovc_cpims_id_individual = ovc_cpims_id_individual[len(
                            'individual_ovc_id_'):]
                    individual_question['ovc_cpims_id'] = ovc_cpims_id_individual
                    event_data['individual_questions'].append(
                        individual_question)
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

        
        if not request.user.is_authenticated:
            return Response({'error': 'User is not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)

        # Fetch by ovc id
        events = OVCMobileEvent.objects.filter(
            ovc_cpims=ovc_id, is_accepted=1)
        
        events_list = events.values('id')
        print(events)

        # Retrieve  event attributes
        attributes = OVCMobileEventAttribute.objects.filter(
            event__in=events_list)
        
        for event in events:
            app_metadata = json.loads(event.app_form_metadata.replace("'", "\""))
            
            # get child name
            full_name= f"{event.ovc_cpims.first_name} {event.ovc_cpims.other_names} {event.ovc_cpims.surname}"
            ovc_age=event.ovc_cpims.age
            ovc_sex=get_sex_person(event.ovc_cpims.sex_id)
            event_signature = event.signature
            event_signature = event_signature.tobytes()
            event_signature = event_signature.decode('utf-8')
            # print("dir",type(event_signature))
            # breakpoint()
            
            event_data = {
                'ovc_cpims_id': event.ovc_cpims.id,               
                'ovc_name': full_name,
                'ovc_sex': ovc_sex,
                'ovc_age': ovc_age,
                'date_of_event': event.date_of_event,
                'app_form_metadata':app_metadata,
                'event_id': event.id,
                'created_at':event.created_at,
                'signature':event_signature,
                'questions': [],
                'individual_questions': [],
                'scores': [],
                'sub_population': [],
            }
            
            for attribute in attributes:
                attribute_data = {
                    'question_name': attribute.question_name,
                    'answer_value': attribute.answer_value,
                    'ovc_cpims_id': attribute.ovc_cpims,
                }

                if attribute.question_name.startswith('question_') and attribute.event_id == event.id:
                    # Remove the 'question_' prefix
                    question_code = attribute.question_name[len('question_'):]
                    event_data['questions'].append({
                        'question_code': question_code,
                        'answer_id': attribute_data['answer_value'],
                    })
                    
                elif attribute.question_name.startswith('individual_question_') and attribute.event_id == event.id:
                    full_name= f"{attribute.ovc_cpims.first_name} {attribute.ovc_cpims.other_names} {attribute.ovc_cpims.surname}"
                    ovc_cpims_id=attribute.ovc_cpims.id
                    ovc_age =attribute.ovc_cpims.age
                    ovc_sex=get_sex_person(attribute.ovc_cpims.sex_id)
                
                    #remove prefix
                    question_code = attribute.question_name[len(
                        'individual_question_'):]
                    individual_question = {
                        'question_code': question_code,
                        'answer_id': attribute_data['answer_value'],
                    }
                    # remove the prefixes
                    ovc_cpims_id_individual = attribute_data['ovc_cpims_id'].id
                    # if ovc_cpims_id_individual.startswith('individual_ovc_id_'):
                    #     ovc_cpims_id_individual = ovc_cpims_id_individual[len(
                    #         'individual_ovc_id_'):]

                    individual_question['ovc_cpims_id'] = ovc_cpims_id_individual
                    individual_question['ovc_name'] = full_name
                    individual_question['ovc_age'] = ovc_age
                    individual_question['ovc_sex'] = ovc_sex
                    
                    event_data['individual_questions'].append(
                        individual_question)

                elif attribute.question_name.startswith('sub_population_') and attribute.event_id == event.id:
                    full_name= f"{attribute.ovc_cpims.first_name} {attribute.ovc_cpims.other_names} {attribute.ovc_cpims.surname}"
                    ovc_cpims_id=attribute.ovc_cpims.id
                    ovc_age =attribute.ovc_cpims.age
                    ovc_sex=get_sex_person(attribute.ovc_cpims.sex_id)
                    
                    # Remove 'sub_population_' prefix
                    question_code = attribute.question_name[len(
                        'sub_population_'):]
                    individual_sub_pop = {
                        'criteria': question_code,

                    }
                    # remove individual_cpims_id prefixes
                    ovc_cpims_id_individual = attribute_data['ovc_cpims_id'].id
                    # if ovc_cpims_id_individual.startswith('individual_ovc_id_'):
                    #     ovc_cpims_id_individual = ovc_cpims_id_individual[len(
                    #         'individual_ovc_id_'):]
                    
                    # child = OVCRegistration.objects.get(is_void=False, person=ovc_cpims_id_individual)

                    individual_sub_pop['ovc_cpims_id'] = ovc_cpims_id_individual
                    individual_sub_pop['ovc_name'] = full_name
                    individual_sub_pop['ovc_age'] = ovc_age
                    individual_sub_pop['ovc_sex'] = ovc_sex
                    event_data['sub_population'].append(individual_sub_pop)

                elif attribute.question_name.startswith('score_') and attribute.event_id == event.id:
                    # Remove the 'score_' prefix

                    event_data['scores'].append(
                        {attribute.question_name[len('score_'):]: attribute_data['answer_value']})

            data.append(event_data)

        return Response(data, status=status.HTTP_200_OK)
    except OVCMobileEvent.DoesNotExist:
        return Response({'error': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH', 'POST'])
@permission_classes([IsAuthenticated])
def update_cpara_is_accepted(request, event_id):
    try:
        event = OVCMobileEvent.objects.get(pk=event_id)
        attributes = OVCMobileEventAttribute.objects.filter(event=event)

        
        if not request.user.is_authenticated:
            return Response({'error': 'User is not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)

        # If is_accepted is false, recreate it in the rejected tables
        is_accepted = request.data.get('is_accepted')
        print("hapa",is_accepted)
        
        if is_accepted == ApprovalStatus.TRUE.value:
            # event.is_accepted = is_accepted
            # event.save()
            try:
                event_rejected = OVCMobileEventRejected.objects.get(pk=event_id).delete()
                OVCMobileEventAttributeRejected.objects.filter(event=event_rejected).delete()
                attributes.delete()
                event.delete()
                return Response({'message': 'is_accepted updated successfully to TRUE'}, status=status.HTTP_200_OK)
            except OVCMobileEventRejected.DoesNotExist:
                attributes.delete()
                event.delete()

            return Response({'message': 'is_accepted updated successfully to TRUE'}, status=status.HTTP_200_OK)
        
        elif is_accepted == ApprovalStatus.FALSE.value:
                # is_accepted = data.get('is_accepted')
                rejected_event = event.id
                mobile_event_rejected = OVCMobileEventRejected.objects.create(
                    user=event.user,
                    ovc_cpims=event.ovc_cpims,
                    date_of_event=event.date_of_event,
                    is_accepted=is_accepted,
                    app_form_metadata=event.app_form_metadata,
                    message=request.data.get('message'),
                    id=rejected_event
                )
                print("rejected_event_id")
               
                
                for attribute in attributes:
                    
                    OVCMobileEventAttributeRejected.objects.create(
                        event=mobile_event_rejected,
                        ovc_cpims=attribute.ovc_cpims,
                        question_name=attribute.question_name,
                        answer_value=attribute.answer_value
                    )
                event.is_accepted = is_accepted
                event.save()
                return Response({'message': 'is_accepted updated successfully to FALSE'}, status=status.HTTP_200_OK)
        
        elif is_accepted == ApprovalStatus.NEUTRAL.value:
            event.is_accepted = is_accepted
            event.save()
            return Response({'message': 'is_accepted updated successfully to NEUTRAL'}, status=status.HTTP_200_OK)

        else:
            return Response({'error': 'Invalid value for is_accepted'}, status=status.HTTP_400_BAD_REQUEST)

    except OVCMobileEvent.DoesNotExist:
        return Response({'error': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    


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
def create_ovc_event(request, form_id):
    try:
        
        if not request.user.is_authenticated:
            return Response({'error': 'User is not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)

        user_id = AppUser.objects.get(pk=request.user.id) 
        
        form_type = form_id

        if form_type not in ['F1A', 'F1B']:
            return Response({'message': 'Invalid form type (F1A, F1B)'}, status=status.HTTP_400_BAD_REQUEST)

        data = request.data

        # print(f" {form_type} mobile data {data}")


        ovc_cpims_id = data.get('ovc_cpims_id', '')
       

        if not ovc_cpims_id:
            return Response({'message': 'ovc_cpims_id cannot be empty'}, status=status.HTTP_400_BAD_REQUEST)

        event_id = data.get('id')
        ovc_cpims_id = RegPerson.objects.get(pk=ovc_cpims_id)
        if event_id:
            try:
                event = OVCEvent.objects.get(pk=event_id)
                OVCServices.objects.filter(event=event).delete()
                event.delete()                
            except OVCServices.DoesNotExist:
                return Response({'Alert': 'Record with provided id is not found'}, status=status.HTTP_404_NOT_FOUND)


            event = OVCEvent.objects.create(
                id=event_id,
                ovc_cpims=ovc_cpims_id,
                date_of_event=data.get('date_of_event'),
                form_type=form_type,
                user=user_id,
                app_form_metadata=json.dumps(data.get('app_form_metadata'))
            )
           
        else:
            event = OVCEvent.objects.create(
                ovc_cpims=ovc_cpims_id,
                date_of_event=data.get('date_of_event'),
                form_type=form_type,
                user=user_id,
                app_form_metadata=json.dumps(data.get('app_form_metadata'))
            )

        
        services = data.get('services', [])
        critical_events = data.get('critical_events', [])
        for service_data in services:
            OVCServices.objects.create(
                id=uuid.uuid4(),
                event=event,
                domain_id=service_data.get('domain_id', ''),
                service_id=service_data.get('service_id', ''),
                is_accepted=ApprovalStatus.NEUTRAL.value,
            )

        for c_event in critical_events:
            domain_id = f'critical_key_{c_event.get("event_id", "")}'
            service_id = f'critical_value_{c_event.get("event_date", "")}'
            OVCServices.objects.create(
                id=uuid.uuid4(),
                event=event,
                domain_id=domain_id,
                service_id=service_id,
                is_accepted=ApprovalStatus.NEUTRAL.value,
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
                    'ovc_cpims_id': event.ovc_cpims,
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
            services_data = OVCServices.objects.filter(
                event__form_type=form_type, event__ovc_cpims=ovc_id,
                is_accepted=1).values(
                'event_id', 'event__ovc_cpims_id', 'event__date_of_event',
                'domain_id', 'service_id', 'is_accepted', 'id',
            ).order_by('event_id')
                
            
        else:
            return Response({'error': 'Enter a valid form type: F1A or F1B'})

        event_dict = {}
        for service in services_data:

            event_id = service['event_id']
            event = OVCEvent.objects.get(pk=event_id)
            
            full_name= f"{event.ovc_cpims.first_name} {event.ovc_cpims.other_names} {event.ovc_cpims.surname}"
            app_metadata = json.loads(event.app_form_metadata.replace("'", "\""))
            ovc_sex=get_sex_person(event.ovc_cpims.sex_id)
            ovc_age=event.ovc_cpims.age
           
            
            if event_id not in event_dict:
                print(service['event__ovc_cpims_id'])
                event_dict[event_id] = {
                    'ovc_cpims_id': service['event__ovc_cpims_id'],
                    'ovc_name': full_name,
                    'date_of_event': service['event__date_of_event'],
                    'event_id': event_id,
                    'app_form_metadata':app_metadata,
                    'ovc_sex':ovc_sex,
                    'ovc_age':ovc_age,
                    'services': [],
                    'critical_events': [],
                }

            # Check if the domain_id starts with 'critical_'
            if service['domain_id'].startswith('critical_'):
                critical_event_id = service['domain_id'][len('critical_key_'):]
                
                # Add the critical event
                event_dict[event_id]['critical_events'].append({
                    'event_id': critical_event_id,
                    'id': service['id'],
                    'event_date': service['event__date_of_event'],
                })
            else:
                # Add service to event
                event_dict[event_id]['services'].append({
                    'event_id': service['event_id'],
                    'domain_id': service['domain_id'],
                    'service_id': service['service_id'],
                    'is_accepted': service['is_accepted'],
                    'id': service['id']
                })


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
        # breakpoint()
        service = OVCServices.objects.get(id=id)
        is_accepted = request.data.get('is_accepted')
        count_service_by_event = OVCServices.objects.filter(event_id=service.event.id).count()
        if is_accepted is not None:
            if is_accepted == ApprovalStatus.FALSE.value:
                try:
                    # Try to get an existing rejected event
                    rejected_event = OVCEventRejected.objects.get(id=service.event.id)

                except OVCEventRejected.DoesNotExist:
                    # If it doesn't exist, create the rejected event
                    rejected_event = OVCEventRejected.objects.create(
                        id=service.event.id,
                        user=service.event.user,
                        ovc_cpims=service.event.ovc_cpims,
                        date_of_event=service.event.date_of_event,
                        form_type=service.event.form_type,
                        app_form_metadata=service.event.app_form_metadata
                    )

                # Create the corresponding rejected service
                OVCServicesRejected.objects.create(
                    event=rejected_event,
                    id=service.id,
                    domain_id=service.domain_id,
                    service_id=service.service_id,
                    is_accepted=is_accepted,
                    message=request.data.get('message')
                )

                # Update the is_accepted field for the original service
                service.is_accepted = is_accepted
                service.save()
                return Response({'message': 'is_accepted updated successfully'}, status=status.HTTP_200_OK)


            
            elif is_accepted == ApprovalStatus.TRUE.value:
                try:
                    sevice_rej = OVCServicesRejected.objects.get(id=id)
                    count_service_by_event_rej = OVCServicesRejected.objects.filter(event_id=sevice_rej.event.id).count()
                    sevice_rej.delete()
                    
                    
                    service.delete() 
                    if count_service_by_event <2 :                   
                        print(f"deleted services : {count_service_by_event}")
                        OVCEvent.objects.get(id=service.event.id).delete()
                    if count_service_by_event_rej <2 :                   
                        OVCEventRejected.objects.get(id=service.event.id).delete()

                    

                    return Response({'message': 'form accepted successfully'}, status=status.HTTP_200_OK)

                except Exception as e:
                    OVCServices.objects.get(id=id).delete()
                    if count_service_by_event <2 :                   
                        print(f"deleted services : {count_service_by_event}")
                        OVCEvent.objects.get(id=service.event.id).delete()

                return Response({'message': 'form accepted successfully'}, status=status.HTTP_200_OK)

            else:
                return Response({'error': 'Invalid value for is_accepted'}, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response({'error': 'is_accepted field is required in the request body'}, status=status.HTTP_400_BAD_REQUEST)

    except OVCServices.DoesNotExist:
        return Response({'error': 'Service not found'}, status=status.HTTP_404_NOT_FOUND)
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
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_case_plan_template(request):
    try:
        payload = request.data
        print(f"CPT mobile data {payload}")
        
        if not request.user.is_authenticated:
            return Response({'error': 'User is not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)

        user_id = AppUser.objects.get(pk=request.user.id) 
        event_id = payload.get('id')
        
        ovc_cpims_id = payload['ovc_cpims_id']
        ovc_cpims_id=RegPerson.objects.get(pk=ovc_cpims_id)
        
        try:
            event = CasePlanTemplateEvent.objects.get(pk=event_id)
            event.ovc_cpims=ovc_cpims_id
            event.date_of_event=payload['date_of_event'].split('T')[0]
            event.app_form_metadata=json.dumps(payload['app_form_metadata'])
            event.save()
            
            
        except CasePlanTemplateEvent.DoesNotExist:
            # Create a new CasePlanTemplateEvent
            event = CasePlanTemplateEvent.objects.create(
                ovc_cpims=ovc_cpims_id,
                date_of_event=payload['date_of_event'].split('T')[0],
                user=user_id,
                app_form_metadata=json.dumps(payload['app_form_metadata']),
               
            )

        # Create a record for each service
        services = payload['services']
        for service in services:
            completion_date = service['completion_date']
            print("sssssssssss", len(completion_date))
            if len(completion_date.strip()) == 0:
                completion_date = None
            else:
                completion_date = service['completion_date'].split('T')[0]
                print(service['completion_date'])
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
                completion_date=completion_date,
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
                'ovc_cpims_id': event.ovc_cpims,
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

        servicess = CasePlanTemplateService.objects.filter(
            event__in=events, is_accepted=1)

        event_data = []
        for event in events:  
            full_name= f"{event.ovc_cpims.first_name} {event.ovc_cpims.other_names} {event.ovc_cpims.surname}"
            app_metadata = json.loads(event.app_form_metadata.replace("'", "\""))
            ovc_sex=get_sex_person(event.ovc_cpims.sex_id)
           
            services = servicess.filter(event=event)
            event_data.append({
                'event_id': event.id,
                'ovc_cpims_id': event.ovc_cpims.id,
                'ovc_sex': ovc_sex,
                'app_form_metadata':app_metadata,
                'ovc_name': full_name,
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
        service = CasePlanTemplateService.objects.get(
            unique_service_id=unique_service_id)
        # breakpoint()
        event = service.event
        rejected_event=service.event_id

        new_is_accepted = request.data.get('is_accepted')
        if new_is_accepted is not None:
            # Check if is_accepted is set to False (3)
            if new_is_accepted == ApprovalStatus.FALSE.value:
                
                # Create a corresponding rejected record in CasePlanTemplateEventRejected
                event_rejected, created = CasePlanTemplateEventRejected.objects.update_or_create(
                    id=rejected_event,
                    defaults={
                        'user': event.user,
                        'ovc_cpims': event.ovc_cpims,
                        'date_of_event': event.date_of_event,
                        'app_form_metadata': event.app_form_metadata
                    }
                )

                # Create the corresponding rejected service
                CasePlanTemplateServiceRejected.objects.create(
                    unique_service_id=service.unique_service_id,
                    event=event_rejected,
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
                return Response({'message': 'is_accepted updated successfully to FALSE'}, status=status.HTTP_200_OK)

            
            elif new_is_accepted == ApprovalStatus.TRUE.value:
                try:
                    reject_service = CasePlanTemplateServiceRejected.objects.get(unique_service_id=unique_service_id)
                    count_event_reject_service = CasePlanTemplateEventRejected.objects.filter(id = reject_service.event.pk).count()
                    if count_event_reject_service < 2:
                        reject_service.delete()
                        CasePlanTemplateEventRejected.objects.get(id=reject_service.event.id).delete()
                    
                    accept_service = CasePlanTemplateService.objects.get(unique_service_id=unique_service_id)
                    count_accept_service_event = CasePlanTemplateEvent.objects.get(id=accept_service.event.id).count()
                    accept_service.delete()
                    if count_accept_service_event < 2 :
                        CasePlanTemplateEvent.objects.get(id=service.event.id).delete()
                    return Response({'message': 'is_accepted updated successfully to TRUE'}, status=status.HTTP_200_OK)

                
                except Exception as e :
                    # CasePlanTemplateService.objects.get(unique_service_id=unique_service_id).delete()
                    # CasePlanTemplateEvent.objects.get(id=service.event.id).delete()
                    return Response({'message': 'is_accepted updated successfully to TRUE'}, status=status.HTTP_200_OK)
                    
 
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


# Hiv screening
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_ovc_hiv_screening(request):
    try:
        data = request.data

        user_id = AppUser.objects.get(pk=request.user.id) 

        ovc_cpims_id = handle_Null(RegPerson.objects.get(pk=data.get('ovc_cpims_id')) )
        event_id = handle_Null(data.get('adherence_id'))
        app_form = json.dumps(data.get('app_form_metadata'))
        

        if not request.user.is_authenticated:
            return Response({'error': 'User is not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)

        # Check id exists
        try:
            hiv_rs = RiskScreeningStaging.objects.get(pk=event_id)

            for model_field, payload_field in hrs_field_mapping.items():

                hiv_rs.model_field = data.get(handle_Null(payload_field))

            
        except RiskScreeningStaging.DoesNotExist:
            # Create a new record
            print("type",type(ovc_cpims_id))
            hiv_rs = RiskScreeningStaging(
                ovc_cpims=ovc_cpims_id,
                user=user_id,
                app_form_metadata=app_form
            )
            
            for model_field, payload_field in hrs_field_mapping.items():
                print(model_field, payload_field)
                setattr(hiv_rs, model_field, handle_Null(data.get(payload_field)))

                # hiv_rs.model_field = data.get(payload_field)
        
        hiv_rs.save()                
            
        return Response({'message': 'HRS record created successfully'}, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    



 # Hiv Management

@api_view(['PATCH', 'POST'])
@permission_classes([IsAuthenticated])
def update_hiv_screening(request, risk_id):
    try:
        screening = RiskScreeningStaging.objects.get(risk_id=risk_id)

        new_is_accepted = request.data.get('is_accepted')
        if new_is_accepted is not None:
            # Check if is_accepted is set to False (3)            
            if new_is_accepted == ApprovalStatus.FALSE.value:
                # Create rejected records
                RiskScreeningStagingRejected.objects.create(
                    risk_id = screening.risk_id,
                    ovc_cpims = screening.ovc_cpims,
                    date_of_event = screening.date_of_event,
                    test_done_when = screening.test_done_when,
                    test_donewhen_result = screening.test_donewhen_result,
                    caregiver_know_status = screening.caregiver_know_status,
                    caregiver_knowledge_yes = screening.caregiver_knowledge_yes,
                    parent_PLWH = screening.parent_PLWH,
                    child_sick_malnourished = screening.child_sick_malnourished,
                    child_sexual_abuse = screening.child_sexual_abuse,
                    traditional_procedure = screening.traditional_procedure,
                    adol_sick = screening.adol_sick,
                    adol_had_tb = screening.adol_had_tb,
                    adol_sexual_abuse = screening.adol_sexual_abuse,
                    sex = screening.sex,
                    sti = screening.sti,
                    sharing_needles = screening.sharing_needles,
                    hiv_test_required = screening.hiv_test_required,
                    parent_consent_testing = screening.parent_consent_testing,
                    parent_consent_date = screening.parent_consent_date,  ###date new 1
                    referral_made = screening.referral_made,
                    referral_made_date = screening.referral_made_date, ####
                    referral_completed = screening.referral_completed,
                    referral_completed_date = screening.referral_completed_date, ### date new 2
                    not_completed = screening.not_completed,
                    test_result = screening.test_result,
                    art_referral = screening.art_referral,
                    art_referral_date = screening.art_referral_date, #### date
                    art_referral_completed = screening.art_referral_completed,
                    art_referral_completed_date = screening.art_referral_completed_date,  #### date
                    facility_code = screening.facility_code,
                    is_accepted = new_is_accepted,
                    user = screening.user,
                    message = request.data.get('message'),
                    app_form_metadata = screening.app_form_metadata
                )

                # Update the is_accepted field for the original screening
                screening.is_accepted = new_is_accepted
                screening.save()
            
            elif new_is_accepted == ApprovalStatus.TRUE.value:
                try:
                    RiskScreeningStagingRejected.objects.get(risk_id=risk_id).delete()
                    RiskScreeningStaging.objects.get(risk_id=risk_id).delete()
                except Exception as e:
                    RiskScreeningStaging.objects.get(risk_id=risk_id).delete()
                

            return Response({'message': 'is_accepted updated successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'is_accepted field is required in the request body'}, status=status.HTTP_400_BAD_REQUEST)
    except RiskScreeningStaging.DoesNotExist:
        return Response({'error': 'Risk screening not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_one_hiv_screening(request, ovc_id):
    try:
        data = []
        # Check authenticatication
        if not request.user.is_authenticated:
            return Response({'error': 'User is not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
        
        # Fetch by ovc id
        hiv_management_events = RiskScreeningStaging.objects.filter(ovc_cpims=ovc_id, is_accepted=1)
        #data = [model_to_dict_custom(event) for event in hiv_management_events]
        
        for event in hiv_management_events:
            full_name= f"{event.ovc_cpims.first_name} {event.ovc_cpims.other_names} {event.ovc_cpims.surname}"
            app_metadata = json.loads(event.app_form_metadata.replace("'", "\""))
            ovc_sex=get_sex_person(event.ovc_cpims.sex_id)
            ovc_age=event.ovc_cpims.age
            
            event.app_form_metadata =app_metadata
            model_dict = model_to_dict_custom(event)
            model_dict['ovc_name']=full_name
            model_dict['ovc_sex']=ovc_sex
            model_dict['ovc_age']=ovc_age
            
            data.append(model_dict)

        return Response(data, status=status.HTTP_200_OK)
    except RiskScreeningStaging.DoesNotExist:
        return Response({'error': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)    

# hiv management
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_ovc_hiv_management(request):
    try:
        data = request.data
        print(f"hmf mobile data {data}")
        user_id = AppUser.objects.get(pk=request.user.id) 
        ovc_cpims_id = handle_Null(RegPerson.objects.get(pk=data.get('ovc_cpims_id')) )
        event_id = handle_Null(data.get('adherence_id'))
        app_form = json.dumps(data.get('app_form_metadata'))
        

        
        if not request.user.is_authenticated:
            return Response({'error': 'User is not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)

        # Check id exists
        try:
            hiv_management = HIVManagementStaging.objects.get(pk=event_id)

            for model_field, payload_field in hmf_field_mapping.items():

                hiv_management.model_field = data.get(handle_Null(payload_field))

            
        except HIVManagementStaging.DoesNotExist:
            # Create a new record
            hiv_management = HIVManagementStaging(
                ovc_cpims=ovc_cpims_id,
                user=user_id,
                app_form_metadata=app_form
            )
            
            for model_field, payload_field in hmf_field_mapping.items():
                print("vbn",model_field, payload_field)
                setattr(hiv_management, model_field, handle_Null(data.get(payload_field)))

                # hiv_management.model_field = data.get(payload_field)
        
        hiv_management.save()                
            
        return Response({'message': 'HIV Management record created successfully'}, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

   
   
   
 # Fetch unaccepted records      

@api_view(['PATCH', 'POST'])
@permission_classes([IsAuthenticated])
def update_hiv_management(request, adherence_id):
    try:
        service = HIVManagementStaging.objects.get(adherence_id=adherence_id)
        adherence_id=service.adherence_id

        new_is_accepted = request.data.get('is_accepted')
        if new_is_accepted is not None:
            # Check if is_accepted is set to False (3)
            
            if new_is_accepted == ApprovalStatus.FALSE.value:
                # Create rejected records
                HIVManagementStagingRejected.objects.create(
                    adherence_id = adherence_id,
                    ovc_cpims = service.ovc_cpims,
                    hiv_confirmed_date = service.hiv_confirmed_date,
                    treatment_initiated_date = service.treatment_initiated_date,
                    baseline_hei = service.baseline_hei,
                    firstline_start_date = service.firstline_start_date,
                    substitution_firstline_arv = service.substitution_firstline_arv,
                    substitution_firstline_date = service.substitution_firstline_date,
                    switch_secondline_arv = service.switch_secondline_arv,
                    switch_secondline_date = service.switch_secondline_date,
                    switch_thirdline_arv = service.switch_thirdline_arv,
                    switch_thirdline_date = service.switch_thirdline_date,
                    visit_date = service.visit_date,
                    duration_art = service.duration_art,
                    height = service.height,
                    adherence = service.adherence,
                    adherence_drugs_duration = service.adherence_drugs_duration,
                    adherence_counselling = service.adherence_counselling,
                    treatment_supporter = service.treatment_supporter,
                    treatment_supporter_relationship = service.treatment_supporter_relationship,
                    treatment_supporter_gender = service.treatment_supporter_gender,
                    treatment_supporter_age = service.treatment_supporter_age,
                    treatment_supporter_hiv = service.treatment_supporter_hiv,
                    viral_load_results = service.viral_load_results,
                    viral_load_date = service.viral_load_date,
                    detectable_viralload_interventions = service.detectable_viralload_interventions,
                    disclosure = service.disclosure,
                    muac_score = service.muac_score,
                    bmi = service.bmi,
                    nutritional_support = service.nutritional_support,
                    support_group_status = service.support_group_status,
                    nhif_enrollment = service.nhif_enrollment,
                    nhif_status = service.nhif_status,
                    referral_services = service.referral_services,
                    nextappointment_date = service.nextappointment_date,
                    peer_educator_name = service.peer_educator_name,
                    peer_educator_contact = service.peer_educator_contact,
                    date_of_event = service.date_of_event,
                    message=request.data.get('message'),
                    user = service.user,
                    is_accepted = new_is_accepted,
                    app_form_metadata = service.app_form_metadata
                    # You can leave the following as commented code
                    # weight = service.weight,
                    # muac = service.muac,
                    # currentregimen = service.currentregimen,
                    # enoughdrugs = service.enoughdrugs,
                    # attendingsuppportgroup = service.attendingsuppportgroup,
                    # pamacare = service.pamacare,
                    # enrolledotz = service.enrolledotz,
                    # is_void = service.equivalent,
                    # support_group_enrollment = service.support_group_enrollment,

                )
                
                # Update the is_accepted field for the original service
                service.is_accepted = new_is_accepted
                service.save()
                return Response({'message': 'is_accepted updated successfully'}, status=status.HTTP_200_OK)

            elif new_is_accepted == ApprovalStatus.TRUE.value:
                try:
                    HIVManagementStagingRejected.objects.get(adherence_id=adherence_id).delete()
                    HIVManagementStaging.objects.get(adherence_id=adherence_id).delete()
                

                except Exception as e:
                    HIVManagementStaging.objects.get(adherence_id=adherence_id).delete()
            return Response({'message': 'is_accepted updated successfully'}, status=status.HTTP_200_OK)
          
   
        else:
            return Response({'error': 'is_accepted field is required in the request body'}, status=status.HTTP_400_BAD_REQUEST)
    except HIVManagementStaging.DoesNotExist:
        return Response({'error': 'HMF  not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_one_hiv_management(request, ovc_id):
    try:
        data = []
        # Check authenticatication
        if not request.user.is_authenticated:
            return Response({'error': 'User is not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
        
        # Fetch by ovc id
        hiv_management_events = HIVManagementStaging.objects.filter(ovc_cpims=ovc_id, is_accepted=1)
        # data = [model_to_dict_custom(event) for event in hiv_management_events]
        
        for event in hiv_management_events:
            full_name= f"{event.ovc_cpims.first_name} {event.ovc_cpims.other_names} {event.ovc_cpims.surname}"
            app_metadata = json.loads(event.app_form_metadata.replace("'", "\""))
            ovc_sex=get_sex_person(event.ovc_cpims.sex_id)
            ovc_age=event.ovc_cpims.age
            
            event.app_form_metadata =app_metadata
            model_dict = model_to_dict_custom(event)
            model_dict['ovc_name']=full_name
            model_dict['ovc_sex']=ovc_sex
            model_dict['ovc_age']=ovc_age
            
            data.append(model_dict)

        return Response(data, status=status.HTTP_200_OK)
    except HIVManagementStaging.DoesNotExist:
        return Response({'error': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

# fetch  all unnapproved records

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_unaccepted_records(request):
    try:

        data = []

        
        if not request.user.is_authenticated:
            return Response({'error': 'User is not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)

        # Fetch cpara records where is_accepted is FALSE (3) and user_id matches
        ovc_mobile_events_rejected = OVCMobileEventRejected.objects.filter(
            is_accepted=3, user=request.user.id)

        if ovc_mobile_events_rejected:
            for rejected_event in ovc_mobile_events_rejected:
                app_metadata = json.loads(rejected_event.app_form_metadata.replace("'", "\""))
                event_data = {
                    'id':rejected_event.id,
                    'ovc_cpims_id': rejected_event.ovc_cpims,
                    'message': rejected_event.message,
                    'date_of_event': rejected_event.date_of_event,
                    'app_form_metadata':app_metadata,
                    'questions': [],
                    'individual_questions': [],
                    'scores': {},
                }

                # Retrieve  related rejected event
                attributes = OVCMobileEventAttributeRejected.objects.filter(
                    event=rejected_event)

                for attribute in attributes:
                    attribute_data = {
                        'question_name': attribute.question_name,
                        'answer_value': attribute.answer_value,
                        'ovc_cpims_id': attribute.ovc_cpims,
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
                        question_code = attribute.question_name[len(
                            'individual_question_'):]
                        individual_question = {
                            'question_code': question_code,
                            'answer_id': attribute_data['answer_value'],
                        }
                        # Aremove the prefixes
                        ovc_cpims_id_individual = attribute_data['ovc_cpims_id'].id
                        if str(ovc_cpims_id_individual).startswith('individual_ovc_id_'):
                            ovc_cpims_id_individual = ovc_cpims_id_individual[len(
                                'individual_ovc_id_'):]
                        individual_question['ovc_cpims_id'] = ovc_cpims_id_individual
                        event_data['individual_questions'].append(
                            individual_question)
                        
                    elif attribute.question_name.startswith('score_'):
                        # Remove the 'score_' prefix
                        key = attribute.question_name[len('score_'):]
                        event_data['scores'][key] = attribute_data['answer_value']
               
                
            data.append(event_data)
        
       
       
        #fetch Rejected F1A and B
        ovc_services_rejected = OVCServicesRejected.objects.filter(
            is_accepted=3, event__user=request.user.id)
        grouped_data = {}

        if ovc_services_rejected:
            for service_rejected in ovc_services_rejected:              
                app_metadata = json.loads(service_rejected.event.app_form_metadata.replace("'", "\""))
                service_id = service_rejected.event.id
                ovc_cpims_id = service_rejected.event.ovc_cpims
                app_metadata = app_metadata
                event_id = None
                event_date = None
                domain_id = None
                ind_service_id = None
                print("service_rejected",type(ovc_cpims_id))

                
                if service_rejected.domain_id.startswith("critical_key_"):
                    event_id = service_rejected.domain_id.replace("critical_key_", "")
                    event_date = service_rejected.service_id.replace("critical_value_", "")
                else:
                    domain_id = service_rejected.domain_id
                    ind_service_id = service_rejected.service_id
                    
                    
                if service_id in grouped_data:
                    # append 'services'
                    if not service_rejected.domain_id.startswith("critical_key_"):
                        grouped_data[service_id]['services'].append({
                            'id': service_rejected.id,
                            'domain_id': service_rejected.domain_id,
                            'service_id': service_rejected.service_id,
                            'message': service_rejected.message,
                        })
                    # append 'critical_events'
                    elif event_id is not None and event_date is not None:
                        grouped_data[service_id]['critical_events'].append({
                            'id': service_rejected.id,
                            'event_id': event_id,
                            'event_date': event_date,
                            'message': service_rejected.message,
                        })
                else:
                    # Create a new entry in the dictionary
                    grouped_data[service_id] = {
                        'ovc_cpims_id': ovc_cpims_id,
                        'app_form_metadata':app_metadata,
                        'id': service_rejected.event.id,  
                        'date_of_event': service_rejected.event.date_of_event,
                        'services': [] if domain_id is None or ind_service_id is None else [{
                            'id': service_rejected.id,
                            'service_id': ind_service_id,
                            'domain_id': domain_id,
                            'message': service_rejected.message,
                        }],
                        'critical_events': [] if event_id is None or event_date is None else [{
                            'id': service_rejected.id,
                            'event_id': event_id,
                            'event_date': event_date,
                            'message': service_rejected.message,
                        }]
                    }
                

            data = data + list(grouped_data.values())


        # Fetch CasePlanTemplate records where is_accepted is FALSE (3) and user_id matches
        case_plan_services_rejected = CasePlanTemplateServiceRejected.objects.filter(
            is_accepted=3, event__user=request.user.id)
        if case_plan_services_rejected:
         
            for service_rejected in case_plan_services_rejected:
               
                app_metadata = json.loads(service_rejected.event.app_form_metadata.replace("'", "\""))
                event_data = {
                    'id':service_rejected.event.id,
                    'ovc_cpims_id': service_rejected.event.ovc_cpims,
                    'date_of_event': service_rejected.event.date_of_event,
                    'message': service_rejected.message,
                    'app_metadata':app_metadata,
                    'services': {
                        'domain_id': service_rejected.domain_id,
                        'service_id': service_rejected.service_id,
                        'goal_id': service_rejected.goal_id,
                        'priority_id': service_rejected.priority_id,
                        'responsible_id': service_rejected.responsible_id,
                        'results_id': service_rejected.results_id,
                        'reason_id': service_rejected.reason_id,
                        'completion_date': service_rejected.reason_id
                    },
                }
            data.append(event_data)
 
        
        # Fetch unaccepted HIV_Management records for and OVC
        hiv_management_rejected = HIVManagementStagingRejected.objects.filter(is_accepted=3, user=request.user.id)
        if hiv_management_rejected:
            for hiv_management in hiv_management_rejected:   
                app_metadata = json.loads(hiv_management.app_form_metadata.replace("'", "\""))
              
                event_data = {
                    'adherence_id':hiv_management.adherence_id,
                    'ovc_cpims_id': hiv_management.ovc_cpims,
                    'hiv_confirmed_date': hiv_management.hiv_confirmed_date,
                    'treatment_initiated_date': hiv_management.treatment_initiated_date,
                    'baseline_hei': hiv_management.baseline_hei,
                    'firstline_start_date': hiv_management.firstline_start_date,
                    'substitution_firstline_arv': hiv_management.substitution_firstline_arv,
                    'substitution_firstline_date': hiv_management.substitution_firstline_date,
                    'switch_secondline_arv': hiv_management.switch_secondline_arv,
                    'switch_secondline_date': hiv_management.switch_secondline_date,
                    'switch_thirdline_arv': hiv_management.switch_thirdline_arv,
                    'switch_thirdline_date': hiv_management.switch_thirdline_date,
                    'visit_date': hiv_management.visit_date,
                    'duration_art': hiv_management.duration_art,
                    'height': hiv_management.height,
                    'adherence': hiv_management.adherence,
                    'adherence_drugs_duration': hiv_management.adherence_drugs_duration,
                    'adherence_counselling': hiv_management.adherence_counselling,
                    'treatment_supporter': hiv_management.treatment_supporter,
                    'treatment_supporter_relationship': hiv_management.treatment_supporter_relationship,
                    'treatment_supporter_gender': hiv_management.treatment_supporter_gender,
                    'treatment_supporter_age': hiv_management.treatment_supporter_age,
                    'treatment_supporter_hiv': hiv_management.treatment_supporter_hiv,
                    'viral_load_results': hiv_management.viral_load_results,
                    'viral_load_date': hiv_management.viral_load_date,
                    'detectable_viralload_interventions': hiv_management.detectable_viralload_interventions,
                    'disclosure': hiv_management.disclosure,
                    'muac_score': hiv_management.muac_score,
                    'bmi': hiv_management.bmi,
                    'nutritional_support': hiv_management.nutritional_support,
                    'support_group_status': hiv_management.support_group_status,
                    'nhif_enrollment': hiv_management.nhif_enrollment,
                    'nhif_status': hiv_management.nhif_status,
                    'referral_services': hiv_management.referral_services,
                    'nextappointment_date': hiv_management.nextappointment_date,
                    'peer_educator_name': hiv_management.peer_educator_name,
                    'peer_educator_contact': hiv_management.peer_educator_contact,
                    'date_of_event': hiv_management.date_of_event,
                    'app_metadata':app_metadata,
                    # 'weight': hiv_management.equivalent,
                    # 'muac': hiv_management.mUAC,
                    # 'currentregimen': hiv_management.equivalent,
                    # 'enoughdrugs': hiv_management.equivalent,
                    # 'attendingsuppportgroup': hiv_management.equivalent,
                    # 'pamacare': hiv_management.equivalent,
                    # 'enrolledotz': hiv_management.equivalent,
                    # 'is_void': hiv_management.equivalent,
                    # 'support_group_enrollment': hiv_management.equivalent,
                    }
            data.append(event_data)
    
            
        # Fetch unaccepted HIV Screening records for an Ovc
        hiv_screening_rejected = RiskScreeningStagingRejected.objects.filter(is_accepted=3, user=request.user.id)
  
        if hiv_screening_rejected:
            for hiv_screening in hiv_screening_rejected:
                app_metadata = json.loads(hiv_screening.app_form_metadata.replace("'", "\""))
                event_data = {
                    'risk_id': hiv_screening.risk_id,
                    'ovc_cpims_id': hiv_screening.ovc_cpims,
                    'date_of_event': hiv_screening.date_of_event,
                    'test_done_when': hiv_screening.test_done_when,
                    'test_donewhen_result': hiv_screening.test_donewhen_result,
                    'caregiver_know_status': hiv_screening.caregiver_know_status,
                    'caregiver_knowledge_yes': hiv_screening.caregiver_knowledge_yes,
                    'parent_PLWH': hiv_screening.parent_PLWH,
                    'child_sick_malnourished': hiv_screening.child_sick_malnourished,
                    'child_sexual_abuse': hiv_screening.child_sexual_abuse,
                    'traditional_procedure': hiv_screening.traditional_procedure,
                    'adol_sick': hiv_screening.adol_sick,
                    'adol_had_tb': hiv_screening.adol_had_tb,
                    'adol_sexual_abuse': hiv_screening.adol_sexual_abuse,
                    'sex': hiv_screening.sex,
                    'sti': hiv_screening.sti,
                    'sharing_needles': hiv_screening.sharing_needles,
                    'hiv_test_required': hiv_screening.hiv_test_required,
                    'parent_consent_testing': hiv_screening.parent_consent_testing,
                    'parent_consent_date': hiv_screening.parent_consent_date,
                    'referral_made': hiv_screening.referral_made,
                    'referral_made_date': hiv_screening.referral_made_date,
                    'referral_completed': hiv_screening.referral_completed,
                    'referral_completed_date': hiv_screening.referral_completed_date,
                    'not_completed': hiv_screening.not_completed,
                    'test_result': hiv_screening.test_result,
                    'art_referral': hiv_screening.art_referral,
                    'art_referral_date': hiv_screening.art_referral_date,
                    'art_referral_completed': hiv_screening.art_referral_completed,
                    'art_referral_completed_date': hiv_screening.art_referral_completed_date,
                    'facility_code': hiv_screening.facility_code,
                    'is_accepted': hiv_screening.is_accepted,
                    'user_id': hiv_screening.user,
                    'message': request.data.get('message'),
                    'app_metadata':app_metadata,
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
            ovc_services_rejected = OVCServicesRejected.objects.filter(
                is_accepted=3, event__user=request.user.id, event__form_type=form_type)
            print(ovc_services_rejected)
            grouped_data = {}

            if ovc_services_rejected:
                for service_rejected in ovc_services_rejected:
                    print(service_rejected)
                    app_metadata = json.loads(service_rejected.event.app_form_metadata.replace("'", "\""))
                    service_id = service_rejected.event.id
                    ovc_cpims_id = service_rejected.event.ovc_cpims.id
                    app_metadata = app_metadata
                    event_id = None
                    event_date = None
                    domain_id = None
                    ind_service_id = None
                    

                    
                    if service_rejected.domain_id.startswith("critical_key_"):
                        event_id = service_rejected.domain_id.replace("critical_key_", "")
                        event_date = service_rejected.service_id.replace("critical_value_", "")
                    else:
                        domain_id = service_rejected.domain_id
                        ind_service_id = service_rejected.service_id
                        
                    print("12344",domain_id)
                    if service_id in grouped_data:
                        # append 'services'
                        if not service_rejected.domain_id.startswith("critical_key_"):
                            grouped_data[service_id]['services'].append({
                                'id': service_rejected.id,
                                'domain_id': service_rejected.domain_id,
                                'service_id': service_rejected.service_id,
                                'message': service_rejected.message,
                            })
                        # append 'critical_events'
                        elif event_id is not None and event_date is not None:
                            grouped_data[service_id]['critical_events'].append({
                                'id': service_rejected.id,
                                'event_id': event_id,
                                'event_date': event_date,
                                'message': service_rejected.message,
                            })
                    else:
                        # Create a new entry in the dictionary
                        grouped_data[service_id] = {
                            'ovc_cpims_id': ovc_cpims_id,
                            'app_form_metadata':app_metadata,
                            'id': service_rejected.event.id,  
                            'date_of_event': service_rejected.event.date_of_event,
                            'services': [] if domain_id is None or ind_service_id is None else [{
                                'id': service_rejected.id,
                                'service_id': ind_service_id,
                                'domain_id': domain_id,
                                'message': service_rejected.message,
                            }],
                            'critical_events': [] if event_id is None or event_date is None else [{
                                'id': service_rejected.id,
                                'event_id': event_id,
                                'event_date': event_date,
                                'message': service_rejected.message,
                            }]
                        }
                data = data + list(grouped_data.values())

                # delete_parent_and_children(
                    # OVCEventRejected, OVCServicesRejected, service.event.id)
            
                
        elif form_type == 'cpara':
            # Fetch cpara records where is_accepted is FALSE (3) and user_id matches
            cpara_events = OVCMobileEventRejected.objects.filter(
                is_accepted=3, user=request.user.id)

            for event in cpara_events:
                app_metadata = json.loads(event.app_form_metadata.replace("'", "\""))
                event_data = {
                    'id':event.id,
                    'ovc_cpims_id': event.ovc_cpims.id,
                    'date_of_event': event.date_of_event,
                    'app_form_metadata': app_metadata,
                    'questions': [],
                    'individual_questions': [],
                    'scores': {},
                }

                attributes = OVCMobileEventAttributeRejected.objects.filter(
                    event=event)

                for attribute in attributes:
                    attribute_data = {
                        'question_name': attribute.question_name,
                        'answer_value': attribute.answer_value,
                        'ovc_cpims_id': attribute.ovc_cpims,
                    }

                    if attribute.question_name.startswith('question_'):
                        question_code = attribute.question_name[len(
                            'question_'):]
                        event_data['questions'].append({
                            'question_code': question_code,
                            'answer_id': attribute_data['answer_value'],
                        })
                    elif attribute.question_name.startswith('individual_question_'):
                        question_code = attribute.question_name[len(
                            'individual_question_'):]
                        individual_question = {
                            'question_code': question_code,
                            'answer_id': attribute_data['answer_value'],
                        }

                        ovc_cpims_id_individual = attribute_data['ovc_cpims_id'].id

                        if str(ovc_cpims_id_individual).startswith('individual_ovc_id_'):
                            ovc_cpims_id_individual = ovc_cpims_id_individual[len(
                                'individual_ovc_id_'):]

                        individual_question['ovc_cpims_id'] = ovc_cpims_id_individual
                        event_data['individual_questions'].append(
                            individual_question)
                    elif attribute.question_name.startswith('score_'):
                        key = attribute.question_name[len('score_'):]
                        event_data['scores'][key] = attribute_data['answer_value']

                data.append(event_data)


        elif form_type == 'cpt':
            # Fetch CasePlanTemplate records where is_accepted is FALSE (3) and user_id matches
            case_plan_services = CasePlanTemplateServiceRejected.objects.filter(
                is_accepted=3, event__user_id=request.user.id)
            
            events = CasePlanTemplateEventRejected.objects.filter(user_id=request.user.id)

            servicess = CasePlanTemplateServiceRejected.objects.filter(
                event__in=events, is_accepted=3)

        
            for event in events:  
                full_name= f"{event.ovc_cpims.first_name} {event.ovc_cpims.other_names} {event.ovc_cpims.surname}"
                app_metadata = json.loads(event.app_form_metadata.replace("'", "\""))
                ovc_sex=get_sex_person(event.ovc_cpims.sex_id)
                
                services = servicess.filter(event=event)
                event_data={
                    'event_id': event.id,
                    'ovc_cpims_id': event.ovc_cpims.id,
                    'app_form_metadata':app_metadata,
                    'date_of_event': event.date_of_event,
                    'services': [service_serializer(service) for service in services]
                }
        

                data.append(event_data)
                
                            
        elif form_type == 'hmf':
            
            # Fetch unaccepted HIV_Management records for and OVC
            hiv_management_rejected = HIVManagementStagingRejected.objects.filter(is_accepted=3, user=request.user.id)         
            for hiv_management in hiv_management_rejected:
                app_metadata = json.loads(hiv_management.app_form_metadata.replace("'", "\""))
                event_data = {
                    'adherence_id':hiv_management.adherence_id,
                    'ovc_cpims_id': hiv_management.ovc_cpims.id,
                    'hiv_confirmed_date': hiv_management.hiv_confirmed_date,
                    'treatment_initiated_date': hiv_management.treatment_initiated_date,
                    'baseline_hei': hiv_management.baseline_hei,
                    'firstline_start_date': hiv_management.firstline_start_date,
                    'substitution_firstline_arv': hiv_management.substitution_firstline_arv,
                    'substitution_firstline_date': hiv_management.substitution_firstline_date,
                    'switch_secondline_arv': hiv_management.switch_secondline_arv,
                    'switch_secondline_date': hiv_management.switch_secondline_date,
                    'switch_thirdline_arv': hiv_management.switch_thirdline_arv,
                    'switch_thirdline_date': hiv_management.switch_thirdline_date,
                    'visit_date': hiv_management.visit_date,
                    'duration_art': hiv_management.duration_art,
                    'height': hiv_management.height,
                    'adherence': hiv_management.adherence,
                    'adherence_drugs_duration': hiv_management.adherence_drugs_duration,
                    'adherence_counselling': hiv_management.adherence_counselling,
                    'treatment_supporter': hiv_management.treatment_supporter,
                    'treatment_supporter_relationship': hiv_management.treatment_supporter_relationship,
                    'treatment_supporter_gender': hiv_management.treatment_supporter_gender,
                    'treatment_supporter_age': hiv_management.treatment_supporter_age,
                    'treatment_supporter_hiv': hiv_management.treatment_supporter_hiv,
                    'viral_load_results': hiv_management.viral_load_results,
                    'viral_load_date': hiv_management.viral_load_date,
                    'detectable_viralload_interventions': hiv_management.detectable_viralload_interventions,
                    'disclosure': hiv_management.disclosure,
                    'muac_score': hiv_management.muac_score,
                    'bmi': hiv_management.bmi,
                    'nutritional_support': hiv_management.nutritional_support,
                    'support_group_status': hiv_management.support_group_status,
                    'nhif_enrollment': hiv_management.nhif_enrollment,
                    'nhif_status': hiv_management.nhif_status,
                    'referral_services': hiv_management.referral_services,
                    'nextappointment_date': hiv_management.nextappointment_date,
                    'peer_educator_name': hiv_management.peer_educator_name,
                    'peer_educator_contact': hiv_management.peer_educator_contact,
                    'date_of_event': hiv_management.date_of_event,
                    'app_form_metadata': app_metadata,
                    'message':hiv_management.message,
                    # 'weight': hiv_management.equivalent,
                    # 'muac': hiv_management.mUAC,
                    # 'currentregimen': hiv_management.equivalent,
                    # 'enoughdrugs': hiv_management.equivalent,
                    # 'attendingsuppportgroup': hiv_management.equivalent,
                    # 'pamacare': hiv_management.equivalent,
                    # 'enrolledotz': hiv_management.equivalent,
                    # 'is_void': hiv_management.equivalent,
                    # 'support_group_enrollment': hiv_management.equivalent,
                    }
                data.append(event_data)

        
        elif form_type == 'hrs':
            hrs_rejected = []
            # Fetch unaccepted hiv_screening_rejected records for and OVC
            hiv_screening_rejected = RiskScreeningStagingRejected.objects.filter(is_accepted=3, user=request.user.id)
            print(f" load : {hiv_screening_rejected}  userId:  {request.user.id} form  {form_type}")
            
            for risk_screening in hiv_screening_rejected:
                app_metadata = json.loads(risk_screening.app_form_metadata.replace("'", "\""))
                print(app_metadata)
                event_data = {
                    'risk_id':risk_screening.risk_id,
                    'ovc_cpims_id': risk_screening.ovc_cpims.id,
                    'date_of_event': risk_screening.date_of_event,
                    'test_done_when': risk_screening.test_done_when,
                    'test_donewhen_result': risk_screening.test_donewhen_result,
                    'caregiver_know_status': risk_screening.caregiver_know_status,
                    'caregiver_knowledge_yes': risk_screening.caregiver_knowledge_yes,
                    'parent_PLWH': risk_screening.parent_PLWH,
                    'child_sick_malnourished': risk_screening.child_sick_malnourished,
                    'child_sexual_abuse': risk_screening.child_sexual_abuse,
                    'traditional_procedure': risk_screening.traditional_procedure,
                    'adol_sick': risk_screening.adol_sick,
                    'adol_had_tb': risk_screening.adol_had_tb,
                    'adol_sexual_abuse': risk_screening.adol_sexual_abuse,
                    'sex': risk_screening.sex,
                    'sti': risk_screening.sti,
                    'sharing_needles': risk_screening.sharing_needles,
                    'hiv_test_required': risk_screening.hiv_test_required,
                    'parent_consent_testing': risk_screening.parent_consent_testing,
                    'parent_consent_date': risk_screening.parent_consent_date,
                    'referral_made': risk_screening.referral_made,
                    'referral_made_date': risk_screening.referral_made_date,
                    'referral_completed': risk_screening.referral_completed,
                    'referral_completed_date': risk_screening.referral_completed_date,
                    'not_completed': risk_screening.not_completed,
                    'test_result': risk_screening.test_result,
                    'art_referral': risk_screening.art_referral,
                    'art_referral_date': risk_screening.art_referral_date,
                    'art_referral_completed': risk_screening.art_referral_completed,
                    'art_referral_completed_date': risk_screening.art_referral_completed_date,
                    'facility_code': risk_screening.facility_code,
                    'is_accepted': risk_screening.is_accepted,
                    'message': risk_screening.message,
                    'app_form_metadata': app_metadata,
                    }
                # hrs_rejected.append(event_data)
                
                data.append(event_data)

        
        else:
            return JsonResponse({'error': 'Unknown report type'}, status=400)

        return JsonResponse(data, status=200, safe=False)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


# Front end validation login

@login_required
# @is_allowed_user_groups(['DAP'])
def mobile_home(request):
    """Method to do pivot reports."""
    
    hmfhrs = json.loads(read_json_fixture('hfm_hrs.json').content)
 
    form1b = OVCCareEAV.objects.filter(
        event='b4e0d636-34e8-11e9-9e13-e4a471adc5eb')
    try:
        summary = {}
        form = mobile_approve()
        lip_name = request.session.get('ou_primary_name')
        lip_id = request.session.get('ou_primary')

        chvss = OVCRegistration.objects.filter(
            is_void=False, child_cbo_id=lip_id).distinct('child_chv_id')
        care_quiz = OVCCareQuestions.objects.filter(
            is_void=False, code__startswith="CP")
        cpt_fields = ['case_plan_services_school', 'case_plan_services_safe',
                      'case_plan_services_stable', 'case_plan_services_health',
                      'case_plan_goals_school', 'case_plan_goals_safe',
                      'case_plan_goals_stable', 'case_plan_goals_health',
                      'case_plan_gaps_school', 'case_plan_gaps_safe',
                      'case_plan_gaps_stable', 'case_plan_gaps_health',
                      'case_plan_priorities_school', 'ovc_domain_id',
                      'case_plan_priorities_safe',
                      'case_plan_priorities_stable',
                      'case_plan_priorities_health',
                      ]
        cpt_list = get_dict(field_name=cpt_fields)
        f1b_fields = ['form1b_items', 'olmis_domain_id',
                      'olmis_protection_service_id', 'olmis_hes_service_id',
                      'olmis_health_service_id', 'olmis_shelter_service_id',
                      'olmis_pss_service_id', 'olmis_education_service_id',
                      'olmis_critical_event_id', 'caregiver_critical_event_id']
        f1b_list = get_dict(field_name=f1b_fields)
        summary['CHV'] = chvss.count()
        chvs = []
        for chv in chvss:
            chvs.append({
                'cpims_chv_id': chv.child_chv.pk,
                'name': f"{chv.child_chv.full_name}"
            })
        chv_list = chvss.values('child_chv_id')
        childrens = OVCRegistration.objects.filter(
            is_void=False, child_chv_id__in=chv_list).values('person_id')
        
        # count cpara unapproved
        cpr_count=OVCMobileEvent.objects.filter(is_accepted=1, ovc_cpims__in=childrens).count()

        # count Case plan template unapproved
        event_ids = CasePlanTemplateEvent.objects.filter(ovc_cpims__in=childrens)
        result = (
            CasePlanTemplateService.objects
            .filter(is_accepted=True, event_id__in=event_ids)
            .values('event_id')
            .annotate(event_count=Count('event_id'))
        )
        # Filtering only events with at least one record where is_accepted is True
        cpt_count = result.filter(event_count__gt=0).count()

        # count F1A and F1B unapproved
        event_ids_f1a = OVCEvent.objects.filter(ovc_cpims__in=childrens, form_type='F1A')
        event_ids_f1b = OVCEvent.objects.filter(ovc_cpims__in=childrens, form_type='F1B')
        result_f1a = (
            OVCServices.objects
            .filter(is_accepted=True, event_id__in=event_ids_f1a)
            .values('event_id')
            .annotate(event_count=Count('event_id'))
        )

        result_f1b = (
            OVCServices.objects
            .filter(is_accepted=True, event_id__in=event_ids_f1b)
            .values('event_id')
            .annotate(event_count=Count('event_id'))
        )
        # Filtering only events with at least one record where is_accepted is True
        f1a_count = result_f1a.filter(event_count__gt=0).count()
        f1b_count = result_f1b.filter(event_count__gt=0).count()

        # count HMF and HRS unapproved
        hmf_count=HIVManagementStaging.objects.filter(is_accepted=1, ovc_cpims__in=childrens).count()
        hrs_count=RiskScreeningStaging.objects.filter(is_accepted=1, ovc_cpims__in=childrens).count()

        
        print(f"CPT-> {cpt_count} CPR-> {cpr_count} F1A-> {f1a_count} F1B-> {f1b_count} HMF-> {hmf_count} HRS-> {hrs_count}")      
        summary['CPT'] = cpt_count
        summary['CPR'] = cpr_count
        summary['F1A'] = f1a_count
        summary['F1B'] = f1b_count
        summary['HMF'] = hmf_count
        summary['HRS'] = hrs_count

        return render(
            request, 'mobile/home.html',
            {
                'form': form,
                'formdata': form1b,
                'chvs': chvs,
                'lip_name': lip_name,
                'quizzes': care_quiz,
                'cptlist': cpt_list,
                'f1blist': f1b_list,
                'summary': summary,
                'hiv_form': hmfhrs 

            }
        )
    except Exception as e:
        raise e
    else:
        pass


def mobiledataapproval(request):
    message = {}
    try:
        if request.method == "POST":
            data = request.POST
            if(data):
                app_id = data.get('data[id]')
                app_form = data.get('data[form]').upper()
                print(
                    f">>>>>approval data {data} ")

                if app_form == 'CPR':
                    ovc_mobile_event = OVCMobileEvent.objects.get(id=app_id)
                    ovc_mobile_event.approved_initiated = True
                    ovc_mobile_event.save()
                if app_form == 'CPT':
                    cpt_mobile_event = CasePlanTemplateService.objects.get(id=app_id)
                    cpt_mobile_event.approved_initiated = True
                    cpt_mobile_event.save()
                if app_form == 'F1A':
                    f1a_mobile_event = OVCServices.objects.get(id=app_id)
                    f1a_mobile_event.approved_initiated = True
                    f1a_mobile_event.save()
                if app_form == 'F1B':
                    f1b_mobile_event = OVCServices.objects.get(id=app_id)
                    f1b_mobile_event.approved_initiated = True
                    f1b_mobile_event.save()
                if app_form == 'HRS':
                    hrs_mobile_event = RiskScreeningStaging.objects.get(id=app_id)
                    hrs_mobile_event.approved_initiated = True
                    hrs_mobile_event.save()
                if app_form == 'HMF':
                    hrs_mobile_event = HIVManagementStaging.objects.get(id=app_id)
                    hrs_mobile_event.approved_initiated = True
                    hrs_mobile_event.save()
    
            response_data = {
                "status": "success",
                "message": "Data received and processed successfully."
            }
            message.update(response_data)
        else:
            message.update({"error": "Invalid request method."})
    except Exception as e:
        print(f"Mark initiated approval error?: {e}")

    return JsonResponse(message, safe=False)

def fetchChildren(request):
    children = []
    if request.method == "POST":
        data = request.POST.getlist('data[]')
        childrens = OVCRegistration.objects.filter(
            is_void=False, child_chv_id__in=data).select_related('person').order_by(F('person__first_name'))
        for child in childrens:
            children.append({
                'cpims_ovc_id': child.person.pk,
                'name': child.person.full_name,
                'cpims_ovc_id':  child.person.id
            })

        # Do something with the data, e.g., save to a database
        response_data = {
            "message": "Data received and processed successfully."}
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

        formdata = []
        if (form_sel == 'cpr'):

            events = OVCMobileEvent.objects.filter(
                ovc_cpims__in=child_sel, is_accepted=1)
            form_datas = OVCMobileEventAttribute.objects.filter(
                event__in=events)
            dta = {}
            indx = 0
            for event in events:
                indx += 1
                for form_dta in form_datas.values():
                    if(event.id == form_dta['event_id']):
                        dta[form_dta['question_name']
                            ] = form_dta['answer_value']
                        dta['name'] = form_datas[indx].event.ovc_cpims.full_name
                        dta['date_of_event'] = form_datas[indx].event.date_of_event
                        dta['id'] = form_datas[indx].event.id
                        print(form_dta)
                formdata.append(dta)

            print(f"form_data {formdata}")
            # print(f"{form_sel} - {chv_sel} - {child_sel} -- {form_data}")
        elif((form_sel == 'cpt')):

            events = CasePlanTemplateEvent.objects.filter(
                ovc_cpims__in=child_sel)
            form_datas = CasePlanTemplateService.objects.filter(
                event__in=events, is_accepted=1)
            formdata = []
            indx = 0
            for form_dta in form_datas.values():
                dta = {}
               
                for form_dt in form_dta.keys():
                    answer = form_dta[form_dt]
                    dta[form_dt] = answer
                dta['name'] = form_datas[indx].event.ovc_cpims.full_name
                dta['date_of_event'] = form_datas[indx].event.date_of_event
                indx += 1
                formdata.append(dta)

        elif((form_sel == 'form1a')):

            events = OVCEvent.objects.filter(ovc_cpims__in=child_sel)
            form_datas = OVCServices.objects.filter(
                event__in=events, is_accepted=1)
            formdata = []
            indx = 0
            for form_dta in form_datas.values():
                dta = {}
               
                for form_dt in form_dta.keys():
                    answer = form_dta[form_dt]
                    dta[form_dt] = answer
                dta['name'] = form_datas[indx].event.ovc_cpims.full_name
                dta['date_of_event'] = form_datas[indx].event.date_of_event
                indx += 1
                formdata.append(dta)
        elif((form_sel == 'form1b')):

            events = OVCEvent.objects.filter(ovc_cpims__in=child_sel)
            form_datas = OVCServices.objects.filter(
                event__in=events, is_accepted=1)
            formdata = []
            indx = 0
            for form_dta in form_datas.values():
                dta = {}
                
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
