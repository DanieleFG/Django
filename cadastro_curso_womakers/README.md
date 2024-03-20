 ### Instalação do ambiente virtual
 ```
 pip install virtualenv

 ```

### Criar ambiente Virtual

```
python3 -m venv cadastro_curso_womakers

```

### Ativar ambiente 
```
cd cadastro_curso_womakers/
source bin/activate

```

### Desativar ambiente 
```
 deactivate
```

### Instalar Django

```
pip install django

```

### Criar nosso projeto
```
django-admin startproject projeto_womakers .

```
### Rodar o projeto
```
python3 manage.py runserver

```
### Comando aplicativo
```
python3 manage.py startapp base

```


### Comando instalar bootstrap
``` 
pip install django-bootstrap-v5

```


### Comandos para criar arquivo do Banco de Dados
 ```
    python3 manage.py makemigrations
 ```

### Comandos para enviar para  Banco de Dados
 ```
    python3 manage.py migrate
 ```

### Comandos para ecriar super usuario
 ```
    python3 manage.py createsuperuser
 ```
### Comando criar novo aplicativo cursos
```
python3 manage.py startapp cursos

```

desafio
Usuario que se cadstrou consiga se cadastrar em outro curso 
fazer outro app


# Trabalhando com Cache
### Redis

```
pip install redis

```
# Django Rest Frameworlk
### Instalando Djangp Rest Frameworlk
```
pip install djangorestframework

```

# Testes com pytest

```
pip install pytest-django
pip install pytest

```

### Comando
```
   pytest

```
```
pip install model_bakery

```

https://github.com/IsadoraFerrao/Sistema-Cadastro-Cursos/tree/aula_01
