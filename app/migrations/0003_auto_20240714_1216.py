# Generated by Django 3.2.25 on 2024-07-14 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20240714_1147'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarefaexterna',
            old_name='caminho_modulo',
            new_name='caminho_script',
        ),
        migrations.RemoveField(
            model_name='tarefaexterna',
            name='nome_funcao',
        ),
        migrations.RemoveField(
            model_name='tarefaexterna',
            name='nome_modulo',
        ),
    ]
