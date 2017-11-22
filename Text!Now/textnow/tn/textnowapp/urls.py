from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    
    url(r'^$', auth_views.login, {'template_name':'auth/login.html'} , name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'auth/logged_out.html'},name='logout'),
    url(r'^register/$',views.register),
    url(r'^home/$', views.home),
    url(r'^chat/(?P<u1>[0-9]+)/(?P<u2>[0-9]+)/$', views.chat),
    

]

if settings.DEBUG:
	urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)