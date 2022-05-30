# Generated by Django 4.0.4 on 2022-05-30 07:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('repositories', '0002_alter_repository_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repositoryfile',
            name='language',
            field=models.CharField(
                choices=[('Python', 'Python'), ('C', 'C'), ('C++', 'Cpp'), ('C#', 'C Sharp'), ('CSS', 'Css'),
                         ('Java', 'Java'), ('JS', 'Js'), ('PHP', 'Php'), ('Ruby', 'Ruby'), ('Kotlin', 'Kotlin')],
                help_text='Programming language present in the repository.', max_length=20,
                verbose_name='programming language'),
        ),
    ]
