from django.test import  TestCase,Client
from django.urls import  reverse
import cpovc_reports.models as models
import json
class TestViews(TestCase):
     def setUp(self):
          self.client = Client()
          self.report_url = reverse('reports')
     def test_report_home_GET(self):
          response= self.client.get(self.report_url)
          self.assertEqual(response.status_code,200)
          self.assertTemplateUsed(response,'reports/reports_documents.html')
          