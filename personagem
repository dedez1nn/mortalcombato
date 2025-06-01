import pygame
import sys
from fisica import Fisica

pygame.init()

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
    
    @property
    def vida(self):
        return self.__vida
    
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

            if teclas[pygame.K_r]:
                self.attack(tela, alvo)

            self.retangulo.y = self.fisica.aplicar_gravidade(self.retangulo.y, altura - self.retangulo.height)
    
    def attack(self, superficie, alvo):
        attacking_rect = pygame.Rect(self.retangulo.centerx, self.retangulo.y, 2 * self.retangulo.width, self.retangulo.height)
        if attacking_rect.colliderect(alvo.retangulo):
            print("Acertou")
         
        
    
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

    tela.fill((255, 255, 255))    
    player.actions(altura, largura, tela, player2, 1)      
    player.desenhar(tela)
    player2.actions(altura, largura, tela, player, 2)      
    player2.desenhar(tela)     
    pygame.display.flip() 
            
pygame.quit()
