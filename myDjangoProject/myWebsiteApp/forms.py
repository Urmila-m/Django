from django import forms

class GetFeedback(forms.Form):
    GENDER=[('male', 'Male'), ('female', 'Female'), ('others', 'Others')]
    ITEM=[('momo', 'momo'), ('pizza', 'pizza'), ('chwela baji', 'chwela baji'), ('newari khaja set', 'newari khaja set'), ('chicken chilly', 'chicken chilly'), ('coffee', 'coffee')]
    name = forms.CharField(max_length=50)
    address = forms.CharField(max_length=50)
    email = forms.EmailField()                  # primary_kry=True raakhda ni hunxa or by default euta integer primary field id, django le asssign gareko hunxa
    gender = forms.ChoiceField(choices= GENDER, widget=forms.RadioSelect)
    item = forms.ChoiceField(choices=ITEM)
    quantity = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput, max_length=50)
    suggestion = forms.CharField(widget=forms.Textarea)
