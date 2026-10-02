def ficha_aluno(nome , **dados):
    print(f"--- FICHA DO ALUNO: {nome.upper()} ---")

    #Percorra cada par chave/valor recebido
    for chave, valor in dados.items():
        #Formata a chave para ficar legível (ex: 'data_nascimento' vira 'Data Nascimento')
        campo_formatado  = chave.replace("_", " ").title()
        print(f"{campo_formatado}: {valor}")

#Exemplo de Uso

ficha_aluno(

    "Maria Silva",
    idade = 19,
    turma = "3 Ano B",
    matricula = 202429,
    cidade = "São Paulo",
    status = "Ativo"
)