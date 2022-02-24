from django.urls import path
from . import views

app_name = 'users'

    
urlpatterns = [
     path('create-account/', views.CreateAccountView.as_view(),name='createAccount'),
     path('<int:pk>/profile/', views.ProfileView.as_view(), name='profile'),
]
