from django.db import models

# Create your models here.

#this corresponds to a single story, with headline, summary, and publication date
class story(models.Model):

    headline = models.CharField(max_length=50)
    story = models.CharField(max_length=500)
    time = models.CharField(max_length=50)

    def __str__(self):
        return self.headline + "\t" + self.time + "\n" + self.story

