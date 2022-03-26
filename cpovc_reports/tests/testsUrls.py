from django.test import SimpleTestCase
from django.urls import reverse,resolve
import cpovc_reports.views as views

class testUrls(SimpleTestCase):
    def test_report_url(self):
        url = reverse('reports')
        self.assertEqual(resolve(url).func,views.reports_home)
    def  test_document_reports_urls(self):
         url = reverse('document_reports')
         self.assertEqual(resolve(url).func, views.reports_home)
    def  test_cpims_reports_urls(self):
         url = reverse('cpims_reports')
         self.assertEqual(resolve(url).func, views.reports_cpims)
    def  test_caseload_reports_urls(self):
         url = reverse('caseload_reports')
         self.assertEqual(resolve(url).func, views.reports_caseload)
    def  test_get_viral_load_report_urls(self):
         url = reverse('get_viral_load_report')
         self.assertEqual(resolve(url).func, views.get_viral_load_report)
    def  test_manage_reports_urls(self):
         url = reverse('manage_reports')
         self.assertEqual(resolve(url).func, views.manage_reports)
    def  test_manage_dashboard_urls(self):
         url = reverse('manage_dashboard')
         self.assertEqual(resolve(url).func, views.manage_dashboard)
    def  test_download_reports_urls(self):
         url = reverse('download_reports')
         self.assertEqual(resolve(url).func, views.reports_download)
    def  test_generate_reports_urls(self):
         url = reverse('generate_reports')
         self.assertEqual(resolve(url).func, views.reports_generate)
    def  test_pivot_reports_urls(self):
         url = reverse('pivot_reports')
         self.assertEqual(resolve(url).func, views.reports_pivot)
    def  test_pivot_rawdata_urls(self):
         url = reverse('pivot_rawdata')
         self.assertEqual(resolve(url).func, views.reports_rawdata)
    def  test_pivot_ovc_reports_urls(self):
         url = reverse('pivot_ovc_reports')
         self.assertEqual(resolve(url).func, views.reports_ovc_pivot)
    def  test_pivot_ovc_reports_mer_urls(self):
         url = reverse('pivot_ovc_reports_mer')
         self.assertEqual(resolve(url).func, views.reports_ovc_datim_mer_pivot)
    def  test_pivot_ovc_reports_mer23_urls(self):
         url = reverse('pivot_ovc_reports_mer23')
         self.assertEqual(resolve(url).func, views.reports_ovc_datim_mer23_pivot)
    def  test_pivot_ovc_reports_mer24_urls(self):
         url = reverse('pivot_ovc_reports_mer24')
         self.assertEqual(resolve(url).func, views.reports_ovc_datim_mer24_pivot)
    def  test_pivot_ovc_reports_mer25_urls(self):
         url = reverse('pivot_ovc_reports_mer25')
         self.assertEqual(resolve(url).func, views.reports_ovc_datim_mer25_pivot)
    def  test_pivot_ovc_pepfar_urls(self):
         url = reverse('pivot_ovc_pepfar')
         self.assertEqual(resolve(url).func, views.reports_ovc_pepfar)
    def  test_pivot_ovc_kpi_urls(self):
         url = reverse('pivot_ovc_kpi')
         self.assertEqual(resolve(url).func, views.reports_ovc_kpi)
    def  test_viral_load_urls(self):
         url = reverse('viral_load')
         self.assertEqual(resolve(url).func, views.viral_load)
    def  test_pivot_ovc_rawdata_urls(self):
         url = reverse('pivot_ovc_rawdata')
         self.assertEqual(resolve(url).func, views.reports_ovc_rawdata)
    def  test_ovc_download_urls(self):
         url = reverse('ovc_download')
         self.assertEqual(resolve(url).func, views.reports_ovc_download,)
    def  test_reports_ovc_urls(self):
         url = reverse('reports_ovc')
         self.assertEqual(resolve(url).func, views.reports_ovc)
    def  test_dashboard_details_urls(self):
         url = reverse('dashboard_details')
         self.assertEqual(resolve(url).func, views.dashboard_details)
    def  test_cluster_urls(self):
         url = reverse('cluster')
         self.assertEqual(resolve(url).func, views.cluster)
    def  test_reports_ovc_list_urls(self):
         url = reverse('reports_ovc_list')
         self.assertEqual(resolve(url).func, views.reports_ovc_list)
         
         
        
    