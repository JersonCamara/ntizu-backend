# Generated by Django 4.2.7 on 2023-11-09 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_empresamodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresamodel',
            name='profissao',
        ),
        migrations.AddField(
            model_name='empresamodel',
            name='nuit',
            field=models.CharField(default=123, max_length=50),
            preserve_default=False,
        ),
    ]
