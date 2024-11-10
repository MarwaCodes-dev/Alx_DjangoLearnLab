from django.urls import path
from .views import list_books
from .views import LibraryDetailView 
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('register/',SignUpView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('library/', LibraryDetailView.as_view(), name='library-detail'),
    path('list_books/', list_books, name='list_books'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]