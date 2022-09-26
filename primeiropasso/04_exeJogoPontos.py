'''
Jogo para acertar um número gerado randomicamente.
O jogador tem X números de alternativas que varia a parti do nivel de difuculdade.
'''

import random

print("----------------------------------------")
print("Bem vindo ao jogo!")
print("----------------------------------------")

'''
Declarações de variaveis:
'''
numero_secreto = round(random.randrange(1, 100))
total_tentativas = 0
pontos = 1000

'''
Nivel de dificuldade:
'''
print("Qual nivel de dificuldade: ")
print("Facil (1) Medio (2) Dificil (3)")
nivel = int(input("Digite o nível: "))

if(nivel == 1):
    total_tentativas = 20
elif(nivel == 2):
    total_tentativas = 10
else:
    total_tentativas = 5

'''
Tentativas e acertos:
'''
for rodada in range(1, total_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_tentativas))
    chute = int(input("Digite um número: "))
    print("Você digitou ", chute)

    if(chute < 1 or chute > 100):
        print("Digite um número entre 1 e 100")
        continue #essa função para uma das interações do laço e não sai do laço.

    acertou = numero_secreto == chute
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if (acertou):
        print("Você acertou e fez {} pontos!".format(pontos))
        break
    else:
        if (maior):
            print("Você errou! O seu chute foi maior do que o numero secreto")
        elif (menor):
            print("Você errou! O seu chute foi menor do que o numero secreto")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos
    pass


print("Fim do jogo!")
