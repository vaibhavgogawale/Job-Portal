from django.db import models

# Create your models here.


class ITjobs(models.Model):

    company_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    experience = models.FloatField()
    packege = models.FloatField()
    location = models.CharField(max_length=255)
    qualification = models.CharField(max_length=255)
    no_of_jobs = models.IntegerField()
    resume = models.FileField(upload_to='files', default="00")


    def __str__(self):
        return f"{self.company_name}"



class MechJobs(models.Model):
    pass