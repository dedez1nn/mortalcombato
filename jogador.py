import pygame
import sys
from fisica import Fisica
from carregar_sprites import Sprites
from estado_animacoes import Estados
from personagem_base import PersonagemBase

class Jogador(PersonagemBase):
    def __init__(self, nome: str, listar: list, x: int, y: int):
        super().__init__(nome, listar, x, y)
        
            
    
    def actions(self, superficie, altura, largura, alvo):
        teclas = pygame.key.get_pressed()
        
        
        
        if self.retangulo.centerx > alvo.retangulo.centerx:
            self.flip = True
            deslocamento = 5
        else:
            self.flip = False
            deslocamento = -5
            
        if self.estados.atingido:
            self.retangulo.x += deslocamento
            
        if self.retangulo.x <= 0:
            self.retangulo.x = 0
        elif self.retangulo.right >= largura:
            self.retangulo.right = largura
        #movimentos player 1
        if not self.estados.atingido and not self.estados.soco and not self.estados.defesa:
                if teclas[pygame.K_a]:
                    nova_x = self.retangulo.x - 5
                    ret_temp = self.retangulo.copy()
                    ret_temp.x = nova_x
                    if nova_x >= 0 and not ret_temp.colliderect(alvo.retangulo):
                        self.retangulo.x = nova_x
                    self.estados.andando = True

                if teclas[pygame.K_d]:
                    nova_x = self.retangulo.x + 5
                    ret_temp = self.retangulo.copy()
                    ret_temp.x = nova_x
                    if nova_x + self.retangulo.width <= largura and not ret_temp.colliderect(alvo.retangulo):
                        self.retangulo.x = nova_x
                    self.estados.andando = True

                if teclas[pygame.K_w] and not self.fisica.pulo and self.retangulo.y == altura - self.retangulo.height:
                    self.fisica.iniciar_pulo()
                    self.estados.pulando = True
                
                if not teclas[pygame.K_k]:
                    if teclas[pygame.K_f]:
                        self.estados.soco = True
                        
                    if teclas[pygame.K_t] and self.especial >= 100:
                        self.estados.special = True
                if teclas[pygame.K_k]:
                    self.estados.defesa = True
        #garantir um player sempre olhar para o outro
            
        #adicionar um cooldown
        if self.ataquecdr > 0:
            self.ataquecdr -= 1
 
        #metodo para pulo em fisica
        self.retangulo.y = self.fisica.aplicar_gravidade(self.retangulo.y, altura - self.retangulo.height)
        
        #resetar o estado de pulo
        if self.retangulo.y == altura - self.retangulo.height:
            self.estados.pulando = False
            
        
        #desenhar as animacoes na tela com base nos estados
        self.atualizar_animacao(superficie, alvo, 50) #tela, inimigo e cdr ataque
        self.estados.resetar_estados()  
        
