def reg (nota, boletim=None):  #Difinição do do boletim
    """Não altera a lista original"""
    if boletim is None:
        boletim = []
    novo = boletim[:] #copia
    novo.append (nota)
    return novo

notas = [7]
print(reg(9, notas))
print(notas)