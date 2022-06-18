from rest_framework.permissions import BasePermission
from datetime import datetime, timedelta
from django.utils import timezone

class RegistedMoreThanAMinuteUser(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        user = request.user
        if not request.user or not request.user.is_authenticated:
            return False
        
        print(f"user join date : {user.join_date}")
        return bool(user.join_date < (timezone.now() - timedelta(minutes=3)))