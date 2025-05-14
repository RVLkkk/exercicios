clientes = []

def obter_dados_clientes():

    nome_cliente = input("informe seu nome completo:")
    idade_cliente = int(input("informe sua data de nascimento:"))
    email_cliente = int(input("informe seu email:"))
    endereco_cliente = input("informe o Enderoço:")
    rg_cliente = int(input("informe seu RG:"))
    cpf_cliente = float(input("informe seu cpf:"))
    estado_cliente = input("digite seu estado:")
    cidade_cliente = input("digite sua cidade:")
    celular_cliente = int(input("digite seu celular:"))
    telefone_cliente = int(input("digite seu telefone:"))

    cliente = {
        "nome_cliente": nome_cliente,
        "idade_cliente": idade_cliente,
        "email_cliente": email_cliente,
        "endereco_cliente": endereco_cliente,
        "rg_cliente": rg_cliente,
        "cpf_cliente": cpf_cliente,
        "estado_cliente": estado_cliente,
        "cidade_cliente": cidade_cliente,
        "celular_cliente": celular_cliente,
        "telefone_cliente": telefone_cliente


    }

    return cliente


def cadastrar_cliente(dados_cliente):
    clientes.append(dados_cliente)

    return clientes

def mostrar_dados_clientes(dados_clientes):
    for cliente in dados_clientes:
        print(f"""
          nome do cliente: {cliente["nome_cliente"]}
          idade do cliente: {cliente["idade_cliente"]}
          email do cliente: {cliente["email_cliente"]}
          endereco do cliente: {cliente["endereco_cliente"]}
          rg do cliente: {cliente["rg_cliente"]}
          cpf do cliente: {cliente["cpf_cliente"]}
          estado do cliente: {cliente["estado_cliente"]}
          cidade do cliente: {cliente["cidade_cliente"]}
          celular do cliente: {cliente["celular_cliente"]}
          telefone do cliente: {cliente["telefone_cliente"]}
          
""")
    

def iniciar_sistema():
    while True:
        print("")
        print("=*80")
        print("opçao 1- mostrar lista de clientes.")
        print("opçao 2 - cadastrar clientes.")
        print("opçao 3 - sair do sistema.")
        print("=*80")
        
        opcao = input("escolha uma das opçoes do menu")

        if opcao == "1":
            mostrar_dados_clientes(clientes)
        elif opcao == "2":
            cadastrar_cliente(obter_dados_clientes())
        elif opcao == "3":
            print("sistema finalizado.")
            break
        else:
           print("opçao invalidade, escolha umas das opçoes do menu")