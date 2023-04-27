from django.db import models

# Create your models here.

class facultyinfo(models.Model):
	facultyid = models.IntegerField()
	facultyname = models.Charfield(max_length = 100)
	facultyage= models.IntegerField()
	researcharea = models.TextField()