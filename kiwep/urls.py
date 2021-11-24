"""kiwep URL Configuration
path('accounts/', include('django.contrib.auth.urls')),
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
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from accounts.views import MyLoginView

admin.autodiscover()

urlpatterns =[
    path('admin', admin.site.urls),
    path('i18n', include('django.conf.urls.i18n')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('backend.urls')),
    path('', include('content.urls')),
    path('message/', include('message.urls')),
    path('todo/', include('todo.urls')),
    path('login/', MyLoginView.as_view(), name='login'),
    path('api_project/content/', include('content.api_project.project_urls')),
    path('api_team/content/', include('content.api_team.team_urls')),
    # path('api_mission/content/', include('content.api_mission.mission_urls')),
    path('api_resource/content/', include('content.api_resource.resource_urls')),
]
if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
