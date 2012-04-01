# coding=utf-8

from django import forms

class PhoneWidget(forms.MultiWidget):
    
    def __init__(self, attrs=None):
        ddd_attrs = {'class':'ddd', 'maxlength':'2'}
        phone_attrs = {'class':'phone', 'maxlength':'9'}

        widgets = (
            forms.TextInput(attrs=ddd_attrs),
            forms.TextInput(attrs=phone_attrs)
        )

        super(PhoneWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if not value:
            return [None, None]
        return value.split('-')