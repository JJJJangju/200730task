from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=10)
    image = models.ImageField(upload_to='images/')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.title

    def summary(self):
        return self.body
    #제목, 본문, 이미지
