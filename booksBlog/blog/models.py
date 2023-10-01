from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    date = models.DateField()
    content = models.TextField()

    def __str__(self):
        return f'{self.date} | {self.title}'

