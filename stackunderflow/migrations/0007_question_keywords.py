from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stackunderflow', '0006_auto_20160517_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='keywords',
            field=models.CharField(blank=True, max_length=250),
            preserve_default=False,
        ),
    ]
