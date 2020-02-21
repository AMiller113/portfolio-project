from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=150)
    publication_date = models.DateTimeField()
    blog_post_text = models.TextField()
    blog_image = models.ImageField(upload_to='images/')

