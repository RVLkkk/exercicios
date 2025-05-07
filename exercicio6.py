def cadastrar_filme(nome_filme, descricao, classificacao, categoria01, categoria02, categoria03):
    dados_filme = []
    filme = {
        "filme": filme,
        "descricao": descricao,
        "classificacao": classificacao,
        "categoria01": categoria01,
        "categoria02": categoria02,
        "categoria": categoria03
}
    dados_filme.append(filme)
    return dados_filme 

print(cadastrar_filme("minecraft", "descriçao", "10", "açao", "aventura", "comedia" ))