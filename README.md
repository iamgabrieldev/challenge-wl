# Passo a Passo para Executar uma Aplicação Django Rest Framework

## Pré-requisitos
- Python instalado
- Pip instalado
- Virtualenv instalado

## Passos

1. **Criar e ativar um ambiente virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

2. **Instalar Django e Django Rest Framework:**
    ```bash
    pip install django djangorestframework
    pip install -r requirements.txt
    ```

3. **Executar o servidor de desenvolvimento:**
    ```bash
    docker-compose up -d
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
       user: root
       email: root@root.com
       passoword: root
    
    python manage.py runserver
    ```

4. **Executar os testes unitários e de integração**
    ```bash
    python manage.py test
    ```

5. **Acessar a API:**
    Abra o navegador e vá para `http://127.0.0.1:8000/api/items/`
    