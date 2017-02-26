from rest_framework import permissions
from rest_framework.compat import is_authenticated


class AllowSpecialUsersToCreateOnlyAdminUsersToList(permissions.BasePermission):
	def has_permission(self, request, view):
		if view.action == "create" and request.user and is_authenticated(request.user):
			return True
		elif view.action == "list" and request.user and request.user.is_superuser:
			return True
		return False