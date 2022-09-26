# -*- coding: UTF-8 -*-

def procurar(nomes):
    print 'Digite o nome a procurar:'
    nome = raw_input()
    if (nome in nomes):
        print "Nome %s esta cadastrado" % (nome)
    else:
        print "Nome %s não esta cadastrado" % (nome)

def alterar(nomes):
    print 'Qual nome você gostaria de alterar?'
    nome_alterar = raw_input()

    if(nome_alterar in nomes):
        posicao = nomes.index(nome_alterar)
        print 'Digite novo nome:'
        nome_novo = raw_input()
        nomes[posicao] = nome_novo

def remover(nomes):
    print 'Qual nome gostaria de remover?'
    nome = raw_input()
    nomes.remove(nome)

def listar(nomes):
    print 'Listando nomes:'
    for nome in nomes:
        print nome

def cadastrar(nomes):
    print 'Digite o nome:'
    nome = raw_input()
    nomes.append(nome)

def menu():
    nomes = []
    escolha = ''
    while escolha != '0':
        print 'Digite: 1 para cadastrar'
        print 'Digite: 2 para listar'
        print 'Digite: 3 para remover'
        print 'Digite: 4 para alterar'
        print 'Digite: 5 para procurar'
        print 'Digite: 0 para sair'
        escolha = raw_input()
        if (escolha == '1'):
            cadastrar(nomes)

        if (escolha == '2'):
            listar(nomes)

        if (escolha == '3'):
            remover(nomes)

        if (escolha == '4'):
            alterar(nomes)

        if (escolha == '5'):
            procurar(nomes)



menu()
