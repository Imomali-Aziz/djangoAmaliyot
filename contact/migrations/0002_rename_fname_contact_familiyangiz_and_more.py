# Generated by Django 4.1.1 on 2022-09-07 15:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='fname',
            new_name='familiyangiz',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='lname',
            new_name='ismingiz',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='message',
            new_name='xabar',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='phone',
        ),
        migrations.AddField(
            model_name='contact',
            name='telefon',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Telefon raqamni quyidagi ko'rinishda kiritishingiz kerak: '+999999999'. 15 tagacha belgi kiritishingiz mumkin.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
