"""exhbn_project URL Configuration

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
from mainpage import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('allprofile', views.allprofile, name = 'allprofile'),
    path('detailprofile', views.detailprofile, name = 'detailprofile'),


    path('works', views.worksall, name = 'worksall'),
    path('works/<str:wtype>', views.works, name = 'works'),
    path('work_detail/<int:pk>', views.work_detail, name = 'work_detail'),
    path('work_detail2/<int:pk>', views.work_detail2, name = 'work_detail2'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
