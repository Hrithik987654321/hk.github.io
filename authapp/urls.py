from django.urls import path
from authapp import views

urlpatterns = [
    path('',views.Home,name="Home"),
    path("signup/",views.signup,name="signup"),
    path("signin/",views.signin,name="signin"),
    path("faq/",views.faq,name="faq"),
    path("subjects/",views.subjects,name="subjects"),
    path("contact/",views.contact,name="contact"),
    path("about/",views.about,name="about"),
    path('logout/', views.custom_logout, name='logout'),
    path('php/',views.php,name="php"),
    path('linux/',views.linux,name="linux"),
    path('statistics/',views.statistics,name="statistics"),
    path('daa/',views.daa,name="daa"),
    path('sase/',views.sase,name="sase"),
    
]
