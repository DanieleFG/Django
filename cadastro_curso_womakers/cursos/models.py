from django.db import models

# Create your models here.
class Curso(models.Model):
    niveis_de_curso = (
        ('Iniciante', 'Iniciante'),
        ('Intermediario', 'Intermediario'),
        ('Avançado', 'Avançado')
    )
    titulo = models.CharField(max_length=50)
    nivel = models.CharField(max_length=50, choices=niveis_de_curso)
    carga_horaria = models.IntegerField()
    data_do_curso = models.DateField(help_text='aaaa/mm/dd')
    descricao = models.TextField()

    def __str__(self):
        return f'{self.titulo}: {self.data_do_curso} - {self.carga_horaria}'

    class Meta:
        verbose_name = 'Cadastro de Cursos'
        verbose_name_plural = 'Cadastros de Cursos'
        ordering = ['-data_do_curso']