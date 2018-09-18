from django import forms
from django.core.validators import ValidationError
def validateName(value):
    if value.isdigit():
        raise ValidationError("username cannot be a digit")
def validateEmail(email):
    if email.find('@mytectra.com')<0:
        raise ValidationError("please provide my tectra domain email")

class formexample(forms.Form):
    citylist=(
        ('','--select option--'),
        ('bangalore','Bangalore'),
        ('hyderabad','Hyderabad'),
        ('mysore','Mysore'),
        ('chennai','Chennai')
    )
    city=forms.ChoiceField(choices=citylist)
    is_active=forms.BooleanField(required=False)
    active=forms.CharField(widget=forms.CheckboxInput)
    gen=(
        ('m','male'),
        ('f','female')
    )
    gender = forms.ChoiceField(choices=gen,
                               widget=forms.RadioSelect
                               )
    username = forms.CharField(min_length=8,max_length=20,
                                required=True,label='Name',
                               help_text='please provide valid user name',
                               error_messages={'required':"Emoployee name cannot be blank",
                                               'min_length':'new text'},

                               widget=forms.TextInput(
                        attrs={
           'placeholder':'Employee name..',



    }
                               )

                               )
    email = forms.EmailField()
    address = forms.CharField(max_length=250,
                              widget=forms.Textarea)
    password1=forms.CharField(max_length=20,
                              widget=forms.PasswordInput)
    password2=forms.CharField(max_length=20,
                              widget=forms.PasswordInput)
    def clean(self):
        form_data=self.cleaned_data
        if 'username' in form_data:
            if form_data['username'].isdigit():
                self.errors['username']=['employee name cannot be digits']
        if 'email' in form_data:
            if form_data['email'].find('@mytectra.com')<0:
                self.errors['email']=['invalid email']
        if 'password1' in form_data and 'password2' in form_data:
            if form_data['password1']!= form_data['password2']:
                self.errors['password2']=['password mismatch']

        return form_data
