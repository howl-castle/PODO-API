"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import *
from rest_framework import routers, serializers, viewsets, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from apiapp import views


schema_view = get_schema_view(
    openapi.Info(
        title='podo api',
        default_version='v4',
        description='api for podo ios',
        terms_of_service='https://www.ourapp.com/policies/terms/',
        contact=openapi.Contact(email=''),
        license=openapi.License(name='...'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [

    path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),

    path('signup/',views.signup, name = 'signup'),
    path('addwallet/',views.integrate_phantom_wallet, name = 'integrate_phantom_wallet'),
    path('signin/',views.signin, name = 'signin'),
    path('signout/',views.signout, name = 'signout'),

#    path('article_list',views.article_list, name = 'article_list'),
#    path('article_detail/<int:pk>',views.article_detail, name = 'article_detail'),
#    path('article_create',views.article_create, name = 'article_create'),
#    path('article_update/<int:pk>',views.article_update, name = 'article_update'),
#    path('article_delete/<int:pk>',views.article_delete, name = 'article_delete'),
#    path('question_list',views.question_list, name = 'question_list'),
#    path('question_detail/<int:pk>',views.question_detail, name = 'question_detail'),
#    path('question_create',views.question_create, name = 'question_create'),
#    path('question_update/<int:pk>',views.question_update, name = 'question_update'),
#    path('question_delete/<int:pk>',views.question_delete, name = 'question_delete'),
#    path('comment_list',views.comment_list, name = 'comment_list'),
#    path('comment_detail/<int:pk>',views.comment_detail, name = 'comment_detail'),
#    path('comment_create',views.comment_create, name = 'comment_create'),
#    path('comment_update/<int:pk>',views.comment_update, name = 'comment_update'),
#    path('comment_delete/<int:pk>',views.comment_delete, name = 'comment_delete'),
#    path('<int:pk>/answer_detail',views.answer_detail, name = 'answer_detail'),
#    path('<int:pk>/answer_create',views.answer_create, name = 'answer_create'),
#    path('<int:pk>/answer_update',views.answer_update, name = 'answer_update'),
#    path('<int:pk>/answer_delete',views.answer_delete, name = 'answer_delete'),
#    path('<int:pk>/answer_choose',views.answer_choose, name='answer_choose'),
    
]

