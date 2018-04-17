from django import forms

class SearchDropdown(forms.Form):
    categories = {
        ('null', 'Select Category'),
        ('internship', 'Internship'),
        ('volunteer', 'Volunteer'),
        ('jobs', 'Jobs'),
        ('conference', 'Conference'),
        ('community', 'Community'),
    }
    field = {
        ('null', 'Select Field'),
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
    opportunity_category = forms.ChoiceField(choices=categories, initial='null', required=True, widget=forms.Select(attrs={'class':'form-control'}))
    opportunity_field = forms.ChoiceField(choices=field, initial='null', required=True, widget=forms.Select(attrs={'class':'form-control'}))
