from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
# Create your models here.


class Post(models.Model):
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title=models.CharField(max_length=256)
    text=models.TextField()
    created_date=models.DateTimeField(default=timezone.now())
    published_date=models.DateTimeField(null=True,blank=True)
    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.title