import json

from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import (HttpResponseRedirect, get_object_or_404,redirect, render)
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .forms import *
from .models import *


def parent_home(request):
    parent = get_object_or_404(Parent, admin=request.user)
    context = {
        'page_title': 'Parent Portal - ' + str(parent.admin.last_name),
      
    }
    return render(request, 'parent_template/home_content.html', context)

def parent_due(request):
    if request.method=='POST':
        try:
            stud = request.POST.get('student')
            parent = get_object_or_404(Parent, admin=request.user)
            student = Student.objects.all().filter(username=stud)
            print(student)
            field_name1 = 'student_fee'
            field_name2 = 'student_fee_paid'
            obj = Student.objects.filter(username=stud).first()
            field_value1 = getattr(obj, field_name1)
            field_value2 = getattr(obj, field_name2)
            tot = field_value1 - field_value2
        
        
        
        
        
            context = {
                'page_title': 'Parent Portal',
                'student' : student,
                'tot':tot
            }
            return render(request, 'parent_template/parent_due.html', context)
        except Exception as e:
            messages.error(request, "Admin not Updated Student Fee details " + str(e))
            return render(request, 'parent_template/parent_due.html')
    return render(request, 'parent_template/parent_due.html')