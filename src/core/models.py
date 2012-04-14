# coding=utf-8

from django.db                import models
from django.utils.translation import ugettext_lazy as _

from custom_managers          import KindContactManager

class Speaker(models.Model):
    name = models.CharField(_('Nome'), max_length=255)
    slug = models.SlugField()
    url = models.URLField(_('Site'), verify_exists=False)
    description = models.TextField(_('Descrição'), blank=True)
    avatar = models.FileField(_('Avatar'), upload_to='palestrantes', blank=True, null=True)

    def __unicode__(self):
        return self.name

class Contact(models.Model):
    # Convenção de código Python variáveis com uppercase, são consideradas como constantes. Verificar PEP8.
    KINDS = (
        ('P', _('Telefone')),
        ('E', _('E-mail')),
        ('F', _('Fax')),
    )

    speaker = models.ForeignKey('Speaker', verbose_name=_('Palestrante'))
    kind = models.CharField(_('Tipo'), max_length=1, choices=KINDS) 
    value = models.CharField(_('Valor'), max_length=255)

    objects = models.Manager()
    phones = KindContactManager('P')
    emails = KindContactManager('E')
    faxes = KindContactManager('F')

