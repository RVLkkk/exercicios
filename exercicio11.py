import json
import os

veiculos = "veiculos.json"

def carregar_dados():
    if os.path.exists(veiculos):
        with open(veiculos, "r", encoding="utf-8") as arq_json:
            return json.load(arq_json)
    else:
        return []

#----------------------------------------------------------------------------------------

def obter_dados():
    marca_carro = input("informe a marca do veiculo:")
    modelo_carro = input("informe o modelo do veiculo:")
    ano_carro = int(input("informe o ano do veiculo:"))
    cor_carro = input("informe a cor do veiculo:")


    cliente = {
    "marca_carro": marca_carro,
    "modelo_carro": modelo_carro,
    "ano_carro": ano_carro,
    "cor_carro": cor_carro

}
    return cliente
#----------------------------------------------------------------------------------------

def cadastrar_veiculo(receber_veiculos):
    db_veiculos = carregar_dados
    db_veiculos.append(receber_veiculos)

    with open(veiculos, "w", encoding="utf-8") as arq_json:
        json.dump(db_veiculos, arq_json, indent=4, ensure_ascili=False) 


#----------------------------------------------------------------------------------------

def mostrar_veiculos(veiculos):
    if veiculos:
        for veiculo in veiculos:
            print(f"""
                  nome do veiculo {veiculos["nome do carro"]}
                  ano do veiculo {veiculos["ano"]}
                cor do veiculo {veiculos["cor"]}
                modelo do veiculo {veiculos["modelo"]}
                  """)
            
        else:
            print("nao exite nenhum veiculo cadastrado")

#------------------------------------------------------------------------------------------
def iniciar_sistema():
    veiculos = carregar_dados()
    while True:
        print("")
        print("=" * 80)
        print("Opção 1 - Mostrar Lista de Veículos")
        print("Opção 2 - Cadastrar Veículo")
        print("Opção 3 - Sair do Sistema")
        print("=" * 80)

opcao = input("Escolha uma das opções do Menu: ")

if opcao == "1":
               mostrar_veiculos("veiculo")
elif opcao == "2":
            cadastrar_veiculo(obter_dados())
            veiculos = carregar_dados()
elif opcao == "3":
            print("Sistema Finalizado")
            
else:
 print("Opção inválida, escolha uma das opções no menu.")

if __name__ == "__main__":
    iniciar_sistema()



