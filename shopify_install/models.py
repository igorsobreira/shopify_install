from django.db import models

class Token(models.Model):
    shop = models.CharField(max_length=1000)
    token = models.CharField(max_length=1000)

    def __str__(self):
        return self.token
