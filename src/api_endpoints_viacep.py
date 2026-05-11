import requests

base_url = "https://viacep.com.br/ws/"


# Criar as funcoes que irao pegar os dados da api
# nome da funcao deve ter o prefixo get, post ou put

def get_ceps(cep):


# 1 - Definir o endpoint que vai ser consumido
    url = f"{base_url}{cep}/json/"

# 2 - Fazer a requisição (pedindo os dados)
    dados = requests.get(url)

# 3 - Retornar os dados
    return dados.json()
