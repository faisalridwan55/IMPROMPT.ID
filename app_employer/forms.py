from django import forms

class EmployerProfileEdit(forms.Form):
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
    email = {
        'type': 'email',
        'class': 'form-control',
        'placeholder': 'Enter valid email adress',
    }
    phone_number = {
        'type': 'text',
        'class': 'form-control',
        'placeholder': 'Enter valid phone number',
    }

    first_name = forms.CharField(label='First Name', required=True, max_length=140, widget=forms.TextInput(attrs=first_name))
    last_name = forms.CharField(label='Last Name', required=True, max_length=140, widget=forms.TextInput(attrs=last_name))
    email = forms.CharField(label='Email', required=True, max_length=140, widget=forms.TextInput(attrs=email))
    phone_number = forms.CharField(label='Phone Number', required=True, max_length=140, widget=forms.TextInput(attrs=phone_number))

class CompanyProfileEdit(forms.Form):
    error_message = {
        'required': 'This field is required to fill',
    }
    company_name = {
        'type': 'text',
        'class': 'form-control',
        'placeholder': 'Company Name',
    }
    country = {
        'type': 'text',
        'class': 'form-control',
        'placeholder': 'Country',
    }
    website = {
        'type': 'url',
        'class': 'form-control',
        'placeholder': 'Enter your company website',
    }
    province = {
        'type': 'text',
        'class': 'form-control',
        'placeholder': 'Province',
    }
    city = {
        'type': 'text',
        'class': 'form-control',
        'placeholder': 'City',
    }
    company_description = {
        'type': 'text',
        'cols': 50,
        'rows': 4,
        'class': 'form-control desc_textarea',
        'placeholder': 'Tell us about your company briefly',
    }
    company_name = forms.CharField(label='Company Name', required=True, max_length=140, widget=forms.TextInput(attrs=company_name))
    country = forms.CharField(label='Country', required=True, max_length=140, widget=forms.TextInput(attrs=country))
    province = forms.CharField(label='Province/State', required=True, max_length=140, widget=forms.TextInput(attrs=province))
    city = forms.CharField(label='City', required=True, max_length=140, widget=forms.TextInput(attrs=city))
    company_website = forms.CharField(label='Company Website', required=True, max_length=140, widget=forms.TextInput(attrs=website))
    company_description = forms.CharField(label='Company Description', required=True, max_length=140, widget=forms.Textarea(attrs=company_description))
