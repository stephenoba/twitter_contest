from django import forms


class EntryForm(forms.Form):
    twitter_handle = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control",
        'placeholder': "twitter handle '@stephenooba'"
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'youemail@example.com',
        'type': 'email',
        'class': "form-control"
    }))

