import pygame

class Fisica:
    def __init__(self):
        self.__vel_y = 0
        self.__gravidade = 1
        self.__altura_pulo = 20
        self.__pulo = False
        self.__velocidade = 5

    @property
    def velocidade(self):
        return self.__velocidade
    
    @velocidade.setter
    def velocidade(self, val: int):
        self.__velocidade = val
        
    @property
    def pulo(self):
        return self.__pulo

    @pulo.setter
    def pulo(self, valor: bool):
        self.__pulo = valor

    @property
    def vel_y(self):
        return self.__vel_y

    @vel_y.setter
    def vel_y(self, valor: float):
        self.__vel_y = valor

    @property
    def gravidade(self):
        return self.__gravidade

    @gravidade.setter
    def gravidade(self, valor: float):
        self.__gravidade = valor

    @property
    def altura_pulo(self):
        return self.__altura_pulo

    @altura_pulo.setter
    def altura_pulo(self, valor: float):
        self.__altura_pulo = valor

    def aplicar_gravidade(self, y, limite_chao):
        if self.__pulo:
            y += self.vel_y
            self.vel_y += self.gravidade

            if y >= limite_chao:
                y = limite_chao
                self.__pulo = False
                self.__vel_y = 0

        return y

    def iniciar_pulo(self):
        self.__pulo = True
        self.__vel_y = -self.__altura_pulo
            
