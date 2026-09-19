Nome = int(input("Digite seu nome: "))
A = int(input("Digite sua primeira nota: "))
B = int(input("Digite sua segunda nota: "))
C = int(input("Digite sua terceira nota: "))


Média = (A + B + C) / 3

if Média >= 7:
    print(f"Você tirou {Média: .2f}. Parabéns,{Nome} você passou de ano")
elif Média < 7:
    print (f"Infelizmente você não atingiu a média necessária para passar, tirando {Média: .2f}")