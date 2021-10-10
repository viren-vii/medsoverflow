from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import AutoField, IntegerField
from django.contrib.auth.models import User as authUser
# Create your models here.

class Tag(models.Model):
    tagName = models.CharField(max_length=30)

    def __str__(self):
        return self.tagName

class Role(models.Model):
    ROLES = (
        ('Student', 'Student'),
        ('Veteran', 'Veteran'),
        ('Expert', 'Expert'),
        ('Professional', 'Professional'),
    )
    roleName = models.CharField(max_length=50, choices=ROLES)
    def __str__(self):
        return self.roleName

class User(models.Model):
    user = models.OneToOneField(authUser, on_delete=models.CASCADE)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=50, null=True)
    email_id = models.EmailField(unique=True)
    country = models.CharField(max_length=50, null=True)
    rating = models.IntegerField(default=2)
    joined_on = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'username'
    roles = models.ManyToManyField(Role)

    def __str__(self):
        return self.user.username
        
class Question(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    votes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now=True)
    made_by = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    answerCount = models.IntegerField(default=0)
    def __str__(self):
        return self.title

class Answer(models.Model):
    description = models.CharField(max_length=1000)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    votes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now=True)
    made_by = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.made_by.first_name

class Comment(models.Model):
    description = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now=True)
    made_by = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.made_by.first_name
