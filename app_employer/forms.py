from django import forms
from django.core.validators import RegexValidator

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
        'type': 'text',
        'class': 'form-control',
        'placeholder': 'Enter your company website, ex: www.example.com',
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
    company_logo = forms.FileField(label='Upload Your Company Logo',required=True)

class OpportunityForm(forms.Form):
    error_message = {
        'required': 'This field is required to fill',
    }
    durations = {
        'type': 'number',
        'class': 'form-control',
        'placeholder': 'In days/week',
    }
    salary = {
        'type': 'text',
        'class': 'form-control',
        'placeholder': 'Rp.xxx,00,-',
    }
    participants_needed = {
        'type': 'number',
        'class': 'form-control',
        'placeholder': 'Enter number of participants needed',
    }
    requirements = {
        'type': 'text',
        'cols': 50,
        'rows': 4,
        'class': 'form-control',
        'placeholder': 'Write your requirements',
    }
    description = {
        'type': 'text',
        'cols': 50,
        'rows': 4,
        'class': 'form-control desc_textarea',
        'placeholder': 'Tell us about this opportunity briefly',
    }
    contact_person_phone_number = {
        'type': 'text',
        'class': 'form-control',
        'placeholder': 'Enter a valid phone number',
    }
    categories = {
        ('internship', 'Internship'),
        ('volunteer', 'Volunteer'),
        ('jobs', 'Jobs'),
        ('conference', 'Conference'),
        ('community', 'Community'),
    }
    field = {
        ('design', 'Design'),
        ('event', 'Event Organizer'),
        ('teaching', 'Teaching'),
        ('operations', 'Operations'),
        ('marketing', 'Marketing'),
        ('photography', 'Photography'),
        ('engineering', 'Engineering'),
        ('media', 'Media and Communication'),
        ('finance', 'Finance'),
        ('fashion', 'Fashion'),
        ('webdev', 'Web Development'),
        ('other', 'Other'),
    }
    opportunity_category = forms.ChoiceField(choices=categories, required=True, widget=forms.Select(attrs={'class':'form-control'}))
    opportunity_field = forms.ChoiceField(choices=field, required=True, widget=forms.Select(attrs={'class':'form-control'}))
    durations = forms.CharField(label='Durations', required=True, max_length=140, widget=forms.TextInput(attrs=durations))
    salary = forms.CharField(label='Salary', required=True, max_length=140, widget=forms.TextInput(attrs=salary))
    participants_needed = forms.CharField(label='Participants Needed', required=True, max_length=140, widget=forms.TextInput(attrs=participants_needed))
    contact_person_phone_number = forms.CharField(label='Contact Person Number', required=True, max_length=140, widget=forms.TextInput(attrs=contact_person_phone_number))
    requirements = forms.CharField(label='Requirements', required=True, max_length=140, widget=forms.Textarea(attrs=requirements))
    description = forms.CharField(label='Short Description', required=True, max_length=140, widget=forms.Textarea(attrs=description))
