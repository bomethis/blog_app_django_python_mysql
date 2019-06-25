from django.db import models
from datetime import datetime


class Posts(models.Model):
    title = models.CharField(max_length=200)
    body = models. TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    # re-name post objects in admin area to output title of post"
    def __str__(self):
        return self.title

    # correct double ss in Postss in admin area:
    class Meta:
        verbose_name_plural = 'Posts'
