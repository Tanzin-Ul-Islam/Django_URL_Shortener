from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
app_name = 'shortner'
urlpatterns = [
    path('', views.index, name="index"),
    path('link/<pk>', views.link, name="link"),
]