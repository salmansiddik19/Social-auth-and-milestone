# Generated by Django 3.2.1 on 2021-05-19 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MilestoneImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, upload_to='')),
                ('milestone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social_app.milestone')),
            ],
        ),
    ]
