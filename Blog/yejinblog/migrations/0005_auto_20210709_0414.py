# Generated by Django 3.2.5 on 2021-07-09 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yejinblog', '0004_study'),
    ]

    operations = [
        migrations.AlterField(
            model_name='study',
            name='study_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='study',
            name='study_title',
            field=models.CharField(max_length=200),
        ),
    ]