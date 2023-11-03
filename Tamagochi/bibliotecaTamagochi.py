class Tamagochi():
    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = float(peso)
        self.comendo = False
        self.falando = False
        self.dormindo = False

    def comer(self):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
        elif self.falando:
            print(f'{self.nome} não pode comer enquanto fala.')
        elif self.dormindo:
            print(f'{self.nome} está dormindo, então não pode comer agora.')
        else:
            print(f'{self.nome} foi comer.')
            self.comendo = True

    def falar(self):
        if self.falando:
            print(f'{self.nome} já está falando!')
        elif self.comendo:
            print(f'{self.nome} está comendo, então não pode falar agora.')
        elif self.dormindo:
            print(f'{self.nome} está dormindo, então não pode falar agora.')
        else:
            print(f'Olá, sou o {self.nome}, tenho {self.peso:.1f} KG e {self.idade} anos.')
            self.falando = True


    def dormir(self):
        if self.falando:
            print(f'{self.nome} está falando, não pode dormir agora.')
        elif self.comendo:
            print(f'{self.nome} está comendo, não pode dormir agora.')
        elif self.dormindo:
            print(f'{self.nome} já está dormindo!')
        else:
            print(f'{self.nome} foi dormir, boa noite.')
            self.dormindo = True

    def pararComer(self):
        if self.comendo:
            print(f'{self.nome} ficou cheio.')
            self.comendo = False
        else:
            print(f'{self.nome} não está comendo.')

    def pararFalar(self):
        if self.falando:
            print(f'{self.nome} parou de falar.')
            self.falando = False
        else:
            print(f'{self.nome} não está falando.')

    def pararDormir(self):
        if self.dormindo:
            print(f'{self.nome} acordou, bom dia!')
            self.dormindo = False
        else:
            print(f'{self.nome} já está acordado.')