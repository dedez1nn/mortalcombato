import pygame
import sys
from fisica import Fisica
from carregar_sprites import Sprites
from estado_animacoes import Estados
from personagem_base import PersonagemBase

class Inimigo1(PersonagemBase):
    def __init__(self, nome: str, listar: list, x: int, y: int):
        super().__init__(nome, listar, x, y)
        self.__tempo_recuo = 0
        self.__recua = False

    @property
    def tempo_recuo(self):
        return self.__tempo_recuo
    
    @tempo_recuo.setter
    def tempo_recuo(self, val: int):
        self.__tempo_recuo = val
        
    @property
    def recua(self):
        return self.__recua
    
    @recua.setter
    def recua(self, val: bool):
        self.__recua = val

        
    def actions(self, superficie, altura, largura, alvo):
        tempo_atual = pygame.time.get_ticks()

        if self.retangulo.right >= largura:
            self.retangulo.right = largura
        elif self.retangulo.x <= 0:
            self.retangulo.x = 0

        if self.retangulo.x < alvo.retangulo.x:
            self.flip = False
            distanciaplayer = self.retangulo.right - alvo.retangulo.left
            deslocamento = 2
        else:
            self.flip = True
            distanciaplayer = self.retangulo.left - alvo.retangulo.right
            deslocamento = -2

        if not (self.estados.atingido or self.estados.soco or self.estados.pulando):
            if self.recua:
                if tempo_atual - self.tempo_recuo < 500:  # recuar por 0.5 segundos
                    self.retangulo.x -= deslocamento  # move na direção oposta
                    self.estados.andando = True
                else:
                    self.recua = False  # terminou de recuar

            elif distanciaplayer > 0 and not self.retangulo.colliderect(alvo.retangulo):
                self.retangulo.x += deslocamento
                self.estados.andando = True

            else:
                self.recua = True
                self.tempo_recuo = tempo_atual
                self.estados.andando = True

        self.atualizar_animacao(superficie, alvo)
        self.estados.resetar_estados()
        
