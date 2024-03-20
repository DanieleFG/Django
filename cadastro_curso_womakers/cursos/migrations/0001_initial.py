# Generated by Django 4.2.11 on 2024-03-12 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Curso",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo", models.CharField(max_length=50)),
                (
                    "nivel",
                    models.CharField(
                        choices=[
                            (0, "Iniciante"),
                            (1, "Intermediario"),
                            (2, "Avançado"),
                        ],
                        max_length=50,
                    ),
                ),
                ("carga_horaria", models.IntegerField()),
                ("data_do_curso", models.DateField(help_text="aaaa/mm/dd")),
                ("descricao", models.TextField()),
            ],
            options={
                "verbose_name": "Cadastro de Cursos",
                "verbose_name_plural": "Cadastros de Cursos",
                "ordering": ["-data_do_curso"],
            },
        ),
    ]
