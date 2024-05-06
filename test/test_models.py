from django.test import TestCase
from .models import MyModel

class MyModelTestCase(TestCase):
    def setUp(self):
        self.obj = MyModel.objects.create(name="Test", age=25)

    def test_model_can_be_saved(self):
        self.assertEqual(MyModel.objects.count(), 1)

    def test_model_can_be_retrieved(self):
        obj = MyModel.objects.get(name="Test")
        self.assertEqual(obj.age, 25)

    def test_model_can_be_updated(self):
        self.obj.age = 30
        self.obj.save()
        obj = MyModel.objects.get(name="Test")
        self.assertEqual(obj.age, 30)

    def test_model_can_be_deleted(self):
        self.obj.delete()
        self.assertEqual(MyModel.objects.count(), 0)
