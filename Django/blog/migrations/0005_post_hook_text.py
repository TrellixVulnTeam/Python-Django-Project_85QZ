# Generated by Django 3.2.5 on 2021-07-03 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_file_upload'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='hook_text',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]