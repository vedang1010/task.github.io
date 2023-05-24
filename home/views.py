from django.shortcuts import render,redirect
from home.models import Contact
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login
import mysql.connector as sql
from django.db import connection

def index(request):
    # if not request.user.is_authenticated:
    #     return redirect("/login")
    return render(request,"index.html")
def login(request):
    # if not request.user.is_authenticated:
    #     return redirect("/login")
    return render(request,"login.html")

def main(request):
    # if request.user.is_authenticated:
    return render(request,"main.html")
    # return redirect("/login")

def aboutus(request):
    # if request.user.is_anonymous:
    #     return redirect("/login")
    return render(request,'aboutus.html')

def internship_portal(request):
    return render(request,'internship_portal.html')

def startup_expo(request):
    return render(request,'startup_expo.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')

        contact=Contact(name=name,email=email,subject=subject,message=message,date=datetime.today())
        contact.save()
    return render(request,'contact.html')

# em=''
pwd=''
un=''

def loginUser(request):
    global un,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",password="Vedu@3105",database='psf')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="username":
                un=value
            if key=="password":
                pwd=value

        c="select * from user where username='{}' and password='{}'".format(un,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'login.html')
        else:
            return redirect('/index')

    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')

fn=''
ln=''
pd=''
el=''
cn=''
gd=''
# User Register
def register(request):
    global un,fn,ln,pd,el,cn,gd
    if request.method == "POST":
        m=sql.connect(host="localhost",user="root",password="Vedu@3105",database='psf')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key==("first_name"):
                fn=value
            if key=="last_name":
                ln=value
            if key=="username":
                un=value
            if key=="password":
                pd=value
            if key=="email":
                el=value
            if key=="phone":
                cn=value
            if key=="gender":
                gd=value

        c="insert into user values('{}','{}','{}','{}','{}','{}','{}')".format(un,fn,ln,el,gd,cn,pd)
        cursor.execute(c)
        m.commit()
        # return render(request,'login.html')
        return redirect('login')

    return render(request, 'register.html')

def agro_startups(request):
    return render(request,'agro_startups.html')

def technical_startups(request):
    return render(request,'technical_startups.html')

def education_zone_startup(request):
    return render(request,'education_zone_startup.html')

def green_startups(request):
    return render(request,'green_startups.html')

def health_lifestyle_startups(request):
    return render(request,'health&lifestyle_startups.html')

def innovation_zone_startup(request):
    return render(request,'innovation_zone_startup.html')

def social_startups(request):
    return render(request,'social_startups.html')

def student_startups(request):
    return render(request,'student_startups.html')

def internship_portal_user(request):
    return render(request,'internship_portal_user.html')

a1=''
b1=''
d1=''
query=''
# results=''
# values=[]
f2=''
l2=''
c2=''
g2=''
e2=''
p2=''
i2=''
def company_login(request):
    global a1,b1,d1,results,f2,l2,c2,g2,e2,p2,i2
    if request.method=="POST":
        c1=sql.connect(host="localhost",user="root",password="Vedu@3105",database='psf')
        cursor=c1.cursor()
        d1=request.POST
        for key,value in d1.items():
            if key=="username":
                a1=value
            if key=="password":
                b1=value
            # if key=="status":
            #     f1=value
        query="select first_name,last_name,company_name,email,phone,gender,image from startups where username='{}'"
        cursor.execute(query.format(a1))
        results =tuple(cursor.fetchall())
        for row in results:
            f2 = row[0]
            l2 = row[1]
            c2 = row[2]
            e2 = row[3]
            p2 = row[4]
            g2 = row[5]
            i2 = row[6]
        e1="select * from startups where username='{}' and password1='{}'"
        cursor.execute(e1.format(a1,b1))
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'company_login.html')
        else:
            return redirect('/company_homepage')

    return render(request,'company_login.html')

a=''
b=''
c=''
d=''
e=''
f=''
g=''
h=''
i=''
j=''
# k=''
def company_signup(request):
    global a,b,c,d,e,f,g,h,i,j,k
    if request.method == "POST":
        n=sql.connect(host="localhost",user="root",password="Vedu@3105",database='psf')
        cursor=n.cursor()
        x=request.POST
        for key,value in x.items():
            if key=="username":
                a=value
            if key=="email":
                b=value
            if key=="company_name":
                c=value
            if key=="first_name":
                d=value
            if key=="last_name":
                e=value
            if key=="password1":
                f=value
            if key=="password2":
                g=value
            if key=="phone":
                h=value
            if key=="gender":
                i=value
            if key=="image":
                j=value
            # if key=="status":
            #     k=value


        k="insert into startups (username,email,company_name,first_name,last_name,password1,password2,phone,gender,image) values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(a,b,c,d,e,f,g,h,j,i)
        cursor.execute(k)
        n.commit()
        return redirect('company_login')
        # return render(request, "company_login.html")
    return render(request, 'company_signup.html')

def company_homepage(request):
    for key,value in d1.items():
        if key=="username":
            a1=value

    return render(request,'company_homepage.html',{'username': a1, 'company': c2,'firstname':f2,'lastname':l2,'email':e2,'phone':p2,'gender':g2,'img':i2})

aj1=''
aj2=''
aj3=''
aj4=''
aj5=''
aj6=''
aj7=''
aj8=''
def add_job(request):
    global aj1,aj2,aj3,aj4,aj5,aj6,aj7,aj8
    if request.method == "POST":
        n=sql.connect(host="localhost",user="root",password="Vedu@3105",database='psf')
        cursor=n.cursor()
        x=request.POST
        for key,value in x.items():
            if key=="job_title":
                aj1=value
            if key=="start_date":
                aj2=value
            if key=="end_date":
                aj3=value
            if key=="experience":
                aj4=value
            if key=="salary":
                aj5=value
            if key=="skills":
                aj6=value
            if key=="location":
                aj7=value
            if key=="description":
                aj8=value
            # if key=="gender":
            #     i=value
            # if key=="image":
            #     j=value
            # if key=="status":
            #     k=value


        k="insert into add_job (job_title,start_date,end_date,experience,salary,skills,company_location,job_description) values('{}','{}','{}','{}','{}','{}','{}','{}')".format(aj1,aj2,aj3,aj4,aj5,aj6,aj7,aj8)
        cursor.execute(k)
        n.commit()
        return render(request, 'add_job.html')
        # return render(request, "company_login.html")
    return render(request, 'add_job.html')

def all_jobs(request):
    jobs = Job.objects.all().order_by('-start_date')
    applicant = Applicant.objects.get(user=request.user)
    apply = Application.objects.filter(applicant=applicant)
    data = []
    for i in apply:
        data.append(i.job.id)
    return render(request, "all_jobs.html", {'jobs':jobs, 'data':data})

def job_list(request):
    # companies = Company.objects.get(user=request.user)
    # jobs = Job.objects.filter(company=companies)
    return render(request, "job_list.html")
    # return render(request, "job_list.html", {'jobs':jobs})
