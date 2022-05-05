
# Create your tests here.
import unittest
from django.test import TestCase

class SinovuyoteenTest(unittest.TestCase):
    def test_sinivuyoteen(self):
        client = Client()
        response = client.get('/forms/new_sinovuyoteen_form/new/60/')
        self.assertEqual(response.status_code, 200)
        
        if(response.status_code == 200):
            print("success....")
        print("Failed....")
        
