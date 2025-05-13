from exercicio4 import calcular_media

alunos = []

def obter_dados_alunos():
    nome_aluno = input("informe o nome completo do aluno:")
    email_aluno = input("informe o email do aluno:")
    serie_aluno = input("informe a serie do aluno:")
    nota01_aluno = float(input("informe a primeira nota do aluno:"))
    nota02_aluno = float(input("informe a segunda nota do aluno:"))
    nota03_aluno = float(input("informe a terceira nota do aluno:"))

    return cadastrar_aluno(nome_aluno, email_aluno, serie_aluno, nota01_aluno, nota02_aluno, nota03_aluno)

def cadastrar_aluno(aluno, email, serie, nota01=0, nota02=0, nota03=0):

    notas = [nota01, nota02, nota03]

    aluno = {
            "aluno": aluno,
            "email": email,
            "serie": serie,
            "nota": notas,
            "media": calcular_media(notas)
}
    alunos.append(aluno)

    return aluno

def mostrar_dados_alunos(dados_alunos):
    for aluno in dados_alunos:
        print(f"Nome do aluno: {aluno["nome"]} | Email do aluno: {aluno["email"]} | Série do aluno {aluno["serie"]} | Notas do aluno{aluno["notas"]} Média do aluno {aluno["media"]}")
    
    return

def iniciar_sistema():
    while True:
        print("="*80)
        print("Opçao 1 => mostrar lista de alunos cadastrados.")
        print("Opçao 2 => cadastrar aluno.")
        print("Opçao 3 => sair do sistema.")
        print("="*80)
        
        
        opcao = input("escolha uma das opçoes acima:")

        if opcao == 1:
            mostrar_dados_alunos(alunos)
        elif opcao == 2:
            obter_dados_alunos()
        else:
            print("sistema finalizado")
            break

iniciar_sistema()