# Generated by Django 4.2 on 2025-02-03 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_alter_content_content_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=15)),
                ('messages', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='content',
            name='content_type',
            field=models.CharField(choices=[('portfolio', 'Portfolio Card'), ('hero_slide', 'Hero Slayt'), ('service', 'Service'), ('team_member', 'Team Member'), ('clients', 'Clients'), ('comments', 'Comments'), ('features', 'Features'), ('blog', 'Blog'), ('product', 'Product')], max_length=50),
        ),
    ]
