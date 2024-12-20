from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('Vocabulary/', views.VocabularyApi),
    path('Vocabulary/<str:word>/', views.VocabularyByWordApi), 
    path('Vocabulary/<str:word>/AddExamples/', views.AddExampleByWordApi),
    path('Vocabulary/<str:word>/Examples/', views.ExamplesByWordApi),
    path('Vocabulary/Topic/<str:topic>/', views.get_vocabulary_by_topic),
    path('Vocabularies/AddMultiple/', views.add_multiple_vocabularies),
    path('Register/', views.RegisterView.as_view()),
    path('Login/', views.LoginView.as_view()),
    
]
