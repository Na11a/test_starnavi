from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    liked = models.ManyToManyField(User, blank=True, related_name='likes')
    author = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="Author",related_name='posts')
    title = models.CharField(max_length=100,db_index=True,verbose_name="Title")
    body = models.TextField(max_length=500,verbose_name="Text")
    created = models.DateTimeField(auto_now=True,null=True)
    def __str__(self):
        return '{}'.format(self.title)
    def num_likes(self):
        return self.liked.all().count()

   
    
    class Meta:
        ordering = ('-created',)

    @property
    def total_likes(self):
        return self.likes.count()


LIKE_CHOICES = (
    ('Like', 'Unlike'),
)

class Like(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, max_length=8)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user}-{self.post}-{self.value}"
    