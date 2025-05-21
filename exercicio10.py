import json
import os

data = "filmes.json"

def carregar_dados():
    if os.path.exists(data):
        with open(data, "r", encoding="utf-8") as arq_json:
            return json.load(arq_json)
    else:
        return []


filmes = carregar_dados()
for categoria in filmes:
    print(f'nome do filme: {"O filme"["nome"]} categoria do filme: {categoria ["nome"]}')

#-------------------------------------------------------------------------------------------------------------------
def obter_dados_cliente():   
    filme_cliente = input("informe o nome do filme:")
    categoria_cliente =input("informe a categoria do filme:")
    descricao_cliente = input("informe a descriçao do filme:")
    classificacao_cliente = input("informe a classificaçao do filme:")
   

    cliente = {
        "filme_cliente": filme_cliente,
        "categoria_cliente": categoria_cliente,
        "descricao_cliente": descricao_cliente,
        "classificacao_cliente": classificacao_cliente
  

    }

    return cliente

#-------------------------------------------------------------------------------------------------------------------

def cadastrar_filmes(nome_filme, categoria_filme):
    dados_filme = []
    
    filme = {
        "nome_filme": nome_filme,
        "categoria_filme": categoria_filme
}

    dados_filme.append(filme)
    return dados_filme

#--------------------------------------------------------------------------------------------------------------------

def iniciar_sistema():
    clientes = carregar_dados()
    while True:
        
        print("")
        print("="*80)
        print("Opcao 1 - Mostrar Lista de Clientes")
        print("Opcao 2 - Cadastrar Clientes")
        print("Opcao 3 - Sair do Sistema.")
        print("="*80)

        opcao = input("Escolha uma das opções do Menu: ")

        if opcao == "1":
            cadastrar_filmes(clientes)
        elif opcao == "2":
            obter_dados_cliente(obter_dados_cliente())
        elif opcao == "3":
            print("Sistema Finalizado")
            break
        else:
            print("Opcao invalida, escolha uma das opções no menu.")
iniciar_sistema()