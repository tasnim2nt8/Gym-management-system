from django.contrib import admin
#from . import models

from authapp.models import Contact, MembershipPlan, Enrollment,Trainer, Equipments, Attendance,Service,Appointment,Payment,Faq, Notify, NotifUserStatus
# Register your models here.
admin.site.register(Contact)
admin.site.register(MembershipPlan)
admin.site.register(Enrollment)
admin.site.register(Trainer)
admin.site.register(Equipments)
admin.site.register(Attendance)
admin.site.register(Service)
admin.site.register(Appointment)
admin.site.register(Payment)
admin.site.register(Faq)
admin.site.register(Notify)
admin.site.register(NotifUserStatus)