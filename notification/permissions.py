from rest_framework import permissions


class IsOwnerOrRecipient(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user or request.user in obj.recipients.all()


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
