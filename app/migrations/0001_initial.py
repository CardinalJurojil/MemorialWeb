# Generated by Django 5.1.2 on 2025-01-26 14:01

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Memorial',
            fields=[
                ('memorialid', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('dateofbirth', models.DateField()),
                ('dateofdeath', models.DateField()),
                ('biography', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('messageid', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('dateposted', models.DateField()),
                ('memorial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.memorial')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('photoid', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('datepost', models.DateTimeField(default=django.utils.timezone.now)),
                ('memorial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='app.memorial')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField()),
                ('profilepic', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('memorials', models.ManyToManyField(related_name='tagged_by', to='app.memorial')),
            ],
        ),
        migrations.AddField(
            model_name='memorial',
            name='tags',
            field=models.ManyToManyField(related_name='memorial_tags', to='app.tag'),
        ),
    ]
