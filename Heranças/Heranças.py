class Animal():
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor
    def comer(self):
        print(f'O {self.nome} foi comer. ')
    def emitirSom(self):
        print(f'O {self.nome} emitiu som.')

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def emitirSom(self):
        print(f'O {self.nome} miou.')

class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def emitirSom(self):
        print(f'O {self.nome} latiu.')

class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def emitirSom(self):
        print(f'A {self.nome} mugiu.')

class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def emitirSom(self):
        print(f'O {self.nome} ronronou.')

class Forma():
    def __init__(self):
        self.area = 0
        self.perimetro = 0

class Triângulo(Forma):
    def __init__(self, lado):
        super().__init__(area, perimetro)
        self.lado = lado

    def calculaArea(self):
        self.area = (self.lado * self.lado) / 2
        print(f'A área do triângulo é: {self.area}')

    def calculaPerimetro(self):
        self.perimetro = self.lado * 3
        print(f'O perímetro do triângulo é: {self.area}')

class Retangulo(Forma):
    def __init__(self, altura, base):
        super().__init__()
        self.altura = altura
        self.base = base

    def calculaArea(self):
        self.area = self.base * self.altura
        print(f'A área do retângulo é: {self.area}')

    def calculaPerimetro(self):
        self.perimetro = 2 * (self.base + self.altura)
        print(f'O perímetro do retângulo é: {self.area}')