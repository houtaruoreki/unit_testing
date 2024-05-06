from django.test import TestCase, Client
from django.urls import reverse
from .models import MyModel

class MyViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.obj = MyModel.objects.create(name="Test", age=25)

    def test_list_view_status_code(self):
        response = self.client.get(reverse('list-view'))
        self.assertEqual(response.status_code, 200)

    def test_list_view_queryset(self):
        response = self.client.get(reverse('list-view'))
        self.assertEqual(response.context['object_list'].count(), 1)

    def test_list_view_template(self):
        response = self.client.get(reverse('list-view'))
        self.assertTemplateUsed(response, 'test/model_list.html')
        
