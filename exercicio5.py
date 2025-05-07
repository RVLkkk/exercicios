def cadastrar_aluno(aluno, email, serie):
    alunos = []

    aluno = {
            "aluno": aluno,
            "email": email,
            "serie": serie
}
    alunos.append(aluno)
    return aluno

print(cadastrar_aluno("ygor", "reivulgoliso@gmail.com", "2° TB",7, 9,6))