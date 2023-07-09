from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.views.decorators.cache import cache_page

from user.views import RegisterUser, ProfileUser, confirm_code, DeleteUserView, ListUsersView, BlockUser

app_name = 'user'

urlpatterns = [
    path('register', RegisterUser.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('profile/', cache_page(60)(ProfileUser.as_view()), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('list_users/', ListUsersView.as_view(), name='list_users'),
    path('delete/<int:pk>/', DeleteUserView.as_view(), name='delete'),
    path('confirm_code/<str:email>/', confirm_code, name='confirm_code'),
    path('blocked_user/<int:pk>/', BlockUser.as_view(), name='blocked_user'),
]
