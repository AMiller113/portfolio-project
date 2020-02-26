from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=150)
    publication_date = models.DateTimeField()
    blog_post_text = models.TextField()
    blog_image = models.ImageField(upload_to='images/')

    def summary(self):
        index = 0
        for i, char in enumerate(self.blog_post_text):
            if i > len(self.blog_post_text)//3 and char is '.' or char is '/r/n':
                index = i
                break
        return self.blog_post_text[:index] + '.......'

    def pub_date_alt(self):
        return self.publication_date.strftime('%b %e, %Y')

    def __str__(self):
        return self.title