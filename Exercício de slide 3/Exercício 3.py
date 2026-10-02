def total (*preços, desc = 0):
    s = sum(preços)
    return s * (1 - desc / 100)  #Configuração do cálculo

print (total(10, 25.5, 7))

print (total (10, 25.5, 7, desc = 10)) #Imprimindo o resultado