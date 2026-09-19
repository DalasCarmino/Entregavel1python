nota1 = int(input("Digite a primeira nota: ")) # Solicitação das notas do usuário
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))

#Cálculo da media de todas as notas
media = (nota1 + nota2 + nota3) / 3 
print(f"Sua nota foi {media: .2f}")

#Resultados e prints:
if media >= 7:
    print("Você passou")
else:
    print("Você foi reprovado")