# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 14:18:43 2020
Refaça o exercício anterior armazenando cada um dos valores válidos (dentro do intervalo[Min, Max]) em um vetorde números inteiros.Apresente na tela todos os valores contidos no vetor, bem como o total e a quantidade correta de valores fornecidos.
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
    
v = []
soma = 0
total = 0
x = 1
while (x != 0):
    x = int(input("Digite um valor: "))
    if (x >= min and x <= max):
        v.append(x)
        soma += x
        total += 1
    else:
        print("Valor fora do intervalo [%d, %d], ignorado na totalização." % (min, max))    
    pass

print("Os valores são:".v)
print("A soma dos números: {} e o total digitado: {}".format(soma, total))
