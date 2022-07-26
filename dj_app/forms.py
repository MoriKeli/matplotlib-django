from random import choices
from django import forms
from django.contrib.auth.models import User


class UserForm(forms.Form):
    choice_chart = (
        ('Bar Chart', 'Bar Chart'),
        ('Line Chart', 'Line Chart'),
        ('Pie Chart', 'Pie Chart')
    )
    chart = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select'}), choices=choice_chart)