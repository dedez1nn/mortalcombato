import pygame
import sys
from fisica import Fisica
from carregar_sprites import Sprites
from estado_animacoes import Estados
from personagem_base import PersonagemBase

class Inimigo(PersonagemBase):
     def __init__(self, nome: str, listar: list, x: int, y: int):
        super().__init__(nome, listar, x, y)
        self.__cooldownd = 0
        self.__cooldown_block = 0
        
     @property
     def cooldownd(self):
        return self.__cooldownd
    
     @cooldownd.setter
     def cooldownd(self, val: int):
        self.__cooldownd = val 
        
     @property
     def cooldown_block(self):
        return self.__cooldown_block
    
     @cooldown_block.setter
     def cooldown_block(self, val: int):
        self.__cooldown_block = val 
        
     def actions(self, superficie, altura, largura, alvo):
        deslocamento = 0
            
        if self.retangulo.x > alvo.retangulo.x:
            self.flip = True
            deslocamento = -2
        else:
            self.flip = False
            deslocamento = 2
        
        if self.estados.atingido:
            self.retangulo.x += -(deslocamento * 2.5)
            
        if self.retangulo.x <= 0:
            self.retangulo.x = 0
            self.estados.andando = False
        if self.retangulo.right >= largura:
            self.retangulo.right = largura
            self.estados.andando = False

        if not self.estados.atingido and not self.estados.soco and not self.estados.pulando:
            if self.retangulo.colliderect(alvo.retangulo) and self.__cooldownd == 0:    
                if self.ataquecdr == 0:
                    self.estados.soco = True         
                    self.estados.andando = False 
                    self.cooldownd = 40             
            elif self.cooldownd > 0:
                if not self.estados.defesa:
                    self.retangulo.x += -deslocamento * (1/2)    
                    self.estados.andando = True      
                if self.cooldownd <= 10 and self.cooldown_block == 0:
                    self.estados.defesa = True                    
            else:
                if not self.estados.defesa and not self.retangulo.colliderect(alvo.retangulo):
                    self.estados.andando = True              
                    self.retangulo.x += deslocamento
            
        if self.ataquecdr > 0:
            self.ataquecdr -= 0.25
        if self.__cooldownd > 0:
            self.__cooldownd -= 0.25
        if self.__cooldown_block > 0:
            self.__cooldown_block -= 0.25
            

        self.atualizar_animacao(superficie, alvo, 60) #superficie, player, cdratk
        self.estados.resetar_estados()
        
