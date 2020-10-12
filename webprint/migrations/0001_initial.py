# Generated by Django 3.1.2 on 2020-10-11 22:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Print',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='name')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='publication date')),
                ('expires_in', models.IntegerField(choices=[(1, '1 hour'), (2, '2 hours'), (24, '1 day'), (48, '2 days'), (168, '1 week')], default=48, verbose_name='expires in')),
                ('ip', models.GenericIPAddressField(verbose_name='IP')),
                ('desc', models.TextField(blank=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'print',
                'verbose_name_plural': 'prints',
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='PrintImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(verbose_name='order')),
                ('img', models.ImageField(upload_to='webprint/', verbose_name='image')),
                ('print', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imgs', to='webprint.print', verbose_name='print')),
            ],
            options={
                'verbose_name': 'image',
                'verbose_name_plural': 'images',
                'ordering': ['order'],
            },
        ),
    ]
