from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=32, default='title')
    content = models.TextField(null=True)
    pub_data = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Users(models.Model):
    usname = models.CharField(max_length=8, null=False)
    solotext = models.TextField(max_length=28, null=True)
    upage = models.TimeField(auto_now=True)

    def __str__(self):
        return self.usname
