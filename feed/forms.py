from django import forms

class posts(forms.Form):
    photo=forms.CharField(required=True,max_length=1000)
    caption=forms.CharField(max_length=200)

class search(forms.Form):
    email=forms.EmailField(required=True)
class comment(forms.Form):
    text=forms.CharField(max_length=200)




