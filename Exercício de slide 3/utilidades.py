# Módulo utilidades.py

def converter_celsius_para_fahrenheit(celsius):
    """Converte uma temperatura em Celsius para Fahrenheit."""
    return (celsius * 9/5) + 32


def validar_senha(senha):
    """
    Valida se a senha tem pelo menos 8 caracteres 
    e contém pelo menos um dígito numérico.
    """
    tem_tamanho_minimo = len(senha) >= 8
    tem_numero = any(caractere.isdigit() for caractere in senha)
    return tem_tamanho_minimo and tem_numero


def calcular_total_caixa(*precos):
    """Recebe uma quantidade variável de preços e calcula a soma total."""
    return sum(precos)