from django import forms

class RegForm(forms.Form):
	nombre = forms.CharField(max_Length=100)
	edad = forms.IntegerField()