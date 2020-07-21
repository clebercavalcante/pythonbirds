class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return 'Olá Mundo'

if __name__ == '__main__':
    p = Pessoa('Cleber', 30)
    print(p.cumprimentar())
    print(p.nome, 'tem', p.idade,'anos')

