from django.test import TestCase
from cpovc_auth.models import AppUser

class CpovTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        AppUser.objects.create(role='Big', username='Bob')
        AppUser.objects.create(role='Small', username='Boy')

    def test_common_access(self):
        """Animals that can speak are correctly identified"""
        # Big = CommonAccess.objects.get(name="lion")
        # Small = CommonAccess.objects.get(name="cat")
        comm = AppUser.objects.get(id=1)
        field_label = comm._meta.get_field('role').verbose_name
        self.assertEqual(field_label, 'role')

