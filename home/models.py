from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.EmailField(max_length=122)
    subject=models.CharField(max_length=180)
    message=models.TextField()
    date=models.DateField()

    def __str__(self) :
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add any additional fields you need for the user profile

    def __str__(self):
        return self.user.username

# class Registration(models.Model):
#     name=models.CharField(max_length=122)
#     email=models.EmailField(max_length=122)
#     contact=models.CharField(max_length=122)
#     password=models.CharField(max_length=122)
#     date=models.DateField()

#     def __str__(self) :
#         return self.name
# class Contact(models.Model):
#     name=models.CharField(max_length=122)
#     email=models.EmailField(max_length=122)
#     subject=models.CharField(max_length=180)
#     message=models.TextField()
#     date=models.DateField()

#     def __str__(self) :
#         return self.name

# class Blog(models.Model):
#         title = models.CharField(max_length=120)
#         author = models.CharField(max_length=120)
#         date_of_publishing = models.DateField(auto_now_add=True)
#         content = models.TextField()
#         def __str__(self):
#             return self.title
