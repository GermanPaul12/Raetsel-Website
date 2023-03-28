from django import forms


class FormName(forms.Form):
    name = forms.CharField(max_length=264)
    email = forms.EmailField(max_length=264)
    postcode = forms.CharField(max_length=10)
    text = forms.CharField(widget=forms.Textarea)