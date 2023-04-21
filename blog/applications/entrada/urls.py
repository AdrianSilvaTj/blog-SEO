#
from django.urls import path
from . import views

app_name = "entrada_app"

urlpatterns = [
    path('entrys/', views.EntryListView.as_view(), name='list_all'),  
    path('detail/<slug>', views.EntryDetailView.as_view(), name='detail'),  
]