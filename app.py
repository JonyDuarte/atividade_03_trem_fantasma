'''Crie um programa que controle a entrada de usuários no brinquedo "Trem Fantasma"
 de um parque de diversões. O programa só deve autorizar a entrada de usuários que 
 possuam mais de 10 anos de idade e menos de 150kg de peso. 
 Ao terminar, envi para o GitHub'''

# Entrada de dados do usuário
idade = int(input("Informe sua idade: "))
peso = float(input("Informe seu peso atual: "))

# Autorização com base nas informações
if idade >= 10 and peso < 150:
    print(f"Entrada liberada.")
elif idade < 10:
    print(f"Não autorizada entrada de menores de 10 anos.")
elif peso < 150:
    print(f"Entrada autorizada.")
else:
    print(f"Não autorizada entrada a partir de 150 kg.")