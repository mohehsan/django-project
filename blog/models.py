from django.db import models
from users.models import Users


# Create your models here.

class Comment(models.Model):
    text_comment = models.CharField(max_length=255, blank=True, null=True)
    photo = models.ForeignKey('Photos', on_delete=models.CASCADE)
    users = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.users} - {self.text_comment}'


# photo models
class Photos(models.Model):
    caption = models.CharField(max_length=200)
    users = models.ForeignKey(Users, on_delete=models.CASCADE)
    memes_photo = models.ImageField()
    upload = models.DateTimeField(auto_now_add=True)
    comments = models.ForeignKey('Comment', on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey('Categories', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.memes_photo}"


class Categories(models.Model):
    name = models.CharField(max_length=225, unique=True)
    category_image = models.ImageField(upload_to='category_img/')

    def __str__(self):
        return f"{self.id} . {self.name}"
