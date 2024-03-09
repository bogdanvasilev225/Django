from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend


class EmailAuthBackend(BaseBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        user_madel = get_user_model()
        try:
            user = user_madel.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except (user_madel.DoesNotExist, user_madel.MultipleObjectsReturned):
            return None

    def get_user(self, user_id):
        user_madel = get_user_model()
        try:
            return user_madel.objects.get(pk=user_id)
        except user_madel.DoesNotExist:
            return None
