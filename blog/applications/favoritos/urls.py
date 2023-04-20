#
from django.urls import path

from . import views

app_name = "favoritos_app"

urlpatterns = [
    path(
        'perfil/', 
        views.UserPageView.as_view(),
        name='perfil',
    ),
    path(
        'add_favoritos/<pk>/', 
        views.AddFavoritesView.as_view(),
        name='add_favoritos',
    ),
    path(
        'del_favoritos/<pk>/', 
        views.FavoritesDeleteView.as_view(),
        name='del_favoritos',
    ),
]