# Generated by Django 5.1.3 on 2024-12-05 18:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0013_likedpost_posts_likes'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LikedComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.ManyToManyField(related_name='likedcomments', through='posts.LikedComment', to=settings.AUTH_USER_MODEL),
        ),
    ]