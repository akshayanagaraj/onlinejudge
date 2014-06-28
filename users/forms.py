from django import forms

class RegisterForm(forms.Form):
	Choices = (('M','M'),
				('F','F'))
	name = forms.CharField(max_length=100)
	gender = forms.ChoiceField(choices=Choices)
	email = forms.EmailField()
	reg_no = forms.CharField(max_length=22)
	password =forms.CharField(max_length=32,widget=forms.PasswordInput())
	confpassword =forms.CharField(max_length=32,widget=forms.PasswordInput())
        
class LoginForm(forms.Form):
        username = forms.CharField(max_length=22)
        password = forms.CharField(max_length=32,widget=forms.PasswordInput())

class ProfileForm(forms.Form):
	Choices = (('M','M'),
				('F','F'))
	name = forms.CharField(max_length=100)
	gender = forms.ChoiceField(choices=Choices)
	oldpassword = forms.CharField(max_length=32,widget=forms.PasswordInput(),required=False)
	password =forms.CharField(max_length=32,widget=forms.PasswordInput(),required=False)
	confpassword =forms.CharField(max_length=32,widget=forms.PasswordInput(),required=False)




    
