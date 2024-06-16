from django.test import TestCase
from .models import SupplierRecord

# Create your tests here.

# TESTING 

class SupplierRecordTestCase(TestCase):
    def setUp(self):
        SupplierRecord.objects.create(name = "james", email="dave@gmail.com", phone_number="0976564411", address="10, napast close")

    def test_for_supplier(self):
        name = SupplierRecord.objects.get(name="james")
        print(name)
        self.assertEqual(name.name, 'james')
        self.assertEqual(name.email, "dave@gmail.com")
        self.assertEqual(name.phone_number, "0976564411")
        self.assertEqual(name.address, "10, napast close")
