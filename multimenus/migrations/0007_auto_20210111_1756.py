# Generated by Django 2.2.17 on 2021-01-11 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multimenus', '0006_auto_20200715_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
