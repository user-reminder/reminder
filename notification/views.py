from django.db.models import Q

from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from notification.models import Notification
from notification.serializers import NotificationCreateSerializer, \
    NotificationSerializer, NotificationUpdateSerializer
from notification.permissions import IsOwnerOrRecipient, IsOwner


class NotificationCreateView(generics.CreateAPIView):
    serializer_class = NotificationCreateSerializer
    permission_classes = (IsAuthenticated,)


class NotificationListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        if self.kwargs['username'] != self.request.user.username:
            return Response(status=status.HTTP_403_FORBIDDEN, data={
                "detail": "You do not have permission to perform this action."
            })

        notifications = Notification.objects.filter(
            Q(owner__username=self.kwargs['username']) |
            Q(recipients__username=self.kwargs['username'])
        ).distinct()
        serializer = NotificationSerializer(notifications, many=True)
        return Response({"data": serializer.data})


class NotificationDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()
    permission_classes = (IsAuthenticated, IsOwnerOrRecipient,)


class NotificationUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = NotificationUpdateSerializer
    queryset = Notification.objects.all()
    permission_classes = (IsAuthenticated, IsOwner,)
