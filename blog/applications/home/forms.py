from django import forms

from .models import Contact

# class SuscriberForm(forms.ModelForm):
#     class Meta:
#         model = Suscribers
#         fields = {
#             'email'
#         }
#         widgets = {
#             'email' : forms.EmailInput(
#                 attrs={
#                     'placeholder': 'Introduzca email...'
#                 }
#             )
#         }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('__all__')
        
        