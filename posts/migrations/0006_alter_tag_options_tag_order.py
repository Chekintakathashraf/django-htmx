# Generated by Django 5.1.3 on 2024-12-03 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_rename_sslug_tag_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['-order']},
        ),
        migrations.AddField(
            model_name='tag',
            name='order',
            field=models.IntegerField(null=True),
        ),
    ]