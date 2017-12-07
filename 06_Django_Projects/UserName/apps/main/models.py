from __future__ import unicode_literals

from django.db import models


class UserManager(models.Manager):
    def user_validation(self, postData):
        print postData
        errors = []

        if len(postData['user_name']) < 1:
            errors.append("User name field cannot be blank.")
        if len(postData['user_name']) < 8 or len(postData['user_name']) > 20:
            errors.append("User name must be greater 8 characters and less than 20 charaters.")
        try:
            User.objects.get(user_name = postData['user_name'])
            errors.append("User name has already been registered")
        except:
            pass

        response_to_views = {}
        if errors:
            response_to_views['status'] = False
            response_to_views['error'] = errors
        else:
            user = self.create(user_name=postData['user_name'])
            response_to_views['status'] = True
            response_to_views['user'] = user
        print response_to_views
        return response_to_views

class User(models.Model):
    user_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()
