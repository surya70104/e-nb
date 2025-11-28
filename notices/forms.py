from django import forms
from .models import Notice


class NoticeForm(forms.ModelForm):
    expiry_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Notice
        fields = ['title', 'content', 'file', 'category', 'expiry_date']
