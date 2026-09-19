segundos_totais = int(input("Digite o tempo em segundos: ")) # Solicita o valor em segundos ao usuário

# Calculando horas, minutos e segundos
horas = segundos_totais // 3600 
restos_segundos = segundos_totais % 3600

minutos = restos_segundos // 60
segundos = restos_segundos % 60

# Exibindo o resultado formatado
print(f"{segundos_totais} segundos equivalem a: {horas}h {minutos}m {segundos}s")