from django.test import TestCase
from cpovc_access.models import CommonAccess

class GreatTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        CommonAccess.objects.create(user_agent='Big', ip_address="12.00.03.4", username='Bob', trusted=True, http_accept="http char", path_info="path info")


    def test_common_access(self):
        """Animals that can speak are correctly identified"""
        # Big = CommonAccess.objects.get(name="lion")
        # Small = CommonAccess.objects.get(name="cat")
        comm = CommonAccess.Objects.get(id=1)
        field_label = comm._meta.get_field('user_agent').verbose_name
        self.assertEqual(field_label, 'user agent')

