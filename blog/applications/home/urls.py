#
from django.urls import path
from . import views

app_name = "home_app"

urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),  
    path('suscription/', views.SuscriberCreateView.as_view(), name='suscription'),  
    path('add_contact/', views.ContactCreateView.as_view(), name='add_contact'),  
]