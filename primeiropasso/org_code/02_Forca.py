import random
'''
Jogo da forca
'''

def jogar_forca():
    
    imprime_bemVindo()

    palavra_secreta = carregaPalavraSecreta()
    
    # Informando as palavras secretas
    #letrasAcertadas = ["_" for letra in palavra_secreta] (versão antiga)

    letrasAcertadas = inicializar_palavraAcertada(palavra_secreta)
    print(letrasAcertadas)

    enforcou = False
    acertou = False
    erros = 0

    #Enquanto não tiver enforcado e enquanto não tiver acertado (True)
    while(not enforcou and not acertou):

        chute = pedeChute()

        if(chute in palavra_secreta):
            insereChute(chute, letrasAcertadas, palavra_secreta)
        else:
            erros += 1
        
        #Alterando os valores da variaveis enforcou e acertou (bool)
        enforcou = erros == 6 # Se erros forem iguais a 6 a variavel enforcou = True
        acertou = "_" not in letrasAcertadas # Se não tiver underscor na lista de letrasAcertadas será True

        print(letrasAcertadas)

    
    if(acertou):
        print("Você ganhou!!")
    else:
        print("Você perdeu!")


def imprime_bemVindo():
    print("----------------------------------------")
    print("Bem vindo ao jogo!")
    print("----------------------------------------")

def carregaPalvraSecreta():
    # Buscando nos arquivos as palavras para a caça palavras.
    arquivo = open("palavra.txt", "r")
    palavra = []
    for linha in arquivo:
        linha = linha.strip()
        palavra.append(linha)
    arquivo.close()
    
    # Randomizar e atribuir a palavra secreta
    numero = random.randrange(0,len(palavra))
    palavra_secreta = palavra[numero].upper()
    return palavra_secreta

def inicializar_palavraAcertada(palavra):
    return ["_" for letra in palavra]

def pedeChute():
    chute = input("Qual letra?")
    chute = chute.strip().upper()
    return chute

def insereChute(chute, letrasAcertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        # Se o caracter chute estiver no caracter letra que esta na palavra, então adiciona na lista letra acertada.
        if(chute == letra):
            letrasAcertadas[index] = letra
                     
        index = index + 1

# Condição para saber se o main esta nesse arquivo ou não.
if (__name__ == "__main__"):
    jogar_forca()