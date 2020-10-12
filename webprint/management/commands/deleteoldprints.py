from datetime import timedelta
from os import listdir, unlink

from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils import timezone

from ... import models


class Command(BaseCommand):
    help = 'Delete old prints'

    def handle(self, *args, **options):
        now = timezone.now()
        prints = models.Print.objects.values('id', 'pub_date', 'expires_in')
        olds_id = {p['id']
                   for p in prints
                   if p['pub_date'] + timedelta(hours=p['expires_in']) < now}
        models.Print.objects.filter(id__in=olds_id).delete()

        if (settings.MEDIA_ROOT / 'webprint').exists():
            db_imgs = set(models.PrintImg.objects.values_list('img', flat=True))
            hd_imgs = {f'webprint/{f}' for f in listdir(settings.MEDIA_ROOT / 'webprint')}
            for img in hd_imgs.difference(db_imgs):
                unlink(settings.MEDIA_ROOT / img)
