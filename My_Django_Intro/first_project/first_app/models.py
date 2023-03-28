from django.db import models

# Create your models here.
class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)
    
    def __str__(self) -> str:
        return self.top_name
    
class Website(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)
    
    def __str__(self) -> str:
        return self.name
    
    
class AccessRecord(models.Model):
    name = models.ForeignKey(Website,on_delete=models.CASCADE)
    date = models.DateTimeField()
    
    def __str__(self) -> str:
        return str(self.date)    
        