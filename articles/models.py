from django.db import models

# Create your models here.
class Article(models.Model):
    class Meta():
        db_table = 'articles'

    def __str__(self):
        return str(self.title)
    
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    