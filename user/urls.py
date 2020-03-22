from django.urls import path, include

from user.views import UserCreateView, UserListView, UserProfileView
from notification.views import NotificationListView


urlpatterns = [
    path('user/auth/', include('rest_framework.urls')),
    path('user/register/', UserCreateView.as_view()),
    path('all/', UserListView.as_view()),
    path('user/<str:username>/profile/', UserProfileView.as_view()),
    path('user/<str:username>/notifications/', NotificationListView.as_view())
]
