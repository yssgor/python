class Filme:
    def __init__(self, nome, ano, duracao):
        self.nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.likes = 0
    
    def dar_like(self):
        self.like += 1

class Serie:
    def __init__(self, nome, ano, temporada):
        self.nome = nome.title()
        self.ano = ano
        self.temporada = temporada
        self.likes = 0
    
    def dar_like(self):
        self.like += 1


vingadores = Filme ('vingadores - guerra infinita', 2018, 160)
vingadores.dar_like()
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração:{vingadores.duracao} - Likes: {vingadores.likes}')

atlanta = Serie ('atlanta', 2018, 2)


atlanta.dar_like()
atlanta.dar_like()
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas:{atlanta.temporada} - Likes: {atlanta.likes}')