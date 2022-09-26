# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 13:37:53 2020
Escreva um programa que leia dois números inteiros denominados Min e Max. Em seguida, inicie um laço dentro do qual será efetuadaa leitura de um número inteiro X. O laço termina quando for digitado o valor 0 (zero) para X. Dentro do laço oprograma deve totalizar todos os valores de Xque estejam no intervalo fechado [Min,Max], bem como contá-los.Se algum valor fora dointervalofor digitado para X, o programa deve dar a mensagem "Valor fora dointervalo [Min, Max]ignorado na totalização". Apóssair do laço, deve apresentar o total e a quantidade correta de valores fornecidos.Cuidado com a possibilidade do usuário digitar o valor Min maior que o valor Max. Se isso acontecer o programa deve avisar a situação e invertê-los.
@author: Gor
"""

x = 0
min = int(input("Digite o valor minimo: "))
max = int(input("Digite o valor máximo: "))
if (min > max):
    print("Minimo é maior que máximo, invertendo os valores")
    x = max
    max = min
    min = x
    

soma = 0
total = 0
x = 1
while (x != 0):
    x = int(input("Digite um valor: "))
    if (x >= min and x <= max):
        soma += x
        total += 1
    else:
        print("Valor fora do intervalo [%d, %d], ignorado na totalização." % (min, max))    
    pass

print("A soma dos números: {} e o total digitado: {}".format(soma, total))

