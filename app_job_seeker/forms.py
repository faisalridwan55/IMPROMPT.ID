from django import forms

class ProfileEdit(forms.Form):
    error_message = {
        'required': 'This field is required to fill',
    }
    first_name = {
        'type': 'text',
        'class': 'form-control',
        'placeholder': 'First Name',
    }
    last_name = {
        'type': 'text',
        'class': 'form-control',
        'placeholder': 'Last Name',
    }
    birthday = {
        'type': 'text',
        'class': 'form-control',
        'placeholder': 'DD/MM/YYYY',
    }
    phone_number = {
        'type': 'text',
        'class': 'form-control',
        'placeholder': 'Enter valid phone number',
    }
    email = {
        'type': 'email',
        'class': 'form-control',
        'placeholder': 'Enter valid email adress',
    }

    first_name = forms.CharField(label='First Name', required=True, max_length=140, widget=forms.TextInput(attrs=first_name))
    last_name = forms.CharField(label='Last Name', required=True, max_length=140, widget=forms.TextInput(attrs=last_name))
    email = forms.CharField(label='Email', required=True, max_length=140, widget=forms.TextInput(attrs=email))
    birthday = forms.CharField(label='Birthday Date', required=True, max_length=140, widget=forms.TextInput(attrs=birthday))
    phone_number = forms.CharField(label='Phone Number', required=True, max_length=140, widget=forms.TextInput(attrs=phone_number))