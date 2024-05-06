from django.test import TestCase
from .forms import MyModelForm

class MyFormTestCase(TestCase):
    def test_valid_form(self):
        form_data = {'name': 'Test', 'age': 25}
        form = MyModelForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {'name': '', 'age': 25}  # Invalid because name is required
        form = MyModelForm(data=form_data)
        self.assertFalse(form.is_valid())
