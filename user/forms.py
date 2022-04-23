from django import forms
from .models import User

class Add_A_User(forms.ModelForm):
    # name = forms.CharField(label='name', max_length=256)
    # email = forms.EmailField()
    # gender = forms.CharField(label='gender', max_length=10)
    # status = forms.CharField(label='status', max_length=20)
    class Meta:
        model = User
        fields = ['name', 'email', 'gender', 'status']