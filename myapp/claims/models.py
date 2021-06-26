from django.db import models
import time


def get_upload_filename(instance, filename):
    return "uploaded_files/%s_%s" %(str(time.time()).replace('.','_'), filename)

class Claim(models.Model):

    loss_choice = (
    ("Own Damage", "Own Damage"),
    ("Knock for Knock", "Knock for Knock"),
    ("Windscreen Damage", "Windscreen Damage"),
    ("Theft", "Theft"),
    )
    options = ( 
    ("Yes", "Yes"),
    ("No", "No"),
    )

    claim_options = (
         ("In Progress", "In Progress"),
         ("Accepted", "Accepted"),
    )


    Name = models.CharField(max_length = 200)
    Email = models.EmailField()
    Mobile_No = models.CharField(max_length = 200)

    Vehicle_Year_Make = models.CharField(max_length = 200)
    Vehicle_Model = models.CharField(max_length = 200)
    Vehicle_No = models.CharField(max_length = 200)

    Date_and_time_of_accident = models.DateTimeField()
    Location = models.CharField(max_length = 200)
    Type_of_Loss = models.CharField(max_length=100,choices=loss_choice)
    Desrciption_of_Loss = models.TextField()
    Police_report_Lodged = models.CharField(max_length=5,choices=options)
    Anybody_Injured = models.CharField(max_length=5,choices=options)

    Photo = models.ImageField(upload_to=get_upload_filename)

    PDF_document_of_Insurance_Cover_Note = models.FileField(upload_to=get_upload_filename)

    Claim_Status = models.CharField(max_length=20,choices=claim_options)

    def __str__(self):
        return self.Name+' '+self.Vehicle_No


class User(models.Model):

    username = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)

    def __str__(self):
        return self.username

