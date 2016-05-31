from django import forms

class BloodForm(forms.Form):
    amount = forms.IntegerField(label="Donate amount")
