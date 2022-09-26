# -*- coding: utf-8 -*-

#Escreva umprograma que permaneça em laço dentro do qual será efetuadaa leitura de um número inteiro X. O laço termina quando for digitado o valor 0 (zero) para X. Para cada valor X lido, o programa deve informarna tela se o mesmo é par ou ímpar.

x = 1

while (x != 0):
    x = int(input("Digite um número: "))
    if(x == 0):
        break
    elif(x % 2 == 0):
        print("Esse número é par!")
    else:
        print("Esse número é impar!")
    pass
