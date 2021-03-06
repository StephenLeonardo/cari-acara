"""cariacara URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', include('event.urls')),
    path('admin/', admin.site.urls),
    path('account/', include('account.urls', namespace='account')),
    path('login_redirect/', views.LoginRedirectPage.as_view(), name='login_redirect'),
    path('logout_redirect/', views.LogoutRedirectPage.as_view(), name='logout_redirect'),
    path('events/', include('event.urls')),
]

urlpatterns  += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
