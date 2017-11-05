from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    
    url(r'^$', auth_views.login, {'template_name':'auth/login.html'} , name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'auth/logged_out.html'},name='logout'),
    url(r'^register/$',views.register),
    url(r'^home/$', views.home),
    url(r'^admin/', admin.site.urls),

]
