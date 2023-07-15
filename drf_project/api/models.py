from django.db import models

# Create your models here.


class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200,blank=False)
    location = models.CharField(max_length=100)
    about = models.TextField()
    type = models.CharField(max_length=200,choices=(('it','IT'), ('brac','Brac'),('housing','Housing')))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    
    def __str__(self):
        return self.name+'--'+self.location


class Employee(models.Model):
    name = models.CharField(max_length=200,blank=False)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    about = models.TextField()
    position = models.CharField(max_length=200,choices=(('soft_dev','SoftWare Engineer'), 
                                                        ('Support','Dupno Support'),('employee','Employee')))
    company = models.ForeignKey(Company,on_delete=models.CASCADE)

    
    
    
    def __str__(self):
        return self.name+" -- "+f"{self.position}"
