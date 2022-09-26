# -*- coding: utf-8 -*-
"""
Criando a classe do conceito POO em python
@author: Gor
"""

class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("construindo objeto... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo #atributos
        self.__limite = limite  # os dois undescor coloca o atributo como privado
    
    def extrato(self): #metodo
        print("Saldo {} do titular {} da conta {}".format(self.__saldo, self.__titular, self.__numero))
    
    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_sacar
    
    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    def transfere(self, valor, destino):
        self.saca(valor) # self é a conta origem
        destino.deposita(valor)

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular
    
    @property
    def limite(self): # vai retornar o valor do limite
        return self.__limite

    @limite.setter
    def limite(self, limite): #vai dar um set no limite
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"
    
    pass

