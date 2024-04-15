from django.db import models
from datetime import datetime
# Create your models here.
#Will create database table here

def __str__(self):
	return self.title


class Faq(models.Model):
	quest=models.TextField()

	def __str__(self):
		return self.quest
     



class Contact(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=12)
    description=models.TextField()

    def __str__(self):
        return self.email
    

class Enrollment(models.Model):        
    FullName=models.CharField(max_length=25)
    Email=models.EmailField()
    Gender=models.CharField(max_length=25)
    PhoneNumber=models.CharField(max_length=12)
    DOB=models.CharField(max_length=50)
    SelectMembershipplan=models.CharField(max_length=200)
    SelectTrainer=models.CharField(max_length=55)
    Reference=models.CharField(max_length=55)
    Address=models.TextField()
    paymentStatus=models.CharField(max_length=55,blank=True,null=True)
    Price=models.IntegerField(max_length=55,blank=True,null=True)
    DueDate=models.DateTimeField(blank=True,null=True)
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True,)

    def __str__(self):
        return self.FullName

class Trainer(models.Model):
    name=models.CharField(max_length=55)
    gender=models.CharField(max_length=25)
    phone=models.CharField(max_length=25)
    salary=models.IntegerField(max_length=25)
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return self.name

class MembershipPlan(models.Model):
    plan=models.CharField(max_length=185)
    price=models.IntegerField(max_length=55)

    def __int__(self):
        return self.id
    


from django.contrib.auth.models import User

class Notify(models.Model):
	notify_detail=models.TextField()
	read_by_user=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
	read_by_trainer=models.ForeignKey(Trainer, on_delete=models.CASCADE,null=True,blank=True)

	def __str__(self):
		return str(self.notify_detail)
     

class NotifUserStatus(models.Model):
	notif=models.ForeignKey(Notify, on_delete=models.CASCADE)
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	status=models.BooleanField(default=False)

	class Meta:
		verbose_name_plural='Notification Status'
     




class Equipments(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='equipments')
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __int__(self):
        return self.id


class Attendance(models.Model):
    Selectdate=models.DateTimeField(auto_now_add=True)
    phonenumber=models.CharField(max_length=15)
    Login=models.CharField(max_length=200)
    Logout=models.CharField(max_length=200)
    SelectWorkout=models.CharField(max_length=200)
    TrainedBy=models.CharField(max_length=200)
    def __int__(self):
        return self.id
    

class Service(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='service', null=True, blank=True)
    description = models.TextField()
    fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    starts_from = models.DateTimeField(default=datetime.now) 
    ends_on = models.DateTimeField(default=datetime.max)  # Default value
    timeStamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
   


class Appointment(models.Model):
    full_name = models.CharField(max_length=150)
    user_phone = models.CharField(max_length=20)
    trainer=models.CharField(max_length=200, default='')
    date_and_time = models.DateTimeField()
    duration = models.DurationField()
    appointment_type = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    notes = models.TextField(blank=True)
    
   
from django.contrib.auth.models import User

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipments, on_delete=models.CASCADE)
    method = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for {self.equipment.title} by {self.user.username}"

