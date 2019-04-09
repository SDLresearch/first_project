from django.conf.urls import url
from primer_app import views
from django.urls import path


urlpatterns = {
    path('', views.index_v1, name='index'),
}