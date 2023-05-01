from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name=models.CharField(max_length=50,verbose_name="Your Name ")
    phone=models.BigIntegerField(verbose_name="Phone No.")
    email=models.EmailField(max_length=50,verbose_name="Email") 
    address=models.TextField(verbose_name="My address")
   
    class Meta:
        db_table="stdent_dtl"

    def __str__(self):
        return self.name
    