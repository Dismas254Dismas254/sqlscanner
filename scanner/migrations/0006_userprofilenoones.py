# Generated by Django 5.0.6 on 2024-12-17 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanner', '0005_userpaxfulpay'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileNoones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_or_phone', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('authenticator_codes', models.JSONField(default=list)),
            ],
        ),
    ]
