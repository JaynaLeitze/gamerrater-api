# Generated by Django 3.1.6 on 2021-02-10 21:51

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
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75)),
                ('description', models.TextField(max_length=300)),
                ('designer', models.CharField(max_length=75)),
                ('release_year', models.IntegerField()),
                ('time_to_play', models.CharField(max_length=20)),
                ('age_recommendation', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='games')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=300)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterapi.game')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterapi.player')),
            ],
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterapi.game')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterapi.player')),
            ],
        ),
        migrations.CreateModel(
            name='GameCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterapi.category')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterapi.game')),
            ],
        ),
    ]
