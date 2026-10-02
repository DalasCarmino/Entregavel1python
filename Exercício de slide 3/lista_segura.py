# Script principal que importa e reutiliza o módulo utilidades
import utilidades

print("=== DEMONSTRAÇÃO DO MÓDULO UTILIDADES ===\n")

# 1. Testando o Conversor de Temperatura
temp_c = 25.0
temp_f = utilidades.converter_celsius_para_fahrenheit(temp_c)
print(f"1. Temperatura: {temp_c}°C equivale a {temp_f}°F")

# 2. Testando o Validador de Senha
senhas_teste = ["12345", "senhaInvalida", "Python2026"]
print("\n2. Validação de Senhas:")
for senha in senhas_teste:
    valida = utilidades.validar_senha(senha)
    status = "VÁLIDA" if valida else "INVÁLIDA"
    print(f"   - Senha '{senha}': {status}")

# 3. Testando a Função de Caixa (*precos)
total = utilidades.calcular_total_caixa(15.50, 42.00, 8.25, 120.00)
print(f"\n3. Total das compras no caixa: R$ {total:.2f}")