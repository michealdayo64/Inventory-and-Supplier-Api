from django.test import TestCase
from .models import ItemsRecord

# Create your tests here.


# ............. TESTING FOR SYSTEM MODELS .................

class ItemRecordTestCase(TestCase):
    def setUp(self):
        ItemsRecord.objects.create(
            name="rice", description="It is great", price=23.0)

    def test_for_item_record(self):
        name = ItemsRecord.objects.get(name="rice")
        print(name)
        self.assertEqual(name.name, 'rice')
        self.assertEqual(name.price, 23.0)
