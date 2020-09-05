# Generated by Django 3.1 on 2020-08-28 20:46

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
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('total_budget', models.IntegerField()),
                ('fb_buget', models.IntegerField()),
                ('insta_budget', models.IntegerField()),
                ('twitter_budget', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('estimates_reach', models.IntegerField()),
                ('current_reach', models.IntegerField(default=0)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]