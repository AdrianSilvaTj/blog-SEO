"""
Proyecto Curso Django
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls.static import static
# seo
from django.contrib.sitemaps.views import sitemap
from applications.home.sitemap import EntrySitemap, Sitemap

urlpatterns_main = [
    path('admin/', admin.site.urls),
    re_path('', include('applications.users.urls')),
    re_path('', include('applications.home.urls')),
    re_path('', include('applications.entrada.urls')),
    re_path('', include('applications.favoritos.urls')),
    # urls para ckeditor
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# ************ SEO ************************
# Objeto estructura sitemap que genera xml
sitemaps = {
    'site': Sitemap( # pagina principal
        [
            'home_app:index'
        ]
    ),
    'entradas' : EntrySitemap # pagina secundaria
}

urlpatterns_sitemap = [
    path(
        "sitemap.xml/",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
]

urlpatterns = urlpatterns_main + urlpatterns_sitemap
