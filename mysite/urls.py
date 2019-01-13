"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path
from django.views.generic import RedirectView
from django.conf.urls import include
from django.conf.urls.i18n import i18n_patterns
from projects import views
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()
urlpatterns = [
    path('admin/', admin.site.urls),
    # url('ckeditor/', include('ckeditor_uploader.urls')),
    path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path('', views.home, name="index"),
    path('mainpage/', views.mainpage, name="mainpage"),
]
urlpatterns += i18n_patterns(
    path('bio/', views.bio, name="bio"),
    path('jobs/', views.jobs, name="jobs"),
    path('en/jobs/', views.jobs, name="en_jobs"),
    path('contact/', views.contact, name="contact"),
    path('job/<int:index>/', views.category, name="category"),
    path('job/all/', views.all_projects, name="all_projects"),
    path('project/<int:pk>/', views.project, name="project"),
    prefix_default_language=False,

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
