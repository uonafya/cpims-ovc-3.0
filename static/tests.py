
import json
from django.test import TestCase
from django.urls import reverse, resolve
from django.test.client import Client
from cpovc_registry.forms import (RegistrationSearchForm, RegOrgUnitAdmin, OrgUnitAuditAdmin,
                                  PersonsAuditAdmin, RegPersonTypesAdmin, RegPersonAdmin,)
from cpovc_registry import admin
from cpovc_registry.views import (home, register_new, new_user, register_edit, register_details,
                persons_search, new_user, person_actions, new_person, edit_person,
                delete_person, registry_look,view_person )

from cpovc_registry.models import (RegOrgUnit, RegOrgUnitContact, RegBiometric, RegPersonsContact,
                                     RegPerson, RegPersonsTypes)
 
# TestCase for urls
class Testurls(TestCase):

    def test_list_url_isresolved(self):
        url = reverse('registry')
        self.assertEquals(resolve(url).func, home)

    def test_list_url_isresolved(self):
        url = reverse('registry_edit')
        self.assertEquals(resolve(url).func, register_edit)

    def test_list_url_isresolved(self):
        url = reverse('register_details')
        self.assertEquals(resolve(url).func, register_details)

    def test_list_url_isresolved(self):
        url = reverse('registry_new')
        self.assertEquals(resolve(url).func, register_new)

    def test_list_url_isresolved(self):
        url = reverse('search_persons')
        self.assertEquals(resolve(url).func, persons_search)

    def test_list_url_isresolved(self):
        url = reverse('new_user')
        self.assertEquals(resolve(url).func, new_user)

    def test_list_url_isresolved(self):
        url = reverse('person_action')
        self.assertEquals(resolve(url).func, person_actions)

    def test_list_url_isresolved(self):
        url = reverse('new_person')
        self.assertEquals(resolve(url).func, new_person)

    def test_list_url_isresolved(self):
        url = reverse('edit_person')
        self.assertEquals(resolve(url).func, edit_person)

    def test_list_url_isresolved(self):
        url = reverse('view_person')
        self.assertEquals(resolve(url).func, view_person)

    def test_list_url_isresolved(self):
        url = reverse('delete_person')
        self.assertEquals(resolve(url).func, delete_person)

    def test_list_url_isresolved(self):
        url = reverse('reg_lookup')
        self.assertEquals(resolve(url).func, registry_look)




# Views Testcases

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('registry')
        self.register_new_url = reverse('registry_new')
        self.register_edit_url = reverse('registry_edit')
        self.register_details_url = reverse('register_details')
        self.persons_search_url = reverse('search_persons')
        self.view_person_url = reverse('view_person')
        self.edit_person_url = reverse('edit_person')
        self.new_user_url = reverse('new_user')
        self.registry_look_url = reverse('reg_look')
        self.persons_actions_url = reverse('person_actions')
        self.new_person_url = reverse('new_person')

    def test_home_POST(self):
        response = self.client.post(self.home_url,)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registry/org_units_index.html')

    def test_register_new_POST(self):
        response = self.client.post(self.register_new_url, )

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registry/org_units_new.html')

    def test_register_edit_POST(self):
        response = self.client.post(self.register_edit_url,org_id=2)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registry/org_units_edit.html')

    def test_register_details_POST(self):
        response = self.client.post(self.register_details_url, org_id=2 )

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registry/org_units_details.html')

    def test_new_person_POST(self):
        response = self.client.post(self.register_details_url, )

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registry/person_new.html')

    def test_person_search_POST(self):
        response = self.client.post(self.persons_search_url, )

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registry/person_search.html')

    def test_edit_person_POST(self):
        response = self.client.post(self.edit_person_url, id=2)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registry/person_edit.html')

    def test_new_user_POST(self):
        response = self.client.post(self.new_user_url, id=2)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registry/new_user.html')

    def test_registry_look_POST(self):
        response = self.client.post(self.registry_look_url, )

        self.assertEquals(response.status_code, 200)

    def test_person_action_POST(self):
        response = self.client.post(self.persons_actions_url, )

        self.assertEquals(response.status_code, 200)


