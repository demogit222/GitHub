
from django.conf.urls import url, include
from django.contrib import admin
from smsapp import views

urlpatterns = [

    url(r'^$', views.login_redirect, name='login_redirect'),
    url(r'^admin/', admin.site.urls),
    url(r'^dashboard/', include('dashboard.urls', namespace='dashboard')),
    url(r'^accounts/', include('accounts.urls', namespace= 'accounts')),
   

    ]
    


 