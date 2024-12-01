from django.db import models
import uuid
# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50,null=True)
    url = models.URLField(max_length=500,null=True)
    image = models.CharField(max_length=50)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=100,default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    
    def __str__(self):
        return str(self.title)
    
    class Meta:
        ordering = ['-created']