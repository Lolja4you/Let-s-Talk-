from django.db import models

class PageHit(models.Model):
    url = models.CharField(unique=True, max_length=2000)
    viewArticle = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.url
    
class IpUser(models.Model):
    ip = models.CharField(max_length=256)

    def __str__(self):
        return self.ip
    