"""TweetsAnnotationTool URL Configuration

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
from Tool import views

urlpatterns = [
    path('', views.index),
    path('test', views.test),
    path('annotate', views.annotate),
    path('delete_tweet/<int:tweet_id>', views.delete_tweet),
    path('delete_tweet_and_annotate/<int:tweet_id>', views.delete_tweet_and_annotate),
    path('annotate_tweet', views.annotate_tweet),
    path('export_json', views.export_json),
    path('upload_tweets_from_csv', views.upload_tweets_from_csv),
    path('admin/', admin.site.urls),
]
