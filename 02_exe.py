# -*- coding: utf-8 -*-

#Escreva um programa que leia dois números inteiros e apresente na tela sua soma apenas se ambos tiverem o mesmo sinal (positivo ou negativo). Use o mesmo formato do exercício anterior e, caso os números fornecidos tenham sinais trocadoso programa deve escrever na tela que os "Dados de Entrada são Inválidos".


x = int(input("Digite o primeiro número: "))

y = int(input("Digite o segundo número: "))

if ((x >= 0 and y >= 0) or (x <= 0 and y <= 0)):
    soma = x + y
    print ("Soma de {} com {} = {}".format(x, y, soma))
else:
    print("Dados de entrada são invalidos")
