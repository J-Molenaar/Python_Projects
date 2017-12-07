from __future__ import unicode_literals

from django.db import models

class BookManager(models.Manager):
    def validate_book(self, postData):
        print postData
        errors =[]
        if len(postData['title']) < 0:
            errors.append('Title requires at least 1 character.')
        if len(postData['author']) < 0:
            errors.append('Author requires at least 1 character.')
        if len(postData['category']) < 0:
            errors.append('Category requires at least 1 character.')

        respone_to_views = {} #created an empty dictionary
        if errors:
            #failed validation
            #send message to views
            respone_to_views['status'] = False
            respone_to_views['error'] = errors
        else:
            book = self.create(title = postData['title'], author = postData['author'], category = postData['category'])
            respone_to_views['status'] = True
            respone_to_views['book'] = book

        return respone_to_views

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publish_date = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()
