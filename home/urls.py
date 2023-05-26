from django.contrib import admin
from django.urls import include, path
from home import views
urlpatterns = [
    path("",views.loginUser,name='home'),
    path("index",views.index,name='index'),
    path("main",views.main,name='main'),
    path("aboutus",views.aboutus,name='aboutus'),
    path("partners",views.partners,name='partners'),
    path("alumni",views.alumni,name='alumni'),
    path("investor",views.investor,name='investor'),
    path("startup_expo",views.startup_expo,name='startup_expo'),
    path("contact",views.contact,name='contact'),
    path("login",views.loginUser,name='login'),
    path("logout",views.logoutUser,name='logout'),
    path('register',views.register,name="register"),
    path('agro_startups',views.agro_startups,name="agro_startups"),
    path('education_zone_startup',views.education_zone_startup,name="education_zone_startup"),
    path('green_startups',views.green_startups,name="green_startups"),
    path('health&lifestyle_startups',views.health_lifestyle_startups,name="health&lifestyle_startups"),
    path('innovation_zone_startup',views.innovation_zone_startup,name="innovation_zone_startup"),
    path('social_startups',views.social_startups,name="social_startups"),
    path('student_startups',views.student_startups,name="student_startups"),
    path('technical_startups',views.technical_startups,name="technical_startups"),
    path('internship_portal',views.internship_portal,name="internship_portal"),
    path('company_login/',views.company_login,name="company_login"),
    path('company_signup/',views.company_signup,name="company_signup"),
    path('company_homepage/',views.company_homepage,name="company_homepage"),
    path('add_job/',views.add_job,name="add_job"),

    path('user_login/',views.user_login,name="user_login"),
    path('user_signup/',views.user_signup,name="user_signup"),
    path('user_homepage/',views.user_homepage,name="user_homepage"),
    path('job_apply/',views.job_apply,name="job_apply"),
    path('all_jobs/',views.all_jobs,name="all_jobs"),
    path('job_detail/',views.job_detail,name="job_detail"),

    path('job_list/',views.job_list,name="job_list"),
    path('internship_portal_user',views.internship_portal_user,name="internship_portal_user")
]