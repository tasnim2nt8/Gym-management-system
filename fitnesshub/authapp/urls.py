
from django.urls import path
from authapp import views
urlpatterns = [
    path('',views.Home,name="Home"),
    path('faq/', views.faq, name='faq'),
    path('add_enquiry/', views.Add_Enquiry, name='add_enquiry'),
    path('enquiry/', views.View_Enquiry, name='enquiry'),
    path('delete_enquiry(?p<int:pid>)', views.Delete_Enquiry, name='delete_enquiry'),
    path('signup',views.signup,name="signup"),
    path('login',views.handlelogin,name="handlelogin"),
    path('logout',views.handleLogout,name="handleLogout"),
    path('contact',views.contact,name="contact"),
    path('join',views.enroll,name="enroll"),
    path('profile',views.profile,name="profile"),
    path('notifications/', views.view_notifications, name='view_notifications'),
    path('notifs/', views.view_notifications, name='view_notifications_shortcut'),
    path('equipments',views.equipments,name="equipments"),
    path('attendance',views.attendance,name="attendance"),
    path('service',views.service,name="service"),
    path('appointment',views.appointment,name="appointment"),
    path('payment/', views.payment_page, name='payment_page'),
    


    
]