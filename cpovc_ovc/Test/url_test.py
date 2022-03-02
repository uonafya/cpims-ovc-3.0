from django.test import  SimpleTestCase
from django.urls import reverse,resolve
import cpovc_ovc.views as views

class TestUrls(SimpleTestCase):
     def test_ovc_home_urls(self):
         url=reverse('ovc')
         self.assertEqual(resolve(url).func,views.ovc_home)
     def  test_ovc_register_urls(self):
         url = reverse('ovc_register')
         self.assertEqual(resolve(url).func, views.ovc_register)
     def  test_ovc_manage_urls(self):
         url = reverse('ovc_manage')
         self.assertEqual(resolve(url).func,views.ovc_manage)
     def  test_ovc_edit_urls(self):
         url = reverse('ovc_edit')
         self.assertEqual(resolve(url).func,views.ovc_edit)
     def  test_ovc_search_urls(self):
         url = reverse('ovc_search')
         self.assertEqual(resolve(url).func,views.ovc_search)
     def  test_ovc_view_urls(self):
         url = reverse('ovc_view')
         self.assertEqual(resolve(url).func,views.ovc_view)










