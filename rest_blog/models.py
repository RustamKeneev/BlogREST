from django.db import models

class Post(models.Model):
    """Модель для постов"""
    title = models.CharField(max_length=128, null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='posts_image/',null=True)
    date_added = models.DateTimeField(auto_created=True, null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """Модель для комментариев"""
    comment = models.TextField(null=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)
    post = models.ForeignKey(Post,on_delete=models.SET_NULL,null=True,related_name="comments")

    def __str__(self):
        return self.comment