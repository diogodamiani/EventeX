# coding=utf-8

from django                       import forms
from django.utils.translation     import ugettext_lazy as _
from django.core.validators       import EMPTY_VALUES

from subscriptions.custom_widgets import PhoneWidget

class PhoneField(forms.MultiValueField):
    widget = PhoneWidget

    default_error_messages = {
        'ddd_invalid': _(u'DDD inválido.'),
        'phone_invalid': _(u'Número de Telefone inválido.'),
    }

    def __init__(self, *args, **kwargs):
        fields = (
            forms.IntegerField(),
            forms.IntegerField()
        )
        super(PhoneField, self).__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        if not data_list:
            return None

        if data_list[0] in EMPTY_VALUES:
            raise forms.ValidationError(self.error_messages['ddd_invalid'])

        if data_list[1] in EMPTY_VALUES:
            raise forms.ValidationError(self.error_messages['phone_invalid'])

        return '%s-%s' % tuple(data_list)