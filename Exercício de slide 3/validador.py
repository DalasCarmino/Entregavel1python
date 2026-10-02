def validador(senha):
    return len(senha) >= 8 #Difinindo a senha

print(validador("AAAAAAAAAAAAAAA")) #Testando a senha
print(validador("AAAAAA"))