# Views Testcases
from multiprocessing.connection import Client
from django.urls import reverse
from django.test import SimpleTestCase


class TestViews(SimpleTestCase):

    def setUp(self):
        self.client = Client()
        self.ovc_home_url = reverse('ovc_home')
        self.ovc_search_url = reverse('ovc_search')
        self.ovc_edit_url = reverse('ovc_edit')
        self.ovc_register_url = reverse('ovc_register')
        self.ovc_view_url = reverse('ovc_view')
        self.hh_manage_url = reverse('hh_manage')
        self.ovc_manage_url = reverse('ovc_manage')

    def ovc_home(self):
        response = self.client.post(self.ovc_home_url, )

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'ovc/home.html')

    def ovc_search(self):
        response = self.client.post(self.ovc_search_url, )

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, '')

    def ovc_edit(self):
        response = self.client.post(self.ovc_edit_url, )

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'ovc/edit_child.html')

    def ovc_register(self):
        response = self.client.post(self.ovc_register_url, )

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'ovc/register_child.html')

    def ovc_view(self):
        response = self.client.post(self.ovc_view_url, )

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'ovc/view_child.html')

    def ovc_manage(self):
        response = self.client.post(self.ovc_manage_url, )

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, '')

    def hh_manage(self):
        response = self.client.post(self.hh_manage_url,)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, '')

