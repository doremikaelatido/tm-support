from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20,unique=True)

    def __str__(self):
        return self.username

    def __unicode__(self):
        return self.username

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    projectname = models.CharField(max_length=20,unique=True)

    def __str__(self):
        return self.projectname
    
    def __unicode__(self):
        return self.projectname

class WorkLog(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=1)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    hours_spent = models.FloatField()
