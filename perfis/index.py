# -*- coding: UTF-8 -*-

#Bem vindo ao programa de gerar perfis
import config


print("\n\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@ BEM VINDO AO CRIAR PERFIL @@@@")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\n")

def opcao():
    print("Escolha uma das opções a baixo: ")
    print("0 - Gerar um novo arquivo date")
    print("1 - Carregar date para o sistema")
    print("2 - Listar todos os perfis do sistema")
    print("3 - Adicionar novo perfil")
    print("X - sair da aplicação")

    op = raw_input()
    if (op == '0'):
        resp = config.arq.nome_arq()
        try:
            if (resp == 's'):
                config.arq.gerar_arq_inicial()
            pass
        except (resp != 's' or resp != 'n') as e:
            print("Resposta incorreta!")
            raise
        opcao()

    if (op == '1'):
        perfil = config.perfil.Perfil.carregar_arq(config.arq.arq_nome)
        print(perfil)
        #config.perfil.Perfil.imprimir(perfil)


    if (op == 'X' or op == 'x'):
        exit()

opcao()
