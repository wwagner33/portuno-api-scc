# 🚀PORTUNO API

**PORTUNO API** é uma API em Python que implementa endpoints de CRUD (Create, Read, Update, Delete) para as entidades e tabelas do banco de dados PostgreSQL: Classroom, Occupancy, Permission, User, Professor, SchoolClass e Semester. A API foi criada utilizando Flask, que é um framework web leve e modular.

## Configuração

Antes de iniciar o uso da API, siga as etapas de configuração abaixo:

1. Clone o repositório para o seu ambiente local:

   ```
   git clone https://github.com/seu-usuario/portuno-api.git
   ```

2. Crie um arquivo `.env` no diretório raiz do projeto e defina as variáveis de ambiente necessárias. Essas variáveis incluem as credenciais do banco de dados e outras configurações específicas do ambiente. Um exemplo básico do conteúdo do arquivo `.env` é mostrado abaixo:

   ```
      USER
      PASSWORD
      HOST
      PORT
      DATABASE
   ```

3. Instale as dependências do projeto. No diretório raiz do projeto, execute o seguinte comando:

   ```
   pip install -r requirements.txt
   ```

4. Após concluir as etapas acima, você está pronto para iniciar a API.

## Uso

A API segue uma arquitetura com camadas de entidades, DAO (Data Access Object) e controladores. Cada entidade corresponde a uma tabela no banco de dados e possui endpoints dedicados para as operações de CRUD. Abaixo está a tabela com os endpoints disponíveis para cada entidade:

| Entidade     | Endpoint            | Descrição                                      |
|--------------|---------------------|------------------------------------------------|
| Classroom    | /classrooms         | Retorna todas as salas                          |
| Classroom    | /classrooms/{id}    | Retorna uma sala específica                     |
| Classroom    | /classrooms         | Cria uma nova sala                              |
| Classroom    | /classrooms/{id}    | Atualiza uma sala existente                     |
| Classroom    | /classrooms/{id}    | Exclui uma sala específica                      |
| Occupancy    | /occupancies        | Retorna todas as ocupações                      |
| Occupancy    | /occupancies/{id}   | Retorna uma ocupação específica                 |
| Occupancy    | /occupancies        | Cria uma nova ocupação                          |
| Occupancy    | /occupancies/{id}   | Atualiza uma ocupação existente                 |
| Occupancy    | /occupancies/{id}   | Exclui uma ocupação específica                  |
| Permission   | /permissions        | Retorna todas as permissões                     |
| Permission   | /permissions/{id}   | Retorna uma permissão específica                |
| Permission   | /permissions        | Cria uma nova permissão                         |
| Permission   | /permissions/{id}   | Atualiza uma permissão existente                |
| Permission   | /permissions/{id}   | Exclui uma permissão específica                 |
| User         | /users              | Retorna todos os usuários                       |
| User         | /users/{id}         | Retorna um usuário específico                   |
| User         | /users              | Cria um novo usuário                            |
| User         | /users/{id}         | Atualiza um usuário
