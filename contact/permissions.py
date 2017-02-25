from rest_framework import permissions


class OnlyAllowAnyOneToSubmit(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == "create":
            return True
        elif view.action=="list" and request.user.is_superuser:
            return True
        return False