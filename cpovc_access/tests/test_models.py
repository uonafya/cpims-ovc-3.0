from django.test import TestCase
from cpovc_access.models import CommonAccess

class GreatTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        CommonAccess.objects.create(user_agent='Big', username='Bob')
        CommonAccess.objects.create(user_agent='Small', username='Boy')

    def test_common_access(self):
        """Animals that can speak are correctly identified"""
        # Big = CommonAccess.objects.get(name="lion")
        # Small = CommonAccess.objects.get(name="cat")
        comm = CommonAccess.objects.get(id=1)
        field_label = comm._meta.get_field('user_agent').verbose_name
        self.assertEqual(field_label, 'user agent')

