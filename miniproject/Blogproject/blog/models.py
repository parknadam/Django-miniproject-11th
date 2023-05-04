from django.db import models
from django.utils import timezone

# Create your models here.


class Blog(models.Model):
    title=models.CharField(max_length=200)
    date=models.DateTimeField('여행 일정 및 시간')
    body=models.TextField()

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:150]
    
class Comment(models.Model):
    post = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    username = models.CharField(max_length=20)
    comment_text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def approve(self):
        self.save()

    def __str__(self):
        return self.comment_text