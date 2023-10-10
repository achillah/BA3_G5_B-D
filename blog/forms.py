from django import forms
from .models import Request
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


RIGHT_CHOICES =(
    (False, "No rights (read only)"),
    (True, "Administrator rights"),
)


class UserCreationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(label="First name")
    last_name = forms.CharField(label="Last name")
    is_staff = forms.ChoiceField(label="User rights",choices=RIGHT_CHOICES)

    class Meta :
        model = User
        fields = ['username', 'email', 'first_name', 'last_name','password1', 'password2', 'is_staff']


class UserCreationUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField(label="First name")
    last_name = forms.CharField(label="Last name")
    is_staff = forms.ChoiceField(label="User rights",choices=RIGHT_CHOICES)

    class Meta :
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'is_staff']



class RequestCreationForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['title', 'reference_number', 'start_date', 'deadline', 'priority', 'budget', 'status', 'faction',
                  'consultant', 'main_skills', 'consultant_level', 'attachment']

    def __init__(self, *args, **kwargs):
        super(RequestCreationForm, self).__init__(*args, **kwargs)
        self.fields['attachment'].required = False