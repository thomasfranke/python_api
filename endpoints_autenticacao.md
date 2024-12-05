
Para rodar o servidor local, consulte a documentação python.py

# Endpoints

- Endpoints começam com a url do servidor, no localhost é:

http://127.0.0.1:8000

# Autenticação:

### Cadastro

- URL: /autenticacao/cadastro/
- Método: POST

Parâmetros:
- username
- password

Repostas / Status Codes:

- 201: Usuário Criado
    -- Parâmetros:
    --- token => chave de autenticação que deverá ser armazenada de forma segura
- 400: Erro
    -- Normalmente usuário já existente ou senha inválida

### Login:

- URL: /autenticacao/autenticar/
- Método: POST

Parâmetros:
- "username"
- "password"

Repostas / Status Codes:

- 201: Usuário Criado
    -- Parâmetros:
    --- "message" => Usuário autenticado com sucesso
    --- "username" -> Nome do usuário
    --- "token" => chave de autenticação que deverá ser armazenada de forma segura
- 400: Erro
    -- Senha incorreta, etc

### Status:

Endpoint simples para checagem de autenticação, para validar o API Token:

- URL: /autenticacao/status/
- Método: GET

Parâmetros:
- Cabeçalho: Authorization: token <api-token>

Repostas / Status Codes:
- 200: Usuário Autenticado com sucesso
- 401: Não autorizado
    -- Autenticação feita de forma correta

### Logout:

- URL: /autenticacao/logout/
- Método: POST

Parâmetros:
- Bearer Token: enviar o API Token que foi armazenado de forma segura

- 200: Usuário deslogado com sucesso
- 401: Erro no logout / usuário já estava deslogado