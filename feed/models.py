from django.db import models
from register.models import CustomUser

class post(models.Model):
    author=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    photo=models.CharField(max_length=1000)
    caption=models.CharField(max_length=200)
    time=models.TimeField()
    like=models.BooleanField(default=False)
    date=models.DateField()
    def __str__(self):
        return self.author

class friends(models.Model):
    friend=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="buddies")
    email=models.EmailField()
    def __str__(self):
        return self.email
class block(models.Model):
    blocker=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    blocked=models.EmailField()
    def __str__(self) :
        return self.blocked   

class requests(models.Model):
    subject=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    sender=models.EmailField()
    accept=models.BooleanField()
    def __str__(self):
        return self.sender


class comments(models.Model):
    post=models.ForeignKey(post,on_delete=models.CASCADE) 
    author=models.EmailField(default="sanidhya738@gmail.com") 
    like=models.BooleanField(default=False)
    text=models.CharField(max_length=100)
    time=models.TimeField()
    date=models.DateField()
    def __str__(self):
        return self.author

