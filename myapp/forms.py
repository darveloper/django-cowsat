from django import forms

class AddTextForm(forms.Form):
    textinput = forms.CharField(widget=forms.Textarea)