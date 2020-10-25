"""foodtable URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path ,include
from foodconf.views import home ,admin_home
from doctors.views import profile_page ,loginpage
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
     path('profile/', profile_page, name='profile'),
      path('logindc/', loginpage, name='logindc'),
    # path('test/', api_test_view, name='api-test'),
    path('start/', admin_home, name='start'),
    # path('api-view', UnitsList.as_view(), name='api-view'),
     
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
