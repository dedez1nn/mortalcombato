import pygame
import sys
from fisica import Fisica
pygame.init()
#nada
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))

pygame.display.set_caption("pescocoviado")

class Personagem(pygame.sprite.Sprite, Fisica):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.fisica = Fisica()
        self.__vida = 100
        self.retangulo = pygame.Rect(x, y, 50, 50)
        self.flip = 0
    
    @property
    def vida(self):
        return self.__vida
    
    @vida.setter
    def vida(self, val:int):
        if val < 0:
            self.__vida = 0
        else:
            self.__vida = val
    
    def actions(self, altura, largura, tela, alvo, op: int):
        teclas = pygame.key.get_pressed()

        
        if op == 1:
            if teclas[pygame.K_LEFT]:
                self.retangulo.x -= 5
                if self.retangulo.x < 0:
                   self.retangulo.x = 0

            if teclas[pygame.K_RIGHT]:
                self.retangulo.x += 5
                if self.retangulo.x > largura - self.retangulo.width:
                    self.retangulo.x = largura - self.retangulo.width

            if teclas[pygame.K_UP] and not self.fisica.pulo and self.retangulo.y == altura - self.retangulo.height:
                self.fisica.iniciar_pulo()

            if teclas[pygame.K_r]:
                self.attack(tela, alvo)
                
            if alvo.retangulo.centerx > self.retangulo.centerx:
                self.flip = 1
            else:
                self.flip = 0
                

            self.retangulo.y = self.fisica.aplicar_gravidade(self.retangulo.y, altura - self.retangulo.height)
        
        if op == 2:
            if teclas[pygame.K_a]:
                self.retangulo.x -= 5
                if self.retangulo.x < 0:
                    self.retangulo.x = 0

            if teclas[pygame.K_d]:
                self.retangulo.x += 5
                if self.retangulo.x > largura - self.retangulo.width:
                    self.retangulo.x = largura - self.retangulo.width

            if teclas[pygame.K_w] and not self.fisica.pulo and self.retangulo.y == altura - self.retangulo.height:
                self.fisica.iniciar_pulo()

            if teclas[pygame.K_f]:
                self.attack(tela, alvo)
                
            if alvo.retangulo.centerx > self.retangulo.centerx:
                self.flip = 0
            else:
                self.flip = 1

            self.retangulo.y = self.fisica.aplicar_gravidade(self.retangulo.y, altura - self.retangulo.height)
    
    def attack(self, superficie, alvo):
        attacking_rect = pygame.Rect(self.retangulo.centerx - (2 *  self.retangulo.width * self.flip), self.retangulo.y, 2 * self.retangulo.width, self.retangulo.height)
        if attacking_rect.colliderect(alvo.retangulo):
            alvo.vida -= 10 
         
        
    def barra_vida(self, vida, x, y):
        razao = vida / 100
        pygame.draw.rect(tela, (255, 255, 255), (x - 2, y - 2, 304, 34))
        pygame.draw.rect(tela, (255, 0, 0), (x, y, 300, 30))
        pygame.draw.rect(tela, (0, 255, 0), (x, y, 300 * razao, 31))
        
        
    def desenhar(self, superficie):
        pygame.draw.rect(superficie, (255, 0, 0), self.retangulo)

run = True
player = Personagem(100, altura - 50)
player2 = Personagem(500, altura - 50)
clock = pygame.time.Clock()

while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()
            

    tela.fill((0, 0, 0))
    player.actions(altura, largura, tela, player2, 1)      
    player.desenhar(tela)
    player.barra_vida(player.vida, 10, 20)
    player2.actions(altura, largura, tela, player, 2)    
    player2.desenhar(tela)     
    player.barra_vida(player2.vida, 490, 20)
    pygame.display.flip() 
            
pygame.quit()
