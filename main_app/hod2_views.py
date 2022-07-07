import json

from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import (HttpResponseRedirect, get_object_or_404,redirect, render)
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .forms import *
from .models import *


def hod2_home(request):
    hod = get_object_or_404(hod2, admin=request.user)
    context = {
        'page_title': 'HOD Panel - ' + str(hod.admin.last_name) + ' (' + str(hod.course) + ')',
      
    }
    return render(request, 'hod2_template/home_content.html', context)
def manage_staff_hod2(request):
    allStaff = CustomUser.objects.filter(user_type=2)
    print(allStaff)
    context = {
        'allStaff': allStaff,
        'page_title': 'View Staff'
    }
    return render(request, "hod2_template/manage_staff_hod2.html", context)

def hod2_take_attendance(request):
    allStaff = CustomUser.objects.filter(user_type=2)
    #.filter(cl=cl)
    aform=AttendanceStaffForm()
    if request.method=='POST':
        form=AttendanceStaffForm(request.POST)
        if form.is_valid():
            Attendances=request.POST.getlist('present_status')
            date=form.cleaned_data['date']
            for i in range(len(Attendances)):
                AttendanceModel=AttendanceStaff()
                #AttendanceModel.cl=cl
                AttendanceModel.date=date
                AttendanceModel.present_status=Attendances[i]
                #AttendanceModel.course=allStaff[i].course
                AttendanceModel.save()
            return redirect('hod2_take_attendance')
        else:
            print('form invalid')
    return render(request,'hod2_template/hod2_take_attendance.html',{'staffs':allStaff,'aform':aform})


# def hod2_view_attendance(request):
#     form=AskDateForm()
#     if request.method=='POST':
#         form=AskDateForm(request.POST)
#         if form.is_valid():
#             date=form.cleaned_data['date']
#             attendancedata=AttendanceStaff.objects.all().filter(date=date,cl=cl)
#            # studentdata=models.StudentExtra.objects.all().filter(cl=cl)
#             mylist=zip(attendancedata)
#             return render(request,'hod2_template/hod2_view_dateask.html',{'mylist':mylist,'date':date})
#         else:
#             print('form invalid')
#     return render(request,'hod2_template/hod2_take_attendance.html',{'form':form})
def hod2_view_attendance(request):
    form=AskDateForm()
    if request.method=='POST':
        form=AskDateForm(request.POST)
        if form.is_valid():
            print("formok")
            date=form.cleaned_data['date']
            attendancedata=AttendanceStaff.objects.all().filter(date=date)
            studentdata=CustomUser.objects.filter(user_type=2)
            print(studentdata)
            print(attendancedata)
            mylist = zip(studentdata, attendancedata)
            context = {
            'mylist': mylist,
            'date':date,
                }
            return render(request,'hod2_template/hod2_view_attendance_page.html',context)
        else:
            print('form invalid')
    return render(request,'hod2_template/hod2_view_dateask.html',{'form':form})

def hod2_searchdept(request):
    if request.method =="POST":
        data = request.POST
        dept = request.POST.get('departement')
        j = str(dept)
        print(j)
        #course = Staff.objects.filter(course__name__startswith=j)
        print("ok")
    allStaff = CustomUser.objects.filter(user_type=2)
    staff = Staff.objects.filter(course_id=1)
    print(staff)
    #.filter(cl=cl)
    aform=AttendanceStaffForm()
    if request.method=='POST':
        form=AttendanceStaffForm(request.POST)
        if form.is_valid():
            Attendances=request.POST.getlist('present_status')
            date=form.cleaned_data['date']
            for i in range(len(Attendances)):
                AttendanceModel=AttendanceStaff()
                #AttendanceModel.cl=cl
                AttendanceModel.date=date
                AttendanceModel.present_status=Attendances[i]
                #AttendanceModel.course=allStaff[i].course
                AttendanceModel.save()
            return redirect('hod2_take_attendance')
        else:
            print('form invalid')
    return render(request,'hod2_template/hod2_take_attendance.html',{'staffs':allStaff,'aform':aform})
        
