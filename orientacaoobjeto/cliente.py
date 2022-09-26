class Cliente:
    
    def __init__(self, nome):
        self.__nome = nome

    @property # diz que o método uma propriedade da classe (para funcionar o atributo tem que ser privado)
    def nome(self):
        return self.__nome.title()

    @nome.setter # isso diz que o set do atributo para um sintase simples como uma propriedade da classe
    def nome(self, nome):
        self.__nome = nome

    pass