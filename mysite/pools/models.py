from django.db import models

class Pools(models.Model):
    content = models.TextField()

    def __unicode__(self):
        return self.content
