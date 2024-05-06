from django.urls import path
from .views import MyModelListView

urlpatterns = [
    path('test/', MyModelListView.as_view(), name='list-view'),
]
