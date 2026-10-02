from calculadora import somar, multiplicar  #comando para importar as operações da calculadora

def orc (qtd, preco, frete = 0): #definindo o preço
    """Total do pedido."""
    s = multiplicar (qtd, preco)
    return somar(s, frete)

print(orc(3, 49.9, 15)) #resultado