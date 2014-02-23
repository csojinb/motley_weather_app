from django import forms

class LocationForm(forms.Form):
    zip_code = forms.RegexField(r'^\d{5}(?:[-\s]\d{4})?$',label='Zip Code')