# -*- coding: utf-8 -*-
jogo_01 = __import__('01_Jogo')
jogo_02 = __import__('02_Forca')
print("----------------------------------------")
print("Bem vindo ao jogo!")
print("----------------------------------------")

print("Adivinhação (1) Forca (2)")

jogo = int(input("Qual jogo? "))

if (jogo == 1):
    print("Jogando Adivinhação")
    jogo_01.jogar_advinhacao()
elif(jogo == 2):
    print("Jogando Forca")
    jogo_02.jogar_forca()
