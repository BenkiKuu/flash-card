from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from tinymce.models import HTMLField


# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'profiles/', null=True)
    email = models.TextField()
    user = models.OneToOneField(User,related_name='user')

    def __str__(self):
        return self.user.name

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()


class Flashcard (models.Model):
    subject = models.CharField(max_length = 60)
    content = HTMLField()
    pub_date = models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(upload_to = 'articles/')


@classmethod
    def search_by_title(cls,search_term):
        subject = cls.objects.filter(title__icontains=search_term)
        return subject
