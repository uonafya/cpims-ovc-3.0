from django.test import TestCase
from cpovc_forms.models import OVCBursary


class TestModels(TestCase):
    def setUp(self):
        OVCBursary.objects.create(bursary_type="OVC Bursary", amount=100)
    def test_bursary_type(self):
        field_label = OVCBursary._meta.get_field('bursary_type').verbose_name
        self.assertEqual(field_label, 'bursary_type')
