preco_inicial = int(input("Digite o valor do produto: ")) #Solicitação dos valores:
desconto = int(input("Digite os desconto (em %): "))

# Cálculo do desconto:
preco_final = preco_inicial * desconto / 100

# Resultado:
print(f"O valor resultará em {preco_final}")