from django import forms

TYPE_CHOICES = [
    ('education', 'Learn something new'),
    ('recreational', 'Do something fun'),
    ('social', 'Do social activities'),
    ('diy', 'Do It Yourself'),
    ('charity', 'Do something for others for free'),
    ('cooking', 'Do something to eat'),
    ('relaxation', 'Take some f***ing relax'),
    ('music', 'Music oriented activities'),
    ('busywork', 'Busywork'),
    ]

class InputForm(forms.Form):
    activity_type = forms.CharField(label='Select activity type', widget=forms.Select(choices=TYPE_CHOICES))
    participants = forms.IntegerField(widget = forms.NumberInput(), min_value=1, max_value=8, initial=1)