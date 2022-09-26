# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 13:17:26 2020

Escreva umprograma que permaneça em laço dentro do qual será efetuadaa leitura de um número inteiro X. O laço termina quando for digitado o valor 0 (zero) para X. Dentro do laço oprograma deve totalizar todos os valores de Xmaiores quezero, bem como contá-los.Se algum valor negativo for digitado para X, o programa deve dar a mensagem "Valor negativo ignorado na totalização". Apóssair do laço, deve apresentar o total e a quantidade correta de valores fornecidos.

@author: Gor
"""

x = 1
soma = 0
total = 0

while (x != 0):
    x = int(input("Digite um valor: "))
    if (x >= 0):
        soma += x
        total += 1
    else:
        print("Valor negativo ignorado na totalização.")    
    pass

print("A soma dos números: {} e o total digitado: {}".format(soma, total))
