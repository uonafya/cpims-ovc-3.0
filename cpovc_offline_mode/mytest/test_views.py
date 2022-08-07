import unittest

from django.test import TestCase, Client
from django.urls import reverse
import json
from cpovc_offline_mode.helpers import get_services
from cpovc_offline_mode.views import fetch_data
from cpovc_auth.models import AppUser
from cpovc_registry.models import RegPerson


class TestViews(TestCase):

    # def create_test_views(self, user_orgs=10, org_units=None):
    #     if org_units is None:
    #         org_units = ['great']

    def test_Templates_view(self):
        client = Client()
        response = client.get(reverse('templates'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ovc/home_offline.html')
        self.assertTemplateUsed(response, 'ovc/view_child_offline.html')
        self.assertTemplateUsed(response, 'forms/form1b_offline.html')

    def test_fetch_services_view(self):
        client = Client()
        response = client.get(reverse('fetch_services'))
        assert response.status_code == 200
        assert response.json() == {'data': str(get_services())}
        # self.assertEqual(json.loads(response.content)['data'], [])

    def test_fetch_data_view(self):
        # self.create_test_views()
        reg = RegPerson.objects.create(first_name='Ivan3', surname="Bowen")
        user = AppUser.objects.create(username='Ivan3', password='Ivan3', reg_person_id=1)
        reg.save()
        user.save()
        c = Client()
        login = self.client.login(username='Ivan3', password='Ivan3')
        resp = c.post('/login/', {'username': 'Ivan3', 'password': 'Ivan3'})
        self.assertEqual(resp.status_code, 200)
        response = c.get(reverse('fetch_data'))
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

    def test_submit_form_views(self):
        client = Client()
        response = client.get(reverse('submit_form'))
        self.assertEqual(response.status_code, 200)
        # assert response.context() == {'msg': 'ok'}


