from django.db import models

class Student(models.Model):
        name            = models.CharField(max_length=200)
        slug            = models.SlugField(unique=True)
        module          = models.ForeignKey('Module')
        stnumber        = models.IntegerField(max_length=8)
        notes           = models.TextField(blank=True)
        image           = models.ImageField(upload_to="images/studenticons/") # help_text="50x180px image")

        def __unicode__(self):
                return self.name

class Module(models.Model):
        name            = models.CharField(max_length=200)
        slug            = models.SlugField(unique=True)
        notes           = models.TextField(blank=True)

        def __unicode__(self):
                return self.name
