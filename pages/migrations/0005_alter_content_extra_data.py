# Generated by Django 4.2 on 2025-02-01 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_alter_content_extra_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='extra_data',
            field=models.CharField(blank=True, null=True),
        ),
    ]
