from django.shortcuts import render
from django.template import loader, RequestContext
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login,logout,authenticate
from users.models import OjUser
from users.forms import RegisterForm, LoginForm,ProfileForm
from django.contrib.auth.decorators import login_required

def home(request):
	return render(request,'index.html')

def register(request):
	url='/register'
	sub='Register'
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			nm = form.cleaned_data['name']
			gender = form.cleaned_data['gender']
			reg_no = form.cleaned_data['reg_no']
			email = form.cleaned_data['email']
			pwd = form.cleaned_data['password']
			x = OjUser.objects.filter(username=email)
			if x:
				return HttpResponse('Email exists')
			l = OjUser.objects.create(
				username = reg_no,
				first_name = nm,
				email = email,
				gender = gender,
				reg_no = reg_no,
			)
			l.set_password(pwd)
			l.save()
			text="Registered Successfully"
			return render(request,"index.html",{'text':text})
		else:
			return render(request,'register.html',{'form':form,'url':url,'sub':sub})
	else:
		form = RegisterForm()
		return render(request,'register.html',{'form':form,'url':'/register','sub':'Register'})

def login_view(request):
    url = '/login'
    sub='Login'
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            em = form.cleaned_data['username']
            pwd = form.cleaned_data['password']
            user =  authenticate(
                username=em,
                password=pwd
            )
            if user is not None and user.is_active:
                u = OjUser.objects.get(username=user.username)
                """     if u.is_loggedin:
                    text = 'This user is already logged in'
                    return render(request,'register.html',{'sub':sub,'url':url,'form':LoginForm(),'text':text})"""

                login(request,user)
                u.is_loggedin = True
                u.save()
                return HttpResponseRedirect('/')
            else:
                text='Email and password do not match'
		return render(request,"register.html",{'form':LoginForm(),'text':text,'url':url,'sub':sub})
        else:

            return render(request,'register.html',{'url':url,'form':form,'sub':sub})
    else:
		   return render(request,'register.html',{'url':url,'form':LoginForm(),'sub':sub})
                
def logoff(request):
        u = OjUser.objects.get(username = request.user.username)
        u.is_loggedin = False
        u.save()
	logout(request)

	return HttpResponseRedirect('/')

@login_required(login_url='/login/')
def profile(request):
	u = OjUser.objects.get(username = request.user.username)
	return render(request,'profile.html',{'u':u,})

@login_required(login_url='/login/')
def edit_profile(request):
	url = '/editprofile'
	sub = 'Submit'
	u = OjUser.objects.get(username=request.user.username)
	if request.method=="POST":
		form = ProfileForm(request.POST)
		if form.is_valid():
			if u.check_password(form.cleaned_data['oldpassword']):
				u.set_password(form.cleaned_data['password'])
			else:
				text = 'Sorry. The old password did not match'
				return render(request,'message.html',{'text': text})
			u.first_name = form.cleaned_data['name']
			u.gender = form.cleaned_data['gender']
			u.reg_no = form.cleaned_data['reg_no']
			u.save()
			return HttpResponseRedirect('/profile')
		else:
			return render(request,'register.html',{'form':form,'url':url,'sub':sub})
	else:
		form = ProfileForm(initial={
			'name':u.first_name,'gender':u.gender,'reg_no':u.reg_no
			})
		return render(request,'register.html',{'form':form,'sub':sub,'url':url})


def htmltop(request):
	return render(request,'htmltop.html')
# Create your views here.
