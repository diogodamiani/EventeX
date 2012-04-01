# coding=utf-8

from django                      import forms
from django.utils.translation    import ugettext_lazy as _

from subscriptions.models        import Subscription
from subscriptions.custom_fields import PhoneField

class SubscriptionForm(forms.ModelForm):
    phone = PhoneField(label=_('Telefone'), required=False)
    email = forms.EmailField(label=_('E-mail'), required=False)

    class Meta:
		model = Subscription
		exclude = ('created_at', 'paid')

    def clean(self):
        super(SubscriptionForm, self).clean()

        if not self.cleaned_data.get('email') and \
           not self.cleaned_data.get('phone'):
            raise forms.ValidationError(_(u'Informe seu e-mail ou telefone.'))

        return self.cleaned_data