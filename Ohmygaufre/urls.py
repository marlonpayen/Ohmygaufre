"""Ohmygaufre URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from website import views
from Ohmygaufre.settings import MEDIA_URL
from Ohmygaufre.settings import MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('home', views.index, name='index'),
    path('messagesent', views.send_message, name='form')
] +static(MEDIA_URL, document_root=MEDIA_ROOT)

handler404 = "website.views.my_custom_page_not_found_view"
handler500 = "website.views.my_custom_error_view"
handler403 = "website.views.my_custom_permission_denied_view"
handler400 = "website.views.my_custom_bad_request_view"
