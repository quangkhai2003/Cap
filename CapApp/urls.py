from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('Vocabulary/', views.VocabularyApi),
]