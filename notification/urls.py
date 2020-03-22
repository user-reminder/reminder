from django.urls import path

from notification.views import NotificationCreateView, NotificationDetailView, \
    NotificationUpdateView


urlpatterns = [
    path('notification/create/', NotificationCreateView.as_view()),
    path('notification/detail/<int:pk>/', NotificationDetailView.as_view()),
    path('notification/update/<int:pk>/', NotificationUpdateView.as_view()),
]
