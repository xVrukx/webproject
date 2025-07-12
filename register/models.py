from django.db import models

class Userinfo(models.Model):
    user_name = models.CharField(max_length=30, blank=True)
    user_email = models.EmailField(max_length=60, blank=True)
    user_number = models.CharField(max_length=30,blank=True)

    def __str__(self):
        return self.user_name