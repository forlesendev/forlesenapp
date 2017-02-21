from django.conf.urls import url

from . import views

urlpatterns = [
            url(r'^$', views.display, name='display'),
            url(r'^text_input/$', views.text_input, name='text_input'),
            ]
