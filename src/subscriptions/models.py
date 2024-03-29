# coding=utf-8

from django.db import models
from django.utils.translation import ugettext_lazy as _

from subscriptions.validators import CPFValidator

# Create your models here.
class Subscription(models.Model):
    name = models.CharField(_('Nome'), max_length=100)
    cpf = models.CharField(_('CPF'), max_length=11, unique=True, validators=[CPFValidator])
    email = models.EmailField(_('E-mail'), unique=True, null=True)
    phone = models.CharField(_('Telefone'), max_length=20, blank=True)
    created_at = models.DateTimeField(_('Criado em'), auto_now_add=True)
    paid = models.BooleanField(_('Pago'))
    
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['created_at']
        verbose_name = _(u'Inscrição')
        verbose_name_plural = _(u'Inscrições')