from django.test import TestCase
from django.urls import reverse, resolve
from cpovc_registry.functions import org_id_generator
from cpovc_registry.views import (home, register_new, new_user, register_edit, register_details,
                persons_search, new_user, person_actions, new_person, edit_person,
                delete_person, registry_look,view_person )

 
# TestCase for urls
class Testurls(TestCase):

    def test_list_url_isresolved(self):
        url = reverse('registry')
        self.assertEquals(resolve(url).func, home)

    def test_list_url_isresolved(self):
        url = reverse('registry_edit', args=[12])
        self.assertEquals(resolve(url).func, register_edit)

    def test_list_url_isresolved(self):
        url = reverse('register_details', args=[1])
        self.assertEquals(resolve(url).func, register_details)

    def test_list_url_isresolved(self):
        url = reverse('registry_new')
        self.assertEquals(resolve(url).func, register_new)

    def test_list_url_isresolved(self):
        url = reverse('search_persons')
        self.assertEquals(resolve(url).func, persons_search)

    def test_list_url_isresolved(self):
        url = reverse('new_user', args=[2])
        self.assertEquals(resolve(url).func, new_user)

    def test_list_url_isresolved(self):
        url = reverse('person_actions')
        self.assertEquals(resolve(url).func, person_actions)

    def test_list_url_isresolved(self):
        url = reverse('new_person')
        self.assertEquals(resolve(url).func, new_person)

    def test_list_url_isresolved(self):
        url = reverse('edit_person', args=[1])
        self.assertEquals(resolve(url).func, edit_person)

    def test_list_url_isresolved(self):
        url = reverse('view_person', args=[1])
        self.assertEquals(resolve(url).func, view_person)

    def test_list_url_isresolved(self):
        url = reverse('delete_person', args=[1])
        self.assertEquals(resolve(url).func, delete_person)

    def test_list_url_isresolved(self):
        url = reverse('reg_lookup')
        self.assertEquals(resolve(url).func, registry_look)


