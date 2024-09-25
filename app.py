# Entrada de dados do usuário
idade = int(input("Informe sua idade: "))
peso = float(input("Informe seu peso atual: "))

# Autorização de entrada com base nas informações
if idade >= 10 and peso < 150:
    print(f"Entrada autorizada.")
elif idade < 10:
    print(f"Não autorizada entrada de menores de 10 anos.")
elif peso < 150:
    print(f"Entrada autorizada.")
else:
    print(f"Não autorizada entrada a partir de 150 kg.")