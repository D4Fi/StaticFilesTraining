

# static Files


## Etapa 1: Criação do projeto

```bash
django-admin startproject StartProject
```
O django criara um projeto chamado StartProject dentro do dir Project . Com a seguinte estrutura:

```
Project
    ├── StartProject
        ├── settings.py
        ├── __init__.py
        ├── wsgi.py
        ├── asgi.py
        ├── urls.py
        ├── manage.py
```



No Django, a estrutura básica de um projeto gerado por startproject geralmente inclui vários arquivos importantes. Aqui está uma breve descrição de cada arquivo na estrutura que você forneceu:


### settings.py

Este arquivo contém as configurações do seu projeto Django. Aqui você define variáveis como configurações de banco de dados, configurações de aplicativos, chaves secretas, etc. É um arquivo crucial para a configuração do seu projeto.
### init.py

Este é um arquivo vazio que informa ao Python que o diretório contendo este arquivo deve ser considerado um pacote Python. É necessário para que o Python reconheça o diretório como parte do seu pacote.
### wsgi.py

O nome WSGI significa "Web Server Gateway Interface". Este arquivo é usado para expor seu aplicativo Django ao servidor web. É responsável por configurar a interface entre o seu aplicativo e o servidor web.
### asgi.py

O nome ASGI significa "Asynchronous Server Gateway Interface". Este arquivo é semelhante ao wsgi.py, mas é usado quando você deseja suportar conexões assíncronas, úteis para aplicativos em tempo real ou que exigem um tratamento eficiente de muitas conexões simultâneas.
### urls.py

Neste arquivo, você define as rotas URL para o seu projeto Django. Ele mapeia URLs para visualizações específicas, direcionando as solicitações do usuário para o código Python correspondente.
### manage.py

Este é um script de linha de comando que facilita a execução de várias tarefas relacionadas ao seu projeto. Você pode usá-lo para realizar migrações de banco de dados, criar um superusuário, iniciar o servidor de desenvolvimento, entre outras operações.
Esses arquivos são componentes fundamentais de um projeto Django e cada um deles desempenha um papel importante no funcionamento e na configuração do seu aplicativo web.




# Criando o primeiro objeto HTTPresponse
- te








