# Generated by Django 4.2.3 on 2023-07-29 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_set_card_card_set'),
    ]

    operations = [
        migrations.AlterField(
            model_name='set',
            name='definition_language',
            field=models.CharField(blank=True, default='English', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='set',
            name='term_language',
            field=models.CharField(blank=True, default='English', max_length=100, null=True),
        ),
    ]
