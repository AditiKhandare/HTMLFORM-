from django.shortcuts import render
from .forms import StudentRegistration
# from .models import Image
# from .forms import StudentRegistration
from .models import User
# Create your views here.

#This function add new items and show all items
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            ad = fm.cleaned_data['address']
            em = fm.cleaned_data['email']
            ph = fm.cleaned_data['mobile_no']
            #img = fm.cleaned_data['image']
            reg = User(name=nm, address=ad, email=em, mobile_no=ph) 
            #image=img
            
            
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form':fm, 'stu':stud})

#This function will Delete
#def delete_data(request, id):
    #if request.method == 'POST':
        #pi = User.object.get(pk=id)
        #pi.delete()
        #return HttpResponseRedirect('/')
