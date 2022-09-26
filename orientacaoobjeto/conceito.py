# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 18:47:19 2020
Isso é um exemplo processual de progamação, fazendo a ligação com poo.
@author: Gor
"""


def cria_conta (numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def deposita (conta, valor):
    conta["saldo"] += valor

def saca (conta, valor):
    conta["saldo"] -= valor

def extrato (conta):
    print("Saldo é {}".format(conta["saldo"]))    