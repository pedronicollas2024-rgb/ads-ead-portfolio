# Calculadora de Gorjeta
# Solicita o valor da conta e a porcentagem de gorjeta desejada,
# e exibe o valor da gorjeta e o total final a pagar.

Valor = float(input("O valor da conta é: "))
porcentagem = int(input("Deseja colocar uma porcentagem na gorjeta? "))
Gorjeta = Valor * (porcentagem / 100)
Final = Valor + Gorjeta

print(f"O valor da conta é {Valor}, a gorjeta é {Gorjeta} e o valor final fica {Final}")