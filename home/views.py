from django.shortcuts import render,redirect,reverse
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
from django.http import HttpResponse
from django.http import HttpResponseRedirect

def index(request):
    # if 'login_status' in request.COOKIES and 'username' in request.COOKIES:
    #     context={
    #     'username':request.COOKIES['username'],
    #     'login_status':request.COOKIES.get('login_status'),
    #     }
    #     response=render(request,"index.html",context)
    # if not request.user.is_authenticated:
    #     return redirect("/login")
    return render(request,"index.html")


def main(request):
    if 'login_status' in request.COOKIES and 'username' in request.COOKIES:
        context={
            'username':request.COOKIES['username'],
            'login_status':request.COOKIES.get('login_status'),
        }
    # if request.user.is_authenticated:
    return render(request,"main.html",context)
    # return redirect("/login")

def aboutus(request):
    if 'login_status' in request.COOKIES and 'username' in request.COOKIES:
        context={
            'username':request.COOKIES['username'],
            'login_status':request.COOKIES.get('login_status'),
        }
    # if request.user.is_anonymous:
    #     return redirect("/login")
    return render(request,'aboutus.html',context)

def internship_portal(request):
    return render(request,'internship_portal_user.html')

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
        context={
            'username':un,
            'login_status':True,
        }


        response=render(request,'index.html',context)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'login.html')
        else:
            response.set_cookie('username',un)
            response.set_cookie('login_status',True)
            return response

    return render(request,'login.html')

def logoutUser(request):
    response=HttpResponseRedirect(reverse('login'))
    response.delete_cookie('username')
    response.delete_cookie('login_status')
    logout(request)
    return response

fn=''
ln=''
pd=''
el=''
cn=''
gd=''
# User Register
def register(request):
    # global un,fn,ln,pd,el,cn,gd
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

        c="insert into user(username,first_name,last_name,email,gender,phone,password) values('{}','{}','{}','{}','{}','{}','{}')".format(un,fn,ln,el,gd,cn,pd)
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
    return render(request,'internship_portal.html')

a1=''
b1=''
d1=''
query=''
f2=''
l2=''
c2=''
g2=''
e2=''
p2=''
i2=''
# l1=()
id3=''
jb3=''
sd3=''
def company_login(request):
    global a1,b1,d1,results,f2,l2,c2,g2,e2,p2,i2,jobs,job,job1,id3,jb3,sd3,l1
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



        query="select id,job_title,start_date from add_job where company_name='{}'"
        cursor.execute(query.format(c2))
        jobs =tuple(cursor.fetchall())
        print(jobs)
        for job in jobs:
            new=list(job)
            if new not in l1:
                l1.append(new)
        # jobn=jobs


        e1="select * from startups where username='{}' and password1='{}'"
        cursor.execute(e1.format(a1,b1))
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'company_login.html')
        else:
            return redirect('company_homepage')

    return render(request,'company_login.html')
l1=[]
# print(l1)

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
    # for key,value in d1.items():
    #     if key=="username":
    #         a1=value
    return render(request,'company_homepage.html',{'username': a1, 'company': c2,'firstname':f2,'lastname':l2,'email':e2,'phone':p2,'gender':g2,'img':i2})
    # return render(request,'company_homepage.html')


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


        k="insert into add_job (job_title,start_date,end_date,experience,salary,skills,company_location,job_description,company_name) values('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(aj1,aj2,aj3,aj4,aj5,aj6,aj7,aj8,c2)
        cursor.execute(k)
        n.commit()
        query="select id,job_title,start_date from add_job where company_name='{}'"
        cursor.execute(query.format(c2))
        jobs =tuple(cursor.fetchall())
        print(jobs)
        for job in jobs:
            new=list(job)
            if new not in l1:
                l1.append(new)

        return render(request, 'add_job.html')
        # return render(request, "company_login.html")
    return render(request, 'add_job.html')

def job_list(request):
    # l1=list[l1]
    # list_of_lists = [list(inner_tuple) for inner_tuple in l1]
    # jobs=[list(job) for job in l1]
    print(l1)
    # print(jobs)
    return render(request, "job_list.html",{'jobs':l1})
    # return render(request, "job_list.html", {'jobs':jobs})

a5=''
b5=''
d5=''
query=''
f5=''
l5=''
c5=''
g5=''
e5=''
p5=''
i5=''
t5=''
k5=''
def user_login(request):
    global a5,b5,d5,results,f5,l5,c5,g5,e5,p5,i5,t5,k5,list2
    if request.method=="POST":
        t5=sql.connect(host="localhost",user="root",password="Vedu@3105",database='psf')
        cursor=t5.cursor()
        d5=request.POST
        for key,value in d5.items():
            if key=="username":
                a5=value
            if key=="password":
                b5=value
            # if key=="status":
            #     f1=value
        query="select first_name,last_name,email,phone,gender,image from interns where username='{}'"
        cursor.execute(query.format(a5))
        results =tuple(cursor.fetchall())
        for row in results:
            f5 = row[0]
            l5 = row[1]
            c5 = row[2]
            e5 = row[3]
            p5 = row[4]
            g5 = row[5]

        query="select company_name,job_title,salary,company_location,start_date from add_job"
        cursor.execute(query.format(c2))
        jobs =tuple(cursor.fetchall())
        print(jobs)
        for job in jobs:
            new=list(job)
            if new not in list2:
                list2.append(new)
        # jobn=jobs


        k5="select * from startups where username='{}' and password1='{}'"
        cursor.execute(k5.format(a5,b5))
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'user_login.html')
        else:
            return redirect('user_homepage')
    return render(request,'user_login.html')
list2=[]
list3=[]
a4=''
b4=''
c4=''
d4=''
e4=''
f4=''
g4=''
h4=''
i4=''
k4=''
def user_signup(request):
    global a4,b4,c4,d4,e4,f4,g4,h4,i4,k4
    if request.method == "POST":
        n=sql.connect(host="localhost",user="root",password="Vedu@3105",database='psf')
        cursor=n.cursor()
        x=request.POST
        for key,value in x.items():
            if key=="username":
                a4=value
            if key=="email":
                b4=value

            if key=="first_name":
                c4=value
            if key=="last_name":
                d4=value
            if key=="password1":
                e4=value
            if key=="password2":
                f4=value
            if key=="phone":
                g4=value
            if key=="gender":
                h4=value
            if key=="image":
                i4=value
            # if key=="status":
            #     k=value


        k4="insert into interns (username,email,first_name,last_name,password1,password2,phone,gender,image) values('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(a4,b4,c4,d4,e4,f4,g4,h4,i4)
        cursor.execute(k4)
        n.commit()
        return redirect('user_login')
    return render(request,'signup.html')


def user_homepage(request):
    return render(request,'user_homepage.html',{'username': a5, 'firstname':f5,'lastname':l5,'email':c5,'phone':e5,'gender':p5,'img':g5})

def job_apply(request):
    return render(request,'job_apply.html')


def all_jobs(request):
    # print(jobs)
    global t5,list3
    t5=sql.connect(host="localhost",user="root",password="Vedu@3105",database='psf')
    cursor=t5.cursor()
    query="select id from interns where username='{}'"
    cursor.execute(query.format(a5))
    data =tuple(cursor.fetchall())
    list3.append(data)
    list3=[]

    return render(request, "all_jobs.html",{'jobs':list2,'data':data})

def job_detail(request):
    return render(request,'job_detail.html')

def partners(request):
    return render(request,'partners.html')

def alumni(request):
    return render(request,'alumni.html')

def investor(request):
    return render(request,'investor.html')
