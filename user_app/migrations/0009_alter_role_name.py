# Generated by Django 5.0.6 on 2024-06-25 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0008_role_remove_user_role_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='name',
            field=models.CharField(choices=[('Зарегистрированный', 'Registered'), ('Студент', 'Student'), ('Преподаватель', 'Teacher')], default='Зарегистрированный', max_length=50, unique=True),
        ),
    ]
