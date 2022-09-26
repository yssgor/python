import random

print("----------------------------------------")
print("Bem vindo ao jogo!")
print("----------------------------------------")

numero_secreto = round(random.randrange(1, 100))
total_tentativas = 0

print("Qual nivel de dificuldade: ")
print("Facil (1) Medio (2) Dificil (3)")
nivel = int(input("Digite o nível: "))

if(nivel == 1):
    total_tentativas = 20
elif(nivel == 2):
    total_tentativas = 10
else:
    total_tentativas = 5


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
        print("Você acertou!")
        break
    else:
        if (maior):
            print("Você errou! O seu chute foi maior do que o numero secreto")
        elif (menor):
            print("Você errou! O seu chute foi menor do que o numero secreto")
    pass


print("Fim do jogo!")
