from django.test import TestCase
from cpovc_registry.models import RegOrgUnit

class GreatTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        RegOrgUnit.objects.create(org_unit_d_vis='BigAutoVIxBanTahhagdy', org_unt_name='great')


    def test_common_access(self):
        """Animals that can speak are correctly identified"""
        # Big = CommonAccess.objects.get(name="lion")
        # Small = CommonAccess.objects.get(name="cat")
        comm = RegOrgUnit.objects.get(id=1)
        max_length = comm._meta.get_field('org_unit_id_vis').max_length
        self.assertEqual(max_length, 12)

