produto = int(input("Valor do produto:"))
pagamento = int(input("Valor do pagamento:")) #Da linha 1 a 2, estará colocando os valore numéricos 

if pagamento >= produto: 
    troco = pagamento - produto
    print(f"O troco será {troco} R$") #Cálculo do troco

    if troco == 0:
        print("O produto foi pago com sucesso, não é necessário troco") #Mensagem para dizer que a compra não precisa de troco

elif pagamento < produto:
    print("Pagamento insuficiente. Compra inválida") #Mensagem para compra inválida