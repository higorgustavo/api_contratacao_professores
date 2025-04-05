from rest_framework.permissions import BasePermission


class ProfessorListPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method not in ("PUT", "DELETE"):
            return True
        return request.user and request.user.is_authenticated
