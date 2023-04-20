#
from django.urls import path
from . import views

app_name = "entrada_app"

urlpatterns = [
    path('entradas/', views.EntryListView.as_view(), name='list_all'),  
]