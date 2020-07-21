class Pessoa:
    def __init__(self, *filhos, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return 'Olá Mundo'

if __name__ == '__main__':
    filho = Pessoa(nome='Enzo',idade= 8)
    pai = Pessoa(filho, nome='Cleber', idade=30)
    print(pai.cumprimentar())
    print(pai.nome, 'tem', pai.idade,'anos')
    for lista_filho in pai.filhos:
        print('O filho de', pai.nome, 'se chama', lista_filho.nome, 'e tem', lista_filho.idade, 'anos de idade')

