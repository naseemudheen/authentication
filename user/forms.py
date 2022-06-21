from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from user.models import MyUser


class UserRegistrationForm(UserCreationForm):
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control pwstrength','data-indicator':'pwindicator'},))
	password2 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'},))

	class Meta:
		model = MyUser
		fields = ('username','email')
		widgets= {
			'username' : forms.EmailInput(attrs={'class': 'required form-control',}),
		}
	# def clean_email(self):
	# 	email = self.cleaned_data['email'].lower()
	# 	try:
	# 		user = MyUser.objects.exclude(pk=self.instance.pk).get(email=email)
	# 	except MyUser.DoesNotExist:
	# 		return email
	# 	raise forms.ValidationError('Email "%s" is already in use.' % user)

	# def clean_username(self):
	# 	username = self.cleaned_data['username']
	# 	try:
	# 		user = MyUser.objects.exclude(pk=self.instance.pk).get(username=username)
	# 	except MyUser.DoesNotExist:
	# 		return username
	# 	raise forms.ValidationError('Username "%s" is already in use.' % username)
	
	# def clean_password1(self):
	# 	password1 = self.cleaned_data['password1']
	# 	if len(password1) < 4:
	# 		raise forms.ValidationError("password is too short")
	# 	return password1


class UserAuthenticationForm(forms.ModelForm):

	password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'required form-control',}))
	username = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'class':'form-control'},))
	class Meta:
		model = MyUser
		fields = ('username', 'password')

	# def clean(self):
	# 	if self.is_valid():
	# 		username = self.cleaned_data['username']
	# 		password = self.cleaned_data['password']
	# 		if not authenticate(username=username, password=password):
	# 			raise forms.ValidationError("Invalid login")


class UserUpdateForm(forms.ModelForm):

	class Meta:
		model = MyUser
		fields = ('email', 'username', )

	# def clean_email(self):
	# 	email = self.cleaned_data['email'].lower()
	# 	try:
	# 		user = MyUser.objects.exclude(pk=self.instance.pk).get(email=email)
	# 	except MyUser.DoesNotExist:
	# 		return email
	# 	raise forms.ValidationError('Email "%s" is already in use.' % user)

	# def clean_username(self):
	# 	username = self.cleaned_data['username']
	# 	try:
	# 		user = MyUser.objects.exclude(pk=self.instance.pk).get(username=username)
	# 	except MyUser.DoesNotExist:
	# 		return username
	# 	raise forms.ValidationError('Username "%s" is already in use.' % username)


