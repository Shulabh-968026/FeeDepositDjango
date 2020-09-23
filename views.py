
from django.shortcuts import render
import os
import time
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.utils.datetime_safe import time
from .models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail, BadHeaderError


# Create your views here.
#login from user
def login(request):
    if request.method=='POST':
        e1=request.POST['email']
        pas=request.POST['password']
        try:
            obj=log.objects.get(email=e1, password=pas)
            ut=obj.usertype
            request.session['usertype']=ut
            request.session['email'] =e1
            if ut=='admin':
                return HttpResponseRedirect('/adminhome/')
        except:
            pass
            return render(request,'log3.html',{'data':"You are not Admin"})
    else:
        return render(request,'log3.html')
#login by accountant
def logacc(request):
    if request.method=='POST':
        e1=request.POST['email']
        pas=request.POST['password']
        try:
            obj=log.objects.get(email=e1, password=pas)
            ut=obj.usertype
            request.session['usertype']=ut
            request.session['email'] =e1
            if ut=='accountant':
                return HttpResponseRedirect('/accountanthome/')
        except:
            pass
            return render(request, 'log3.html', {'data1': "you are not Accountant"})
    else:
        return render(request,'log3.html')
#logout function
def logout(request):
    try:
        del request.session['email']
        del request.session['usertype']
    except:
        pass
    return HttpResponseRedirect('/login/')
#admin main function call
def adminhome(request):
    if request.session.has_key('usertype'):
        ut=request.session['usertype']
        if ut=='admin':
            return render(request,'adminfee.html')
        else:
            return render(request,'error.html')
    else:
         return render (request,'error.html')
#accountant main function
def accountanthome(request):
    if request.session.has_key ('usertype'):
        ut = request.session['usertype']
        if ut =="accountant":
            return render(request, 'accountant.html')
        else:
            return render(request, 'error.html')
    else:
        return render(request, 'error.html')
#added accountant function 
def addaccountant(request):
    if request.session.has_key('usertype'):
        ut=request.session['usertype']
        if ut=='admin':
            if request.method=="POST":
                name = request.POST['name']
                email = request.POST['email']
                password = request.POST['password']
                address = request.POST['address']
                contact = request.POST['contact']
                obj=log()
                obj1=accountant()
                obj.email=email
                obj.password=password
                obj.usertype="accountant"
                obj.save()
                obj1.name=name
                obj1.email=email
                obj1.password=password
                obj1.address=address
                obj1.contact=contact
                obj1.save()
                return render(request,'addaccountant.html',{'data':"accountant successfully saved"})
            else:
                return render(request,'addaccountant.html')
        else:
            return render(request,'error.html')
    else:
        return render(request,'error.html')
#view all accountant function
 def viewaccountant(request):
    if request.session.has_key('usertype'):
        ut=request.session['usertype']
        if ut=='admin':
            obj=accountant.objects.all()
            return render(request,'viewaccountant.html',{'data':obj})
        else:
            return render(request, 'error.html')
    else:
        return render(request,'error.html')
#find accountant by email id for edit
def editaccountant(request):
    if request.session.has_key('usertype'):
        ut = request.session['usertype']
        if ut == 'admin':
            if request.method=="POST":
                email=request.POST['E1']
                obj=accountant.objects.filter(email=email)
                return render(request,'editacc.html',{'data':obj})
            else:
                return render(request, 'error.html')
        else:
            return render(request,'error.html')
    else:
        return render(request, 'error.html')
#edit accountant 
def editacc(request):
    if request.session.has_key('usertype'):
        ut=request.session['usertype']
        if ut=='admin':
            if request.method=="POST":
                name = request.POST['name']
                email = request.POST['email']
                password = request.POST['password']
                address = request.POST['address']
                contact = request.POST['contact']
                obj1=accountant.objects.get(email=email)
                obj1.name=name
                obj1.email=email
                obj1.password=password
                obj1.address=address
                obj1.contact=contact
                obj1.save()
                return HttpResponse("<h1>Accounant Successfully Updated</h1>")
            else:
                return render(request, 'error.html')
        else:
            return render(request, 'error.html')
    else:
        return render(request, 'error.html')
