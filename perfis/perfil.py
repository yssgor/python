# -*- coding: UTF-8 -*-
#Objetivo de gerar perfis através da leitura de arquivo.


class Perfil(object):
    """Objetivo de construir perfis"""

    def __init__(self, nome, telefone, empresa):
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa
        self.__curtidas = 0

    @staticmethod
    def imprimir(lista):
        print 'Nome: %s , Telefone: %s , Empresa: %s ' % (nome, telefone, empresa)

    def curtir(self):
        self.__curtidas+=1

    def obter_curtidas(self):
        return self.__curtidas

    @classmethod
    def carregar_arq(classe, nome_arq):
        arq = open(nome_arq, 'r')
        perfis = []
        for linha in arq:
            valores = linha.split(',') #entende o caracter como um separador de valores
            perfis.append(classe(*valores))
        arq.close()
        return perfis


class Perfil_Vip(Perfil): # Novo estilo é só adcionar object no paremetro da classe.
    """Classe padrão para perfis de usuario vips"""

    def __init__(self, nome, telefone, empresa, apelido):
        super(Perfil_Vip, self).__init__(nome, telefone, empresa)
        self.apelido = apelido

    def obter_creditos(self):
        return super(Perfil_Vip, self).__curtidas * 10.0
