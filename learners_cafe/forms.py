from django import forms


class SuggestionForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    suggestion = forms.CharField(widget=forms.Textarea)
