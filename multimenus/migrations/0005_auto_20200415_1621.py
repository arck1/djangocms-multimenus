# Generated by Django 2.2.5 on 2020-04-15 16:21

from django.db import migrations
import django.db.models.deletion
import parler.fields


class Migration(migrations.Migration):

    dependencies = [
        ('multimenus', '0004_auto_20170530_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitemtranslation',
            name='master',
            field=parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='multimenus.MenuItem'),
        ),
    ]
