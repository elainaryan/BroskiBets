from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    from_email = forms.EmailField(required=True, label="Email")
    message = forms.CharField(widget=forms.Textarea, required=True, max_length="500")