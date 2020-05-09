from django import forms
from .cars import car_list, eng_list, body_list, drive_list, model_list, reg_list

class priceForm(forms.Form):

    car = forms.ChoiceField(choices=list(car_list))
    body = forms.ChoiceField(choices=list(body_list))
    mileage = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'How far has it gone?'}))
    engV = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'How many litres can it hold?'}))
    engType = forms.ChoiceField(choices=list(eng_list))
    registration = forms.ChoiceField(choices=list(reg_list))
    year = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'What year was it made?'}))
    model = forms.ChoiceField(choices=list(model_list))
    drive = forms.ChoiceField(choices=list(drive_list))
    