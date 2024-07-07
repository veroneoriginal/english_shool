from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control'}
    )
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control'}
        )
    )
