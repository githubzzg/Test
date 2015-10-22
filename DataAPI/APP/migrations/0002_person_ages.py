# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='ages',
            field=models.IntegerField(default=20),
            preserve_default=False,
        ),
    ]
