# coding=utf-8

from django.db                import models
from django.utils.translation import ugettext_lazy as _

from custom_managers          import KindContactManager, PeriodManager

class Speaker(models.Model):
    name = models.CharField(_('Nome'), max_length=255)
    slug = models.SlugField()
    url = models.URLField(_('Site'), verify_exists=False)
    description = models.TextField(_('Descrição'), blank=True)
    avatar = models.FileField(_('Avatar'), upload_to='palestrantes', blank=True, null=True)

    class Meta:
        verbose_name = _('Palestrante')

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

    class Meta:
        verbose_name = _('Contato')

class Talk(models.Model):
    title = models.CharField(_('Atividade'), max_length=200)
    description = models.TextField(_('Descrição'))
    start_time = models.TimeField(_(u'Início'), blank=True)
    speakers = models.ManyToManyField('Speaker', verbose_name=_('Palestrantes'))

    objects = PeriodManager()

    class Meta:
        verbose_name = _('Palestra')

    def __unicode__(self):
        return unicode(self.title)

class Course(Talk):
    slots = models.IntegerField()
    notes = models.TextField()

    objects = PeriodManager()

    class Meta:
        verbose_name = _('Curso')

class Media(models.Model):
    MEDIAS = (
        ('SL', 'SlideShare'),
        ('YT', 'Youtube'),
    )

    talk = models.ForeignKey('Talk', verbose_name=_('Palestra'))
    type = models.CharField(_('Tipo'), max_length=2, choices=MEDIAS)
    title = models.CharField(_(u'Título'), max_length=255)
    media_id = models.CharField(_('Media_ID'), max_length=255)

    class Meta:
        verbose_name = _(u'Mídia')
    
    def __unicode__(self):
        return u'%s - %s' % (self.talk.title, self.title)