#delete accounant find by email id
def deleteaccountant(request):
    if request.session.has_key('usertype'):
        ut = request.session['usertype']
        if ut == 'admin':
            if request.method=="POST":
                email=request.POST['D1']
                obj=accountant.objects.filter(email=email)
                return render(request,'delacc.html',{'data':obj})
            else:
                return render(request, 'error.html')
        else:
            return render(request,'error.html')
    else:
        return render(request, 'error.html')
#accountant delete 
def delaccountant(request):
    if request.session.has_key('usertype'):
        ut=request.session['usertype']
        if ut=='admin':
            if request.method=="POST":
                name = request.POST['name']
                email = request.POST['email']
                password = request.POST['password']
                address = request.POST['address']
                contact = request.POST['contact']
                usertype="accountant"
                obj1=accountant.objects.filter(email=email)
                obj=log.objects.filter(email=email)
                obj.email=email
                obj.password=password
                obj.usertype=usertype
                obj.delete()
                obj1.name=name
                obj1.email=email
                obj1.password=password
                obj1.address=address
                obj1.contact=contact
                obj1.delete()
                return HttpResponse("<h1>Accounant Successfully Deleted</h1>")
            else:
                return render(request, 'error.html')
        else:
            return render(request, 'error.html')
    else:
        return render(request, 'error.html')
#add student function for fee deposit 
def addstudent(request):
    if request.session.has_key('usertype'):
        ut=request.session['usertype']
        if ut=='accountant':
            if request.method=="POST":
                name = request.POST['name']
                email = request.POST['email']
                collegeid = request.POST['collegeid']
                sex = request.POST['sex']
                course = request.POST['course']
                branch = request.POST['branch']
                sem = request.POST['semester']
                fee = request.POST['fee']
                paid = request.POST['paid']
                due = request.POST['due']
                address = request.POST['address']
                contact = request.POST['contact']
                date = request.POST['date']
                obj=student()
                obj.name=name
                obj.email=email
                obj.collegeid=collegeid
                obj.sex=sex
                obj.course=course
                obj.branch=branch
                obj.semester=sem
                obj.fee=fee
                obj.paid=paid
                obj.due=due
                obj.address=address
                obj.contact=contact
                obj.date=date
                obj.save()
                return render(request,'feesubmisson.html',{'data':"Student data successfully saved"})
            else:
                return render(request,'feesubmisson.html')
        else:
            return render(request,'error.html')
    else:
        return render(request,'error.html')
#edit student find by college id
def editstudent(request):
    if request.session.has_key('usertype'):
        ut = request.session['usertype']
        if ut == 'accountant':
            if request.method == "POST":
                collegeid = request.POST['E1']
                obj = student.objects.filter(collegeid=collegeid)
                return render(request, 'editstu.html', {'data': obj})
            else:
                return render(request, 'error.html')
        else:
            return render(request, 'error.html')
    else:
        return render(request, 'error.html')
#edit student details
def editstud(request):
    if request.session.has_key('usertype'):
        ut = request.session['usertype']
        if ut == 'accountant':
            if request.method == "POST":
                name = request.POST['name']
                email = request.POST['email']
                cid = request.POST['cid']
                sex = request.POST['sex']
                course = request.POST['course']
                branch = request.POST['branch']
                sem = request.POST['semester']
                fee = request.POST['fee']
                paid = request.POST['paid']
                due = request.POST['due']
                address = request.POST['address']
                contact = request.POST['contact']
                date = request.POST['date']
                obj = student.objects.get(email=email)
                obj.name = name
                obj.email = email
                obj.collegeid=cid
                obj.sex = sex
                obj.course = course
                obj.branch = branch
                obj.semester = sem
                obj.fee = fee
                obj.paid = paid
                obj.due = due
                obj.address = address
                obj.contact = contact
                obj.date = date
                obj.save()
                return HttpResponse("<h1>Student data successfully Updated</h1>")
            else:
                return render(request, 'error.html')
        else:
            return render(request, 'error.html')
    else:
        return render(request, 'error.html')
