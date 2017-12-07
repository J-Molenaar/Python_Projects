from __future__ import unicode_literals

from django.db import models

class CourseManager(models.Manager):
    def validate_course(self, postData):
        print postData
        errors = []
        if len(postData['name']) < 0:
            errors.append('Course name must be at least 1 character.')
        if len(postData['description']) < 0:
            errors.append('Description name must be at least 1 character.')

        response_to_views = {}
        if errors:
            response_to_views['status'] = False
            response_to_views['error'] = errors
        else:
            course = self.create(name=postData['name'], description=postData['description'])
            response_to_views['status'] = True
            response_to_views['course'] = course
        return response_to_views

    def delete_course(self, id):
        self.filter(id=id).delete()

class Course(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()
