# Generated by Django 5.1.4 on 2025-01-13 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_bookinstance_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': [('can_mark_returned', 'Can mark books as returned')]},
        ),
    ]
