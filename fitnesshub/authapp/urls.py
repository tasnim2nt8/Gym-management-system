
from django.urls import path
from authapp import views
urlpatterns = [
    path('',views.Home,name="Home"),
    path('faq', views.faq, name='faq'),
    path('signup',views.signup,name="signup"),
    path('login',views.handlelogin,name="handlelogin"),
    path('logout',views.handleLogout,name="handleLogout"),
    path('contact',views.contact,name="contact"),
    path('join',views.enroll,name="enroll"),
    path('profile',views.profile,name="profile"),
    path('notifs',views.notifs,name='notifs'),
	path('get_notifs',views.get_notifs,name='get_notifs'),
	path('mark_read_notif',views.mark_read_notif,name='mark_read_notif'),
    path('equipments',views.equipments,name="equipments"),
    path('attendance',views.attendance,name="attendance"),
    path('service',views.service,name="service"),
    path('appointment',views.appointment,name="appointment"),
    path('payment/', views.payment_page, name='payment_page'),


    
]