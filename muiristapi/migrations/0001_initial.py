# Generated by Django 3.2.9 on 2021-12-06 19:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Muirist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Park',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('location', models.CharField(max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('content', models.CharField(max_length=120)),
                ('muirist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='muiristapi.muirist')),
                ('park', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='muiristapi.park')),
            ],
        ),
        migrations.CreateModel(
            name='SnippetList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lists', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='muiristapi.list')),
                ('snippets', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='muiristapi.snippet')),
            ],
        ),
        migrations.AddField(
            model_name='list',
            name='muirist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='muiristapi.muirist'),
        ),
        migrations.AddField(
            model_name='list',
            name='park',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='muiristapi.park'),
        ),
        migrations.CreateModel(
            name='FavoritePark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('muirist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='muiristapi.muirist')),
                ('parks', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='muiristapi.park')),
            ],
        ),
    ]
