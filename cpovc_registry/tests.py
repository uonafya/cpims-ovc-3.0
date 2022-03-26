from django.test import TestCase
from cpovc_registry.models import RegOrgUnit

class GreatTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        RegOrgUnit.objects.create(org_unit_id_vis='Big', org_unit_name='Bob')


    def test_common_access(self):
        """Animals that can speak are correctly identified"""
        # Big = CommonAccess.objects.get(name="lion")
        # Small = CommonAccess.objects.get(name="cat")
        comm = RegOrgUnit.objects.get(id=1)
        field_label = comm._meta.get_field('org_unit_name').verbose_name
        self.assertEqual(field_label, 'org unit name')



# import json
# from django.test import TestCase
# from django.urls import reverse, resolve
# from django.test.client import Client
# from cpovc_registry.forms import (RegistrationSearchForm, RegOrgUnitAdmin, OrgUnitAuditAdmin,
#                                   PersonsAuditAdmin, RegPersonTypesAdmin, RegPersonAdmin,)
# from cpovc_registry import admin
# from cpovc_registry.views import (home, register_new, new_user, register_edit, register_details,
#                 persons_search, new_user, person_actions, new_person, edit_person,
#                 delete_person, registry_look,view_person )
#
# # TestCase for urls
# class Testurls(TestCase):
#
#     def test_list_url_isresolved(self):
#         url = reverse('registry')
#         self.assertEquals(resolve(url).func, home)
#
#     def test_list_url_isresolved(self):
#         url = reverse('registry_edit')
#         self.assertEquals(resolve(url).func, register_edit)
#
#     def test_list_url_isresolved(self):
#         url = reverse('register_details')
#         self.assertEquals(resolve(url).func, register_details)
#
#     def test_list_url_isresolved(self):
#         url = reverse('registry_new')
#         self.assertEquals(resolve(url).func, register_new)
#
#     def test_list_url_isresolved(self):
#         url = reverse('search_persons')
#         self.assertEquals(resolve(url).func, persons_search)
#
#     def test_list_url_isresolved(self):
#         url = reverse('new_user')
#         self.assertEquals(resolve(url).func, new_user)
#
#     def test_list_url_isresolved(self):
#         url = reverse('person_action')
#         self.assertEquals(resolve(url).func, person_actions)
#
#     def test_list_url_isresolved(self):
#         url = reverse('new_person')
#         self.assertEquals(resolve(url).func, new_person)
#
#     def test_list_url_isresolved(self):
#         url = reverse('edit_person')
#         self.assertEquals(resolve(url).func, edit_person)
#
#     def test_list_url_isresolved(self):
#         url = reverse('view_person')
#         self.assertEquals(resolve(url).func, view_person)
#
#     def test_list_url_isresolved(self):
#         url = reverse('delete_person')
#         self.assertEquals(resolve(url).func, delete_person)
#
#     def test_list_url_isresolved(self):
#         url = reverse('reg_lookup')
#         self.assertEquals(resolve(url).func, registry_look)
#
#
#
#
# # Views Testcases
#
# class TestViews(TestCase):
#
#     def setUp(self):
#         self.client = Client()
#         self.home_url = reverse('registry')
#         self.register_new_url = reverse('registry_new')
#         self.register_edit_url = reverse('registry_edit')
#         self.register_details_url = reverse('register_details')
#         self.persons_search_url = reverse('search_persons')
#         self.view_person_url = reverse('view_person')
#         self.edit_person_url = reverse('edit_person')
#         self.new_user_url = reverse('new_user')
#         self.registry_look_url = reverse('reg_look')
#         self.persons_actions_url = reverse('person_actions')
#         self.new_person_url = reverse('new_person')
#
#     def test_home_POST(self):
#         response = self.client.post(self.home_url, )
#
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'registry/org_units_index.html')
#
#     def test_register_new_POST(self):
#         response = self.client.post(self.register_new_url, )
#
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'registry/org_units_new.html')
#
#     def test_register_edit_POST(self):
#         response = self.client.post(self.register_edit_url, )
#
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'registry/org_units_edit.html')
#
#     def test_register_details_POST(self):
#         response = self.client.post(self.register_details_url, )
#
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'registry/org_units_details.html')
#
#     def test_new_person_POST(self):
#         response = self.client.post(self.register_details_url, )
#
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'registry/person_new.html')
#
#     def test_person_search_POST(self):
#         response = self.client.post(self.persons_search_url, )
#
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'registry/person_search.html')
#
#     def test_edit_person_POST(self):
#         response = self.client.post(self.edit_person_url, )
#
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'registry/person_edit.html')
#
#     def test_new_user_POST(self):
#         response = self.client.post(self.new_user_url, )
#
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'registry/new_user.html')
#
#     def test_registry_look_POST(self):
#         response = self.client.post(self.registry_look_url, )
#
#         self.assertEquals(response.status_code, 200)
#
#     def test_persons_action_POST(self):
#         response = self.client.post(self.persons_actions_url, )
#
#         self.assertEquals(response.status_code, 200)
#
#
# #Forms TestCases
#
# """class MyTests(TestCase):
#     def test_forms(self):
#         form_data = {'something': 'something'}
#         form = MyForm(data=form_data)
#         self.assertTrue(form.is_valid())
#         ... # other tests relating forms, for example checking the form data"""
#
#
#
#
# class RegPersonTypesAdminTestCase(TestCase):
#     def setUpTestData(cls):
#         admin.RegPersonTypesAdmin.search_fields = ['Mwajuma', 'Sidi']
#         admin.RegPersonTypesAdmin.list_display = ['1', 'Sidi Manajuma', 'temporary',
#                     '12/12/2017', 'False', ]
#
#
#
#
