"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import url,include
# from django.contrib.auth import views
# from blog import views
from django.contrib.auth import views as auth_views
# import views from auth library like login and logout


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'',include('blog.urls')),
    url(r'^accounts/login/$',auth_views.LoginView.as_view(),name='login'),
    url(r'^accounts/logout/$',auth_views.LogoutView.as_view(),name='logout',kwargs={'next_page':'/'}),
    # url(r'^self',views.self,name='ip'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns=[
        path('__debug__/',include(debug_toolbar.urls))
    ] + urlpatterns
