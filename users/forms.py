from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import UserProfile
class ExtendedUserCreationForm(UserCreationForm):
	email=forms.EmailField(required=True)
	first_name=forms.CharField(max_length=15, required=True)
	last_name=forms.CharField(max_length=15, required=True)

	class Meta:
		model= User
		fields=('username', 'email','first_name', 'last_name','password1','password2')
		widgets={
			'username':forms.TextInput(attrs={'class':'form-control'}),
			'email':forms.EmailInput(attrs={'class':'form-control'}),
			'first_name':forms.TextInput(attrs={'class':'form-control'}),
			'last_name':forms.TextInput(attrs={'class':'form-control'}),
			'password1':forms.PasswordInput(attrs={'class':'form-control'}),
			'password2':forms.PasswordInput(attrs={'class':'form-control'}),

		}

	def save(self, commit=True):
		user=super().save(commit=False)
		user.email=self.cleaned_data['email']
		user.first_name=self.cleaned_data['first_name']
		user.last_name=self.cleaned_data['last_name']
		if commit:
			user.save()
		return  user

class UserProfileForm(forms.ModelForm):
	class Meta:
		model= UserProfile
		fields=['age', 'phone']
		widgets={
			'age':forms.TextInput(attrs={'class':'form-control'}),
			'phone':forms.TextInput(attrs={'class':'form-control'})
		}
