from turtle import title
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# Users Project
class Project(models.Model):
    owner = models.ForeignKey(User ,on_delete=models.CASCADE 
                              ,related_name='Users')
    title = models.CharField(max_length=100 , null=True ,blank=True)
    description = models.TextField(null=True ,blank=True)
    source = models.URLField(null=True ,blank=True)
    demo = models.URLField(null=True ,blank=True)

    def __str__(self) :
        return self.title
    

# Contact 
class Contact(models.Model):
    instagram = models.URLField()
    github = models.URLField()
    linkedin = models.URLField()
    gmail = models.URLField()
    # https://mail.google.com/mail/u/0/?view=cm&fs=1&to=yash.avasekar.1999@gmail.com

    def __str__(self):
        return self.instagram

    