from cursos.models import Curso
from datetime import date
import pytest
from model_bakery import baker


@pytest.fixture
def curso():
    curso = baker.make(
        Curso,
        titulo='Java',
        data_do_curso=date.today(),
        carga_horaria='60'
    )
    return curso

@pytest.mark.django_db
def test_str_deve_retornar_string(curso):    
    assert str(curso) == 'Java: 2024-03-16 - 60'