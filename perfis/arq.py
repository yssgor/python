# -*- coding: UTF-8 -*-
#Gera e atualizar arquivo date perfis

arq_nome = ''

def nome_arq():
    global arq_nome
    arq_nome = raw_input("Nome do arquivo: ")
    resp = raw_input("Deseja cadastrar? ")
    return resp


def gerar_arq_inicial():
    global arq_nome
    arq = open(arq_nome, 'w')
    qtd = int(raw_input("Quantos usuarios deseja criar? "))

    for x in range(qtd):
        nome = raw_input("Digite o nome do perfil: ")
        telefone = raw_input("Digite o telefone: ")
        empresa = raw_input("Digite a empresa: ")
        arq.write("{},{},{}\n".format(nome, telefone, empresa))
        pass
    arq.close()
    return "Arquivo gerado!"
