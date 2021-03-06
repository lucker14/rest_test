# Generated by Django 3.1.13 on 2021-09-08 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
                ('completed', models.BooleanField(default=False)),
                ('relates_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.task')),
            ],
        ),
    ]
