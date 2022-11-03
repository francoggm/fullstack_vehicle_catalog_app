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

# Group Autenticação - JWT

A API utiliza [JWT](https://developers.docusign.com/platform/auth/jwt/) como forma de autenticação/autorização.


## Solicitando token de acesso [/auth/login]

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

# Group Recursos

# Dados da empresa [/empresa]

Buscar detalhes da conta.

### Listar (List) [GET /empresa]

+ Request (application/json)

    + Headers

            Authorization: Bearer [access_token]


+ Response 200 (application/json)

          {
    "subdom": "zipline",
    "nome": "ZIPLINE TECNOLOGIA LTDA",
    "fantasia": "",
    "cpfcnpj": "04693497000121",
    "fones": "5530263336",
    "emails": "suporte@zipline.com.br",
    "end": "Rua do Acampamento",
    "num": "380",
    "compl": "SALA  1 - 2 E 3",
    "bairro": "Centro",
    "cidadeNome": "Santa Maria",
    "cidadeCod": "4316907",
    "uf": "RS",
    "cep": "97050002",
    "cifrao": "",
    "crt": 10,
    "atividade": 10,
    "pSimples": 4,
    "pICMS": "",
    "pPIS": "",
    "pCOFINS": "",
    "baseIRPJ": "",
    "baseCSLL": "",
    "pIRPJ": "",
    "pCSLL": "",
    "inscMunicipal": "4628202",
    "tipoIE": "",
    "inscEstadual": "",
    "cnae": "6203100",
    "codTributMunicipio": "724",
    "regimeTributacao": "0",
    "cmc": "",
    "RNTRC": ""
}
