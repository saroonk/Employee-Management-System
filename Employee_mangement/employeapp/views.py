from django.shortcuts import render,redirect,HttpResponse
from employeapp.models import User,Employee
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


def adminhome(request):
    return render(request,'adminhome.html')

def logins(request):
    if request.method=='POST':
        USERNAME=request.POST['uname']
        PASSWORD=request.POST['upass']
        userpass= authenticate(request,username=USERNAME,password=PASSWORD)
        if userpass is not None and userpass.is_superuser==1:
            return redirect(adminhome)
        elif userpass is not None and userpass.is_active==1 and userpass.usertype=='USER':
            login(request, userpass)
            request.session['user_id']=userpass.id
            return redirect(userhome)
        else:
            return HttpResponse("<script>alert('invalid');window.location.href=''</script>")
    else:
        return render(request,'login.html')



def logout(request):
    return redirect(logins)


def user_reg(request):
    if request.method=='POST':
        img=request.FILES.get('img')
        fn=request.POST['fname']
        ln=request.POST['lname']
        age=request.POST['age']
        em=request.POST['email']
        ph=request.POST['phone']
        add=request.POST['address']
        un=request.POST['un']
        ps=request.POST['ps']
        x=User.objects.create_user(first_name=fn,last_name=ln,password=ps,username=un,email=em,usertype='USER',is_active=False)
        x.save()
        y=Employee.objects.create(emp_id=x,profilepic=img,age=age,phoneno=ph,address=add)
        y.save()
        return render(request,"login.html")
    else:

        return render(request,'userregistration.html')
    
@login_required
def userhome(request):
    # user1=request.session.get('user_id')
    # userdet=Employee.objects.get(emp_id_id=user1)
    return render(request,'userhome.html')

def userprofile(request):
    users=request.session.get('user_id')
    use=Employee.objects.get(emp_id_id=users)
    return render(request,'userprofile.html',{'view':use})



def userupdate(request):
    users=request.session.get('user_id')
    use=Employee.objects.get(emp_id_id=users)
    uid=use.emp_id_id
    us=User.objects.get(id=uid)
    if request.method=="POST":
        age=request.POST.get('age')
        address=request.POST.get('address')
        fnme=request.POST.get('fname')
        lnme=request.POST.get('lname')
        em=request.POST.get('email')
        ph=request.POST.get('phone')
        pic=request.FILES.get('pic')
        print('//////////////////////////////////////////////////////////////////////',pic)
        print('//////////////////////////////////////////////////////////////////////zzzzzzzzzzzzzzzzzzzzzzzzz',age)
        use.address=address
        use.age=age
        use.phoneno=ph
        us.first_name=fnme
        us.last_name=lnme
        us.email=em
        use.profilepic=pic
        use.save()
        us.save()
        return redirect(userprofile)
    else:
    
        return render(request,'userupdate.html',{'view':use})


def view_employee(request):
    x=Employee.objects.all()
    return render(request,'viewemployee.html',{'x1':x})


def approverequest(request,aid):
    p=Employee.objects.get(id=aid)
    p.emp_id.is_active=True
    p.emp_id.save()
    return redirect(view_employee)

    
def disaproverequest(request,aid):
    p=Employee.objects.get(id=aid)
    p.emp_id.is_active=False
    p.emp_id.save()
    return redirect(view_employee)

def deleterequest(request,did):
    x=Employee.objects.get(id=did)
    uid=x.emp_id.id
    x.delete()
    User.objects.filter(id=uid).delete()
    return redirect(view_employee)






