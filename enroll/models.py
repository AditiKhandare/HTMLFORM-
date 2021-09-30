from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile_no = models.CharField(max_length=200)
    # profile_pic = models.IntegerField(null=True)
    #image = models.ImageField(upload_to = 'media')
    
    class Meta:
        db_table = 'enroll_user'

    # def __str__(self):
    #     return self.name