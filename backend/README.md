## Métodos
Requisições para a API devem seguir os padrões:
| Método | Descrição |
|---|---|
| `GET` | Retorna lista de items registrados no banco de dados. |
| `POST` | Registra um novo item no banco de dados. |
| `PUT` | Atualiza dados de um registro ou altera sua situação. |
| `DELETE` | Remove um registro do sistema. |


## Respostas

| Código | Descrição |
|---|---|
| `200` | Requisição executada com sucesso (success).|
| `400` | Erros de validação ou os campos informados não existem no sistema.|
| `401` | Não possui autorização a partir do token.|
| `404` | Registro pesquisado não encontrado (Not found).|
| `406` | Algumas informações podem estar faltando.|

# Autenticação - JWT

A  API utiliza [JWT](https://developers.docusign.com/platform/auth/jwt/) como forma de autenticação/autorização.

# Autenticações
## Solicitando token de acesso [/auth/login]
### POST

| Parâmetro | Descrição |
|---|---|
| `email` | Email cadastrado no sistema. |
| `password` | Senha cadastrada juntamente com o email. |


+ Request (application/json)

    + Body

            {
              "email": "email@teste.com"
              "password": "12345",
            }

+ Response 200 (application/json)

    + Body

            {
                "token": "[token]",
                "admin": "True",
            }

+ Response 404 (application/json)

    + Body

            {
                "message": "Error logging, wrong password!",
            }

+ Response 404 (application/json)

    + Body

            {
                "message": "Error logging, email not found!",
            }

+ Response 406 (application/json)

    + Body

            {
                "message": "Error logging, missing informations!",
            }

## Registrando novo usuário [/auth/register]
### POST

| Parâmetro | Descrição |
|---|---|
| `name` | Nome do usuário. |
| `email` | Email do usuário. |
| `password` | Senha de no mínimo 6 caracteres. |


+ Request (application/json)

    + Body

            {
              "name": "Nome"
              "email": "email@teste.com"
              "password": "12345",
            }

+ Response 200 (application/json)

    + Body

            {
                "message": "User has been registered",
            }

+ Response 406 (application/json)

    + Body

            {
                "message": "Error creating new user, missing informations",
            }

## Solicitando novo token [/auth/refresh_token]
### GET

| Parâmetro | Descrição |
|---|---|
| `token` | Token gerado anteriormente pelo usuário. |


+ Request (application/json)

    + Body

            {
              "token": "[token]"
            }

+ Response 200 (application/json)

    + Body

            {
                "message": "User has been registered",
            }

+ Response 406 (application/json)

    + Body

            {
                "message": "Error creating new user, missing informations",
            }

# Usuários Cadastrados [/user]

### Listar todos usuários cadastrados [GET /user]

+ Request (application/json)

    + Headers

            {
              "x-access-token": "[token]"
            }
        
    + Response 200 (application/json)

    + Body

            {
                "users": [
                    "name": "Nome",
                    "email": "email@email.com"
                    "password": [password_hash_sha256]
                    "admin": True,
                    "public_id": [random_string_id]
                ],
            }

    + Response 404 (application/json)

    + Body

            {
                "message": "Error getting all users, no users found"
            }

### Listar usuário específico [GET /user/{public_id}]

+ Parameters 

    + public_id (required, string, '123_abc') ... ID Público gerado para cada usuário


+ Request (application/json)

    + Headers

            {
              "x-access-token": "[token]"
            }
        
    + Response 200 (application/json)

    + Body

            {
                "user": {
                    "name": "Nome",
                    "email": "email@email.com"
                    "password": [password_hash_sha256]
                    "admin": True,
                    "public_id": [random_string_id]
                },
            }

    + Response 404 (application/json)

    + Body

            {
                "message": "Error getting all users, no users found"
            }

### Promover usuário para administrador [PUT /user/{public_id}]

+ Parameters 

    + public_id (required, string, '123_abc') ... ID Público gerado para cada usuário


+ Request (application/json)

    + Headers

            {
              "x-access-token": "[token]"
            }
        
    + Response 200 (application/json)

    + Body

            {
                "user": "User has been promoted to admin"
            }

    + Response 400 (application/json)

    + Body

            {
                "message": "User already is admin"
            }

    + Response 404 (application/json)

    + Body

            {
                "message": "Error promoting user, no user found"
            }

### Deletando todos usuários [DELETE /user]

+ Request (application/json)

    + Headers

            {
              "x-access-token": "[token]"
            }
        
    + Response 200 (application/json)

    + Body

            {
                "user": "All users has been deleted"
            }

    + Response 400 (application/json)

    + Body

            {
                "message": "Error deleting user, try again"
            }

### Deletando usuário [DELETE /user/{public_id}]

+ Parameters 

    + public_id (required, string, '123_abc') ... ID Público gerado para cada usuário


+ Request (application/json)

    + Headers

            {
              "x-access-token": "[token]"
            }
        
    + Response 200 (application/json)

    + Body

            {
                "user": "User has been deleted"
            }

    + Response 400 (application/json)

    + Body

            {
                "message": "Error deleting user, try again"
            }

    + Response 404 (application/json)

    + Body

            {
                "message": "Error deleting user, no users found"
            }
