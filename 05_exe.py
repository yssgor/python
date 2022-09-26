# -*- coding: utf-8 -*-

#Escreva umprograma que permaneça em laço dentro do qual será efetuadaa leitura de um número inteiro X. O laço termina quando for digitado o valor 0 (zero) para X. Dentro do laço oprograma deve totalizar todos os valores de X, bem como contar quantos valores foram digitados. Apóssair do laço, deve apresentar o total e a quantidade correta de valores fornecidos.

x = 1
soma = 0
total = 0

while (x != 0):
    x = int(input("Digite um valor: "))
    soma += x
    total += 1
    pass

print("A soma dos números: {} e o total digitado: {}".format(soma, total))
