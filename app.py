# Entrada de dados do usuário
idade = int(input("Informe sua idade: "))
peso = float(input("Informe seu peso atual: "))

# Autorização de entrada com base nas informações
if idade >= 10 and peso < 150:
    print(f"Entrada autorizada.")
else:
    print(f"Entrada não autorizada.")