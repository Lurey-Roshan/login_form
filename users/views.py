from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from users.forms import ExtendedUserCreationForm, UserProfileForm



# Create your views here.
def index(request):
	if request.user.is_authenticate:
		username=request.user.username
	else:
		username="Not logged in"

	context={
		'username':'username'
	}
	return render(request,'index.html', context)

def profile(request):
	return render(request, 'profile.html')


def register(request):
	form=ExtendedUserCreationForm()
	profile_form=UserProfileForm()
	if request.method=='POST':
		form=ExtendedUserCreationForm(request.POST)
		profile_form=UserProfileForm(request.POST)
		if form.is_valid() and profile_form.is_valid():
			user=form.save()
			profile=profile_form.save()
			profile.user= user
			profile.save()
			#form.save()
			username=form.cleaned_data.get('username')
			password=form.cleaned_data.get('password1')
			user=authenticate(username=username, password=password)
			login(request, user)

			return redirect('index')

		else:
			form=ExtendedUserCreationForm()

			profile_form=UserProfileForm()

	context={
		'form':form,
		'profile_form':profile_form,

	}
	return render(request,'register.html' , context)