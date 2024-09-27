# Documentação Básica do Git

Aviso: nunca faça commit na main. Crie branches para as atualizações.

## Criando uma Nova Branch

Antes de iniciar qualquer alteração, crie uma branch específica para suas modificações. Use o seguinte comando:

git checkout -b nome-da-branch

Esse comando cria uma nova branch e muda automaticamente para ela.

## Fazendo Commits

Após realizar suas alterações, siga os passos abaixo para registrar e enviar as mudanças:

### 1. Adicionar arquivos ao commit:

git add .

### Criar um commit explicando suas alterações:

git commit -m "Descreva suas alterações aqui"

### Enviar sua branch para o repositório remoto:

git push origin nome-da-branch

## Criando uma Pull Request (PR)

Depois de concluir suas alterações e enviar a branch para o repositório remoto, crie uma Pull Request (PR) para que suas mudanças possam ser revisadas e mescladas na branch principal. Isso pode ser feito pelo próprio GitHub.

## Gerenciando Branches

Listar as branches existentes: Para visualizar todas as branches no repositório, utilize:

git branch

Mudar para uma branch existente: Para alternar entre branches, execute o comando:

git checkout nome-da-branch

## Atualizando repositório local com a main

git checkout main
git pull origin main