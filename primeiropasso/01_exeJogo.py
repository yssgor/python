print("----------------------------------------")
print("Bem vindo ao jogo!")
print("----------------------------------------")

numero_secreto = 25
total_tentativas = 3
rodada = 1

while (rodada <= total_tentativas):
    print("Tentativa {} de {}".format(rodada, total_tentativas))
    chute = int(input("Digite um número: "))
    print("Você digitou ", chute)

    acertou = numero_secreto == chute
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if (acertou):
        print("Você acertou!")
    else:
        if (maior):
            print("Você errou! O seu chute foi maior do que o numero secreto")
        elif (menor):
            print("Você errou! O seu chute foi menor do que o numero secreto")
    rodada = rodada + 1
    pass


print("Fim do jogo!")
