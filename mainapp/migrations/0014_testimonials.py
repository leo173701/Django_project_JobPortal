# Generated by Django 3.1.5 on 2021-04-16 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0013_auto_20210417_0407'),
    ]

    operations = [
        migrations.CreateModel(
            name='testimonials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
