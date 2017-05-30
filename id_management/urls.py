from django.conf.urls import url
from id_management import views

urlpatterns = [
    url(r'^$', views.IndexView, name='index'),
    url(r'^register/$', views.registerView, name='register'),
    url(r'^login/$', views.loginView, name='login'),
    url(r'^logout/$', views.logoutView, name='logout'),
    url(r'^profile/$', views.profileView, name='profule'),
]