#student find by college id for delete
def deletestudent(request):
    if request.session.has_key('usertype'):
        ut = request.session['usertype']
        if ut == 'accountant':
            if request.method=="POST":
                collegeid=request.POST['D1']
                obj=student.objects.filter(collegeid=collegeid)
                return render(request,'delstu.html',{'data':obj})
            else:
                return render(request, 'error.html')
        else:
            return render(request,'error.html')
    else:
        return render(request, 'error.html')
 #delete student
def delstudent(request):
    if request.session.has_key('usertype'):
        ut=request.session['usertype']
        if ut=='accountant':
            if request.method=="POST":
                name = request.POST['name']
                email = request.POST['email']
                collegeid = request.POST['collegeid']
                sex = request.POST['sex']
                course = request.POST['course']
                branch = request.POST['branch']
                sem = request.POST['semester']
                fee = request.POST['fee']
                paid = request.POST['paid']
                due = request.POST['due']
                address = request.POST['address']
                contact = request.POST['contact']
                date = request.POST['date']
                obj = student.objects.filter(email=email)
                obj.name = name
                obj.email = email
                obj.collegeid = collegeid
                obj.sex = sex
                obj.course = course
                obj.branch = branch
                obj.semester = sem
                obj.fee = fee
                obj.paid = paid
                obj.due = due
                obj.address = address
                obj.contact = contact
                obj.date = date
                obj.delete()
                return HttpResponse("<h1>Student data successfully Deleted</h1>")
            else:
                return render(request, 'error.html')
        else:
            return render(request, 'error.html')
    else:
        return render(request, 'error.html')
#view all students
def viewstudent(request):
    if request.session.has_key('usertype'):
        ut=request.session['usertype']
        if ut=='accountant':
            obj=student.objects.all()
            return render(request,'viewstudent.html',{'data':obj})
        else:
            return render(request, 'error.html')
    else:
        return render(request,'error.html')
#view all due fee student function
def duefee(request):
    if request.session.has_key('usertype'):
        ut=request.session['usertype']
        if ut=='accountant':
            obj= student.objects.all().exclude(due=0)
            return render(request,'viewstudent.html',{'data':obj})
            #else:
             #   return HttpResponseRedirect("<h1>No student found </h1>")
        else:
            return render(request, 'error.html')
    else:
        return render(request,'error.html')

#search student by college id function
def searchstudent(request):
    if request.session.has_key('usertype'):
        ut=request.session['usertype']
        if ut=='accountant':
            if request.method=='POST':
                try:
                    collegeid=request.POST["rollno"]
                    obj=student.objects.filter(collegeid=collegeid)
                    return render(request,'viewstudent.html',{'data':obj})
                except:
                    pass
                    return render(request,'serachstudent.html',{'data1':"Incorrect College Id"})
            else:
                return render(request,'serachstudent.html')
        else:
            return render(request, 'error.html')
    else:
        return render(request, 'error.html')
#send fee recepit to student email function
def send_email(request):
    subject = "Student fee Receipt"
    message = """<html><body><table><tr><th>Name</th><th>Email</th><th>College Id</th>
          <th>Sex</th>
          <th>Course</th>
          <th>Branch</th>
          <th>Semester</th>
          <th>Fee</th>
          <th>Paid Fee</th>
          <th>Due Fee</th>
          <th>Address</th>
          <th>Contact</th>
          <th>Date</th>
          <th>Edit</th>
          <th>Delete</th>
        </tr> </table></body></html>"""
    from_email = "sender@gmail.com"
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['receiver@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        #return HttpResponseRedirect('/contact/thanks/')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')
