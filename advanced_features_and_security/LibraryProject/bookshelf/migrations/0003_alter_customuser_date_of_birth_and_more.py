# Generated by Django 5.1.2 on 2024-11-16 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0002_alter_book_options_customuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/'),
        ),
    ]
