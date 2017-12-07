from __future__ import unicode_literals

from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
import re, md5
import binascii
from os import urandom

class UserManager(models.Manager):
    def user_validation(self, postData):
        print postData
        errors = []

        if len(postData['first_name']) < 1:
            errors.append("First name field cannot be blank.")

        if len(postData['last_name']) < 1:
            errors.append("Last name field cannot be blank.")

        if len(postData['email']) < 1:
            errors.append("Email field cannot be blank.")
        if not EMAIL_REGEX.match(postData['email']):
            errors.append("Email address is not valid.")
        try:
            User.objects.get(email = postData['email'])
            errors.append("Email has already been registered")
        except:
            pass

        if len(postData['password']) < 4:
            errors.append("Password must be at least 4 charaters.")
        if len(postData['confirm']) < 1:
            errors.append("Please confirm your password")
        if not postData["password"] == postData["confirm"]:
            errors.append("Your passwords do not match")


        response_to_views = {}
        if errors:
            response_to_views['status'] = False
            response_to_views['error'] = errors
        else:
            salt = binascii.b2a_hex(urandom(15))
            hashed_password = md5.new(postData['password']+salt).hexdigest()
            user = self.create(first_name=postData['first_name'], last_name=postData['last_name'], email=postData['email'], password=postData['password'], salt=salt)
            response_to_views['status'] = True
            response_to_views['user'] = user
            print response_to_views
            print user
            print hashed_password
        return response_to_views

    def login_validation(self, postData):
        print postData
        login_errors = []

        try:
            User.objects.get(email=postData["email"])
            print ("$"*20 + "EMAIL SAME" + "$"*20)
        except:
            login_errors.append("Email incorrect")
        try:
            User.objects.get(email=postData["email"]).password == postData["password"]
            print ('%'*20 + "PASSWORD MATCH")
        except:
            login_errors.append("Password incorrect")

        response_to_views = {}
        if login_errors:
            response_to_views['status'] = False
            response_to_views['errors'] = login_errors
        else:
            user = User.objects.get(email=postData["email"])
            response_to_views['status'] = True
            response_to_views['user'] = user
        print response_to_views
        return response_to_views

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    salt = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
