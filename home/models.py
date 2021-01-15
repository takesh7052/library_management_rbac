from django.db import models

# Create your models here.
class adduser(models.Model):
    username = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    password = models.CharField(max_length=12)
    def _str_(self):
        return self.username

          
