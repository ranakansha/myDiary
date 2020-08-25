from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    phone = models.IntegerField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name+'your query is '+self.subject
    
