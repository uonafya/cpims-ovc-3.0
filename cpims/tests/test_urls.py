from django.test import SimpleTestCase
from django.urls import reverse, resolve
from cpims.views import public_dashboard_reg, public_dashboard_hivstat

class URLTests(SimpleTestCase):

    def test_public_dashboard_reg_url_is_resolves(self):
        url = reverse('public_dashboard_reg')
        self.assertEquals(resolve(url).func, public_dashboard_reg)
    def test_public_dashboard_hivstat_url_is_resolves(self):
        url = reverse('public_dashboard_hivstat')
        self.assertEquals(resolve(url).func, public_dashboard_hivstat)