# Models tests
class RegPerson(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        RegPerson.objects.create(first_name='Big', last_name='Bob')

    def test_first_name_label(self):
        regperson = RegPerson.objects.get(id=1)
        field_label = regperson._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first name')

    def test_date_of_death_label(self):
        regperson = RegPerson.objects.get(id=1)
        field_label = author._meta.get_field('date_of_death').verbose_name
        self.assertEqual(field_label, 'died')

    def test_first_name_max_length(self):
        regperson = RegPerson.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 100)

    def test_object_name_is_last_name_comma_first_name(self):
        regperson = RegPerson.objects.get(id=1)
        expected_object_name = f'{author.last_name}, {author.first_name}'
        self.assertEqual(str(author), expected_object_name)

    def test_get_absolute_url(self):
        regperson = RegPerson.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(author.get_absolute_url(), 'include path to regperson')
    
    ### RegPersonGaurdianDetails

class RegPersonGaurdianDetails(TestCase):
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        RegPersonGaurdianDetails.objects.create(first_name='Michoma', last_name='Saruni')

    def test_child_person_label(self):
        regpersongaurdiandetails = RegPersonGaurdianDetails.objects.get(id=1)
        field_label = regpersongaurdiandetails._meta.get_field('child_person').verbose_name
        self.assertEqual(field_label, 'child_person')

    def test_gaurdian_person_label(self):
        regpersongaurdiandetails = RegPersonGaurdianDetails.objects.get(id=1)
        field_label = regpersongaurdiandetails._meta.get_field('gaurdian_person').verbose_name
        self.assertEqual(field_label, 'gaurdian_person')

    def test_first_name_max_length(self):
        regpersongaurdiandetails = RegPersonGaurdianDetails.objects.get(id=1)
        max_length = regpersongaurdiandetails._meta.get_field('relationship').max_length
        self.assertEqual(max_length, 100)

    def test_object_name_is_last_name_comma_first_name(self):
        regpersongaurdiandetails = RegPersonGaurdianDetails.objects.get(id=1)
        expected_object_name = f'{regpersongaurdiandetails.last_name}, {regpersongaurdiandetails.first_name}'
        self.assertEqual(str(regpersongaurdiandetails), expected_object_name)

    def test_get_absolute_url(self):
        regpersongaurdiandetails = RegPersonGaurdianDetails.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(author.get_absolute_url(), 'path to the regpersongaurdiandetails')

    
   ###RegPersonsGeo details
class RegPersonsGeo (TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        RegPersonGeo.objects.create(first_name='Michoma', last_name='Saruni')

    def test_person_label(self):
        regpersonsgeo = RegPersonGeo.objects.get(id=1)
        field_label = regpersonsgeo._meta.get_field('person').verbose_name
        self.assertEqual(field_label, 'person')

    def test_area_label(self):
        regpersonsgeo = Author.objects.get(id=1)
        field_label = refpersonsgeo._meta.get_field('area').verbose_name
        self.assertEqual(field_label, 'area')

    def test_area_type_length(self):
        regpersonsgeo = RegPersonsGeo.objects.get(id=1)
        max_length = regpersonsgeo._meta.get_field('are_type').max_length
        self.assertEqual(max_length, 4)

    def test_object_name_is_last_name_comma_first_name(self):
        regpersonsgeo = RegPersonGeo.objects.get(id=1)
        expected_object_name = f'{regpersongeo.last_name}, {regpersonsgeo.first_name}'
        self.assertEqual(str(regpersonsgeo), expected_object_name)

    def test_get_absolute_url(self):
        regpersonsgeo = RegPersonsGeo.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(author.get_absolute_url(), 'path to reg personsgeo')

    def test_person_timeline(self):
        response = self.client.get('person/tl/person_timeline')
        self.assertEqual(response.status_code, 200)



start_date = '2002-01-01'
fmt = '%Y-%m-%d'

new_date = datetime.strptime(start_date, fmt)
todate = datetime.now()

print(new_date)
