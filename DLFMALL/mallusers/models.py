from django.db import models

class userDetails(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(primary_key=True)
    mobile = models.IntegerField(unique=True)
    password = models.CharField(max_length=20)
    address = models.CharField(max_length=100)

membershipName = (
                  ("Silver","Silver"),
                  ("Gold","Gold"),
                  ("Platinum","Platinum")
                )

class membershipDetails(models.Model):
    membershipcategory = models.CharField(max_length=20,choices=membershipName)
    membershipID = models.AutoField(primary_key=True)
    email = models.ForeignKey(userDetails,on_delete=models.CASCADE)
    validity = models.DateField()

class eventdetails(models.Model):
    eventID = models.AutoField(primary_key=True)
    eventName = models.CharField(max_length=50,unique=True)
    eventDescription = models.CharField(max_length=100)
    eventDate = models.DateTimeField()
    eventVenue = models.CharField(max_length=50)

class registrationDetails(models.Model):
    registrationID = models.AutoField(primary_key=True)
    emailID = models.ForeignKey(eventdetails,on_delete=models.CASCADE)
    email = models.ForeignKey(userDetails,on_delete=models.CASCADE)