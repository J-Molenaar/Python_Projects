from __future__ import unicode_literals

from django.db import models
from ..login.models import User

class SecretsManager(models.Manager):
    def secrets_validation(self, secret):
        errors = []

        if len(secret["secret"]) < 1:
            errors.append("Please tell me a secret!")

        response_to_views = {}
        if errors:
            response_to_views['status'] = False
            response_to_views['error'] = errors
        else:
            secret = self.create(content=secret["secret"], user=secret["user"])
            response_to_views['status'] = True
            response_to_views['secret'] = secret
        print ("@"*20)
        print response_to_views
        return response_to_views

class Secrets(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="all_secrets")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = SecretsManager()


class LikesManager(models.Manager):
    def add_like(self, data):
        user_object = User.objects.get(id= data['user_id'])
        secret_object = Secrets.objects.get(id=data['secret_id'])
        like = self.create(secret=secret_object, user=user_object)
        return like

class Likes(models.Model):
    secret = models.ForeignKey(Secrets, on_delete=models.CASCADE, related_name="all_likes")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="all_user_likes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = LikesManager()
