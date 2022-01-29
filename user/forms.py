from django import forms
from django.contrib.auth.models import User

class AccountAuthenticationForm(forms.ModelForm):

	password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'required form-control',}))
	username = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'class':'form-control'},))
	class Meta:
		model = User
		fields = ('username', 'password')

	# def clean(self):
	# 	if self.is_valid():
	# 		username = self.cleaned_data['username']
	# 		password = self.cleaned_data['password']
	# 		if not authenticate(username=username, password=password):
	# 			raise forms.ValidationError("Invalid login")
