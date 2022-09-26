# -*- coding: utf-8 -*-

#Escreva um programa que permaneça em laço dentro do qual será efetuadaa leitura de um número inteiro X. O laço termina quando for digitado o valor 0 (zero) para X. Para cada valor X lido, o programa deve informarna tela se o mesmo é positivo ou negativo.

x = 1

while (x != 0):
    x = int(input("Digite um número: "))
    if(x > 0):
        print("Esse número é positivo!")
    elif(x == 0):
        break
    else:
        print("Esse número é negativo!")
    pass
