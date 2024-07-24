from django.test import SimpleTestCase
from django.urls import reverse, resolve
from cpovc_offline_mode.views import templates, fetch_data, fetch_services, submit_form


class URLTests(SimpleTestCase):

    def test_template_url_is_resolves(self):
        url = reverse('templates')
        # print(resolve(url))
        self.assertEqual(resolve(url).func, templates)

    def test_fetch_data_url_is_resolves(self):
        url = reverse('fetch_data')
        self.assertEqual(resolve(url).func, fetch_data)

    def test_list_url_is_resolves(self):
        url = reverse('fetch_services')
        self.assertEqual(resolve(url).func, fetch_services)

    def test_submit_form_is_resolves(self):
        url = reverse('submit_form')
        # print(resolve(url))
        self.assertEqual(resolve(url).func, submit_form)
