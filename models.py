from django.db import models

# Create your models here.

class Post(models.Model):
    
    
    slug = models.SlugField()
    image= models.ImageField( upload_to='corn')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:

        ordering= ('-created_at',)
    
    def __str__(self):
        return self.body