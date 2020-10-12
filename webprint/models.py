from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Print(models.Model):
    TIME_CHOICES = (
        (1, _('1 hour')),
        (2, _('2 hours')),
        (24, _('1 day')),
        (48, _('2 days')),
        (168, _('1 week')),
    )

    name = models.CharField(_('name'), max_length=120)
    pub_date = models.DateTimeField(_('publication date'), auto_now_add=True)
    expires_in = models.IntegerField(_('expires in'), choices=TIME_CHOICES, default=48)
    ip = models.GenericIPAddressField(_('IP'))
    desc = models.TextField(_('description'), blank=True)

    class Meta:
        verbose_name = _('print')
        verbose_name_plural = _('prints')
        ordering = ['-pub_date']

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'<Print {self.name!r}>'

    def get_absolute_url(self):
        return reverse('webprint:print', args=[str(self.id)])


class PrintImg(models.Model):
    print = models.ForeignKey(Print, on_delete=models.CASCADE, related_name='imgs', verbose_name=_('print'))
    order = models.IntegerField(_('order'))
    img = models.ImageField(_('image'), upload_to='webprint/')

    class Meta:
        verbose_name = _('image')
        verbose_name_plural = _('images')
        ordering = ['order']

    def __str__(self):
        return f'{self.print.name} [IMG {self.order}]'

    def __repr__(self):
        return f'<PrintImg {self.print.name!r} {self.img.name!r}>'
