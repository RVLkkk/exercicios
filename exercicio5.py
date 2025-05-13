from exercicio4 import calcular_media

def cadastrar_aluno(aluno, email, serie, nota01=0, nota02=0, nota03=0):
    alunos = []

    notas = [nota01, nota02, nota03]

    aluno = {
            "aluno": aluno,
            "email": email,
            "serie": serie,
            "nota": notas,
            "media": calcular_media(notas)
}
    alunos.append(aluno)
    media = calcular_media()
    return aluno

print(cadastrar_aluno("ygor", "reivulgoliso@gmail.com", "2° TB",7, 9,6))        