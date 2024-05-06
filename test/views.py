from django.views.generic import ListView
from .models import MyModel

class MyModelListView(ListView):
    model = MyModel
    template_name = 'test/model_list.html' 
    context_object_name = 'object_list'  
