from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    message = 'Вы не являетесь владельцем!'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True
        return False


# class IsPublic(BasePermission):
#     message = 'Привычка не является публичной'
#
#     def has_object_permission(self, request, view, obj):
#         return obj.is_public