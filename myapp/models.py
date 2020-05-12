from django.db import models

class TextInput(models.Model):
    innerinput = models.CharField(max_length=50)

    def __str__(self):
        return self.innerinput
    
class TextOutpout(models.Model):
    theoutput = models.TextField()