# # # inteiro 

# # a = 1
# # b = -1

# # # float ou reais

# # a1 = 1.5
# # a2 = 2.58239

# # #  string ou linha
# # c = "text here"
# # d = 'text here'

# # # boolean ou lógico 

# # e = True 
# # f = False 

# # # list/array ou listas

# # g = [1, 2, 3, 4, 5, 7]
# # g1 = ["kadu", 16, True]

# # # dict ou dicionário 

# # h = {
# #     "nome": "kadu",
# #     "idade": "16",
# #     "solteiro": True   
# # }

# # # tuples ou tupla 

# # i = (1, 2, 4, 8)

# # Requerimentos 

# # O programa tem que pedir a nome do usuario
# # O programa teme que perguntar a idade do usuario
# # O programa tem que imprimir uma frase constando: O nome, a Idade, e se o usuario é maior ou menor de idade 

# nome = ""
# idade = "0"
# fator = ""


# nome = input("Qual é o seu nome: ")
# idade = input("Quantos anos você tem: ")

# if int(idade) < 18:
#     fator = "menor"
# else:
#     fator = "maior "


# print("Ola " + nome +", a sua idade é " + idade + " anos e voce é " + fator + " de idade")


# Requerimentos
# Ler a opção do usuario (pedra, papel, tesoura)
# sortear uma opção para o computador 
# imprimir quem ganhou 

import random

opções = ["pedra", "papel", "tesoura"]

jogada = input("escolha uma opção ('pedra', 'papel', 'tesoura') ou sair: ")

while jogada != "pedra" and jogada != "papel" and jogada != "tesoura" and jogada != "sair":
        jogada = input("por favor escolha uma destas opções: pedra, papel ou tesoura ou sair: ")

ganhador = "" 

while jogada != "sair":
    
    computador = random.choice(opções)
    
    if computador == "pedra":
        if jogada == "tesoura":
            ganhador = "computador"
        elif jogada == "papel": 
            ganhador = "usuario"
        else:
            ganhador = "empate"

    elif computador == "tesoura":
        if jogada == "tesoura":
            ganhador = "empate"
        elif jogada == "papel": 
            ganhador = "computador"
        else:
            ganhador = "usuario"

    elif computador == "papel":
        if jogada == "tesoura":
            ganhador = "usuario"
        elif jogada == "papel": 
            ganhador = "empate"
        else:
            ganhador = "computador"       
    print(f"Você escolheu {jogada}, o computador escolheu {computador}. O resultado foi: {ganhador}")
    jogada = input("escolha uma opção ('pedra', 'papel', 'tesoura') ou sair: ")
    while jogada != "pedra" and jogada != "papel" and jogada != "tesoura" and jogada != "sair":
        jogada = input("por favor escolha uma destas opções: pedra, papel ou tesoura ou sair: ")

