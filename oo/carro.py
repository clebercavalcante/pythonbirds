class Carro:
    def __init__(self, motor, direcao):
        self.motor = motor
        self.direcao = direcao

    def calcular_velocidade(self):
        return self.motor.velocidade

    def calcular_direcao(self):
        return self.direcao.valor

    def acelerar(self):
        return self.motor.acelerar()

    def frear(self):
        return self.motor.frear()

    def girar_a_esquerda(self):
        return self.direcao.girar_a_esquerda()

    def girar_a_direita(self):
        return self.direcao.girar_a_direta()

class Motor:
    def __init__(self, velocidade=0):
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade = self.velocidade - 2
        if self.velocidade < 0:
            self.velocidade = 0

class Direcao:
    def __init__(self, direcao= 'NORTE'):
        self.valor = direcao

    def girar_a_direta(self):
         if self.valor == 'NORTE':
             self.valor = 'LESTE'
         elif self.valor == 'LESTE':
             self.valor = 'SUL'
         elif self.valor == 'SUL':
             self.valor = 'OESTE'
         elif self.valor == 'OESTE':
             self.valor = 'NORTE'
         else:
             print('Direção informada não faz parte dos valores padrões (N,L,S,O)')

    def girar_a_esquerda(self):
         if self.valor == 'NORTE':
             self.valor = 'OESTE'
         elif self.valor == 'OESTE':
             self.valor = 'SUL'
         elif self.valor == 'SUL':
             self.valor = 'LESTE'
         elif self.valor == 'LESTE':
             self.valor = 'NORTE'
         else:
             print('Direção informada não faz parte dos valores padrões (N,L,S,O)')


if __name__ == '__main__':
    "Testando Motor"
    print('Testando Motor')
    motor = Motor()
    print(motor.velocidade)
    motor.acelerar()
    print(motor.velocidade)
    motor.acelerar()
    print(motor.velocidade)
    motor.acelerar()
    print(motor.velocidade)
    motor.frear()
    print(motor.velocidade)
    motor.frear()
    print(motor.velocidade)
    motor.frear()
    print(motor.velocidade)

    "Testando Direção"
    print('Testando Direcao')
    direcao = Direcao()
    print(direcao.valor)
    direcao.girar_a_direta()
    print(direcao.valor)
    direcao.girar_a_direta()
    print(direcao.valor)
    direcao.girar_a_direta()
    print(direcao.valor)
    direcao.girar_a_direta()
    print(direcao.valor)
    direcao.girar_a_esquerda()
    print(direcao.valor)
    direcao.girar_a_esquerda()
    print(direcao.valor)
    direcao.girar_a_esquerda()
    print(direcao.valor)
    direcao.girar_a_esquerda()
    print(direcao.valor)


    "Testando Carro"
    print('Testando Carro')
    carro = Carro(motor, direcao)
    print(carro.calcular_direcao())
    print(carro.calcular_velocidade())
    carro.girar_a_esquerda()
    carro.acelerar()
    print(carro.calcular_direcao())
    print(carro.calcular_velocidade())
    carro.girar_a_esquerda()
    carro.acelerar()
    print(carro.calcular_direcao())
    print(carro.calcular_velocidade())
    carro.girar_a_direita()
    carro.frear()
    print(carro.calcular_direcao())
    print(carro.calcular_velocidade())