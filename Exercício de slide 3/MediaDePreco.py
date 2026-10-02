def fun(*preco):
    total = sum(preco)
    media = sum(preco) / len(preco)
    mais_caro = max(preco)
    return total, media, mais_caro

print(fun(25.5, 7, 10))

