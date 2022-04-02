from django.test import TestCase
from django.urls import reverse
from django.test.client import Client


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
        response = self.client.post(self.register_edit_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registry/org_units_edit.html')

    def test_register_details_POST(self):
        response = self.client.post(self.register_details_url)

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
        response = self.client.post(self.edit_person_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registry/person_edit.html')

    def test_new_user_POST(self):
        response = self.client.post(self.new_user_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registry/new_user.html')

    def test_registry_look_POST(self):
        response = self.client.post(self.registry_look_url, )

        self.assertEquals(response.status_code, 200)

    def test_person_action_POST(self):
        response = self.client.post(self.persons_actions_url, )

        self.assertEquals(response.status_code, 200)
