from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Custom validator for project_members
def validate_project_members(value):
    members = [member.strip() for member in value.split(',') if member.strip()]
    if len(members) > 5:
        raise ValidationError(_("Maximum of 5 project members allowed."))

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'

class AddRecordForm(forms.ModelForm):
    STATUS_CHOICES = [
        ('PRE', 'Pre'),
        ('START', 'Start'),
        ('END', 'End'),
    ]

    name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "name", "class": "form-control"}), label="")
    intro = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "intro", "class": "form-control"}), label="")
    status = forms.ChoiceField(required=True, choices=STATUS_CHOICES, widget=forms.Select(attrs={"class": "form-control"}), label="")
    start_datetime = forms.DateTimeField(
        required=True,
        widget=forms.widgets.DateTimeInput(attrs={"placeholder": "start date", "class": "form-control", "type": "datetime-local"}),
        label="",
        input_formats=["%Y-%m-%dT%H:%M"],
    )
    end_datetime = forms.DateTimeField(
        required=True,
        widget=forms.widgets.DateTimeInput(attrs={"placeholder": "end date", "class": "form-control", "type": "datetime-local"}),
        label="",
        input_formats=["%Y-%m-%dT%H:%M"],
    )
    project_members = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "members", "class": "form-control"}),
        label="",
        validators=[validate_project_members],
    )

    class Meta:
        model = Record
        exclude = ("user",)

    def clean_project_members(self):
        data = self.cleaned_data['project_members']
        members = [member.strip() for member in data.split(',') if member.strip()]

        if len(members) > 5:
            raise ValidationError(_("Maximum of 5 project members allowed."))

        return ', '.join(members)
