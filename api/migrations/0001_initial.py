# Generated by Django 3.0.5 on 2020-05-08 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
            ],
        ),
        migrations.CreateModel(
            name='Tire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('width', models.FloatField(default=0)),
                ('profile', models.FloatField(default=0)),
                ('diameter', models.CharField(blank=True, max_length=4)),
                ('seoson', models.CharField(choices=[('L', 'Летние'), ('W', 'Зимние')], default='L', max_length=2)),
                ('producer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Producer')),
            ],
        ),
    ]