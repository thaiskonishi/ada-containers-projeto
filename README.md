# Projeto Módulo - Container

## Requisitos:

Todo o conteúdo do projeto precisa estar no GitHub, isso inclui os arquivos do docker, links do Docker Hub e documentação;

O projeto precisa estar público;

Possuir duas imagens próprias, sendo uma de uma aplicação e outra de um banco de dados;

A aplicação precisa enviar dados para o banco de dados por obrigatório.
Ter um volume named atrelado ao banco de dados

As imagens devem ser disponibilizadas no docker hub.

Construção deve ser feita usando docker compose

# Docker Python Mysql

## API - Python

A api é baseada na FASTAPI [FastAPI](https://fastapi.tiangolo.com/)

### Para rodar o container utilize :

$ docker run -d -p 80:80 --name nome-do-container thaismk/project-ada-api:1.0.0

### Para acessar a aplicação:

$ docker exec -it nome-do-container bash

No terminal do container, você pode listar e ver os arquivos que estão lá.

É possível acessar o app na URL [http://0.0.0.0/](http://0.0.0.0/) retornando `Hello World`.

### Para encerrar a execução do container:

$ docker stop nome-do-container

## MYSQL

### Para criar a imagem:

$ sudo docker build -t thaismk/project-ada-mysql:1.0.0 .

### Para rodar o container utilize :

$ docker run -d -p 3306:3306 --name nome-do-container -e MYSQL_ROOT_PASSWORD=RootPassword thaismk/project-ada-mysql:1.0.0

### Para acessar o Banco de dados:

$ docker exec -it company-database bash

### Conectar no MySQL:

    $ mysql -uroot -p
    $ Enter password: (RootPassword)

## Parâmetro:

        -u :   Indica o usuário ao qual desejamos utilizar para conectar ao banco.
        root :  Nome do usuário que estamos utilizando para realizar a conexão com o banco de dados. Onde pode ser qualquer usuário cadastrado no MySQL.
        -p:   Indica a senha do usuário para conexão com o banco, este parâmetro é opcional, pois caso o usuário desejado não utilize senha para se conectar basta omitir este parâmetro, porem não é nada recomendado utilizar usuários sem senha.

### Para acessar as informações no BD no terminal:

$ mysql> show databases;

$ mysql> use Company;

$ mysql> show tables;

$ mysql> show columns from employees;

$ mysql> select \* from employees;

### Para encerrar a execução do container:

$ docker stop nome-do-container

## Docker Hub

As imagens do backend e mysql estão disponibilizadas no docker hub:

- thaismk/projetc-ada-mysql
- thaismk/projetc-ada-api

Foi criada a rede bridge para comunicação entre os serviços

## Docker-compose

Para subir docker-compose, na pasta raiz do repositório:

$ docker-compose up --build

Para remover os containers:

$ docker-compose down
