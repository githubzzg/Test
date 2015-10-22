# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0002_person_ages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='ages',
        ),
    ]
