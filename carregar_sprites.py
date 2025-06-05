import pygame

class Sprites:
    def __init__(self, nome: str, numanim: list):
        self.__sprites = {}
        self.__listanm = numanim
        self.__nomep = nome
        self.sprite_atual = 0.0  # Mantido como float para controle fino

    @property
    def nomep(self):
        return self.__nomep

    @nomep.setter
    def nomep(self, novo: str):
        self.__nomep = novo

    def addsprites(self):
        for i in range(len(self.__listanm)):
            for j in range(self.__listanm[i]):
                temp = pygame.image.load(f'{self.nomep}/{i}/{j}.png').convert_alpha()
                temp = pygame.transform.scale(temp, (150, 150))
                self.__sprites[(i, j)] = temp

    def percorrer(self, indice: int):
        # Diminui a velocidade da animação ajustando a taxa de avanço
        self.sprite_atual += 0.1  # quanto menor, mais lenta
        if self.sprite_atual >= self.__listanm[indice]:
            self.sprite_atual = 0
        temp = self.__sprites[(indice, int(self.sprite_atual))]
        return temp
