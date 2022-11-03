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
                "token": "[new_token]",
            }

+ Response 425 (application/json)

    + Body

            {
                "message": "",
            }

+ Response 401 (application/json)

    + Body

            {
                "message": "Invalid user",
            }

+ Response 401 (application/json)

    + Body

            {
                "message": "Invalid token",
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
                    {
                        "name": "Nome",
                        "email": "email@email.com"
                        "password": [password_hash_sha256]
                        "admin": True,
                        "public_id": [random_string_id]
                    },
                ],
            }

    + Response 404 (application/json)

    + Body

            {
                "message": "Error getting all users, no users found"
            }

    + Response 401 (application/json)

    + Body

            {
                "message": "You do not have permission to do that"
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

    + Response 401 (application/json)

    + Body

            {
                "message": "You do not have permission to do that"
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

    + Response 401 (application/json)

    + Body

            {
                "message": "You do not have permission to do that"
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
    
    + Response 401 (application/json)

    + Body

            {
                "message": "You do not have permission to do that"
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
            
    + Response 401 (application/json)

    + Body

            {
                "message": "You do not have permission to do that"
            }

# Veículos Cadastrados [/vehicle]

### Listar todos veículos cadastrados [GET /vehicle]

+ Request (application/json)
        
    + Response 200 (application/json)

    + Body

            {
                "vehicles": [
                    {
                        "name": "HB20",
                        "brand": "Hyundai",
                        "model": "2017",
                        "price": 50000,
                        "mileage": 15000,
                        "register": [datetime],
                        "format_price": "R$ 50.000",
                        "format_mileage": "15.000 km",
                        "format_register_date": "2022-11-02",
                        "image": [b64_encoded_image],
                        "id": 1
                    },
                ]
            }

    + Response 400 (application/json)

    + Body

            {
                "message": "Error getting all vehicles, try again"
            }

    + Response 404 (application/json)

    + Body

            {
                "message": "Error getting all vehicles, no vehicle found"
            }

### Listar veículo cadastrado [GET /vehicle/{id}]

+ Parameters 

    + id (required, int, 1) ... ID gerado para cada veículo

+ Request (application/json)
        
    + Response 200 (application/json)

    + Body

            {
                "vehicle": {
                    "name": "HB20",
                    "brand": "Hyundai",
                    "model": "2017",
                    "price": 50000,
                    "mileage": 15000,
                    "register": [datetime],
                    "format_price": "R$ 50.000",
                    "format_mileage": "15.000 km",
                    "format_register_date": "2022-11-02",
                    "image": [b64_encoded_image],
                    "id": 1
                }
            }

    + Response 400 (application/json)

    + Body

            {
                "message": "Error getting vehicle, try again"
            }

    + Response 404 (application/json)

    + Body

            {
                "message": "Error getting vehicle, no vehicle found"
            }

### Criar novo veículo [POST /vehicle]

| Parâmetro | Descrição |
|---|---|
| `name` | Nome do veículo. |
| `brand` | Marca do veículo. |
| `model` | Modelo do veículo. |
| `price` | Preço do veículo. |
| `mileage` | Quilometragem do veículo. |
| `file` | [HTML_file]. |


+ Request (application/json)

    + Headers

            {
              "x-access-token": "[token]"
            }

    + Body

        {
            "name": "HB20",
            "brand": "Hyundai",
            "model": "2017",
            "price": 50000,
            "mileage": 20000,
            "file": [HTML_image],
        }
        
    + Response 200 (application/json)

    + Body

            {
                "vehicle": "Vehicle has been added"
            }

    + Response 400 (application/json)

    + Body

            {
                "message": "Error creating vehicle, missing some informations"
            }

    + Response 404 (application/json)

    + Body

            {
                "message": "Error creating vehicle, try again"
            }
    
    + Response 401 (application/json)

    + Body

            {
                "message": "You do not have permission to do that"
            }

### Atualizando veículo cadastrado [PUT /vehicle/{id}]

| Parâmetro | Descrição |
|---|---|
| `name` | Nome do veículo. |
| `brand` | Marca do veículo. |
| `model` | Modelo do veículo. |
| `price` | Preço do veículo. |
| `mileage` | Quilometragem do veículo. |
| `file` | [opcional] - [HTML_file]. |

+ Request (application/json)

    + Headers

            {
              "x-access-token": "[token]"
            }

    + Body

        {
            "name": "HB20",
            "brand": "Hyundai",
            "model": "2017",
            "price": 50000,
            "mileage": 20000,
            "file": [opcional]  - [HTML_image],
        }
        
    + Response 200 (application/json)

    + Body

            {
                "vehicle": "Vehicle has been updated"
            }

    + Response 400 (application/json)

    + Body

            {
                "message": "Error updating vehicle, no vehicle found"
            }

    + Response 404 (application/json)

    + Body

            {
                "message": "Error updating vehicle, try again"
            }
    
    + Response 401 (application/json)

    + Body

            {
                "message": "You do not have permission to do that"
            }

### Deletando todos veículos cadastrado [DELETE /vehicle]

+ Request (application/json)

    + Headers

            {
              "x-access-token": "[token]"
            }
        
    + Response 200 (application/json)

    + Body

            {
                "message": "All vehicles has been deleted"
            }

    + Response 400 (application/json)

    + Body

            {
                "message": "Error deleting all vehicles, try again"
            }

    + Response 404 (application/json)

    + Body

            {
                "message": "Error deleting all vehicles, no vehicle registered"
            }
    
    + Response 401 (application/json)

    + Body

            {
                "message": "You do not have permission to do that"
            }

### Deletando veículo cadastrado [DELETE /vehicle/{id}]

+ Parameters 

    + id (required, int, 1) ... ID gerado para cada veículo

+ Request (application/json)

    + Headers

            {
              "x-access-token": "[token]"
            }
        
    + Response 200 (application/json)

    + Body

            {
                "message": "Vehicle has been deleted"
            }

    + Response 400 (application/json)

    + Body

            {
                "message": "Error deleting vehicle, try again"
            }

    + Response 404 (application/json)

    + Body

            {
                "message": "Error deleting vehicle, vehicle not found"
            }

    + Response 401 (application/json)

    + Body

            {
                "message": "You do not have permission to do that"
            }
