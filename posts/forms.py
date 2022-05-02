from .models import *
from django.forms import *

class SignUp(ModelForm):
    class Meta:
        model = User_people
        fields = '__all__'
        widgets = {
            "username": TextInput(attrs={
                'label': 'Your Name',
                'class': 'form-control',
                'placeholder': 'Enter a username',
                'id': 'username'
            }),
            "fname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your First Name',
            }),
            "lname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Last Name',
            }),
            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Email Address',
            }),
            "pass1": PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a Password',
            }),
            "pass2": PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Confirm your Password',
            }),
            "country": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your Country',
            }),
            "city": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your City',
            })
        }
# class SignIn(ModelForm):
#     class Meta:
#         model = User_people
#         fields = ('username', 'pass1',)
#         widgets = {
#             "username": TextInput(attrs={
#                 'label': 'Your Name',
#                 'class': 'form-control',
#                 'placeholder': 'Enter a username',
#                 'id': 'username'
#             }),
#             "pass1": PasswordInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Enter a Password',
#             }),
#         }

class Sendmessage(Form):
    subject = CharField(label="Subject", max_length=255,
                        widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a subject of message'}))
    text = CharField(label="Text", max_length=255,
                     widget=Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter a text of message'}))


class DocumentForm(forms.Form):
    docfile = FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )

short_widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя Спортсмена',
                'id': 'title'
            }),
            "content": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
            'slug': TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите Slug URL спортсмена',
            }),
}

class BoxingCreate(ModelForm):
    class Meta:
        model = Boxing
        fields = '__all__'
        widgets = short_widgets


class WrestlingCreate(ModelForm):
    class Meta:
        model = Wrestling
        fields = '__all__'
        widgets = short_widgets

class AthleticsCreate(ModelForm):
    class Meta:
        model = Athletics
        fields = '__all__'
        widgets = short_widgets

class WeightliftingCreate(ModelForm):
    class Meta:
        model = Weightlifting
        fields = '__all__'
        widgets = short_widgets

class CyclingCreate(ModelForm):
    class Meta:
        model = Cycling
        fields = '__all__'
        widgets = short_widgets

class Team_sportsCreate(ModelForm):
    class Meta:
        model = Team_sports
        fields = '__all__'
        widgets = short_widgets


