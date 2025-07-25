# Generated by Django 5.1.5 on 2025-07-14 06:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0006_alter_phonespecdetail_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phonespecsection',
            name='section_title',
        ),
        migrations.CreateModel(
            name='PhoneSpecTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='titles', to='phone.phonespecsection')),
            ],
        ),
        migrations.CreateModel(
            name='PhoneSpecValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='values', to='phone.phonespectitle')),
            ],
        ),
        migrations.DeleteModel(
            name='PhoneSpecDetail',
        ),
    ]
