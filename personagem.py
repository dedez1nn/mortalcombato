import pygame
import sys
from fisica import Fisica
from carregar_sprites import Sprites
pygame.init()
#nada
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))

pygame.display.set_caption("pescocoviado")

class Personagem(pygame.sprite.Sprite, Fisica):
    def __init__(self, nome: str, listar: list, x: int, y: int):
        super().__init__()
        self.fisica = Fisica()
        self.spritess = Sprites(nome, listar)
        self.spritess.addsprites()
        self.__vida = 100
        self.retangulo = pygame.Rect(x, y, 150, 150)
        self.flip = False
    
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
                self.desenhar(tela, 1)
                if self.retangulo.x < 0:
                   self.retangulo.x = 0

            elif teclas[pygame.K_RIGHT]:
                self.retangulo.x += 5
                self.desenhar(tela, 1)
                if self.retangulo.right > largura:
                    self.retangulo.right = largura

            elif teclas[pygame.K_UP] and not self.fisica.pulo and self.retangulo.y == altura - self.retangulo.height:
                self.fisica.iniciar_pulo()
                self.desenhar(tela, 2)

            elif teclas[pygame.K_r]:
                self.attack(tela, alvo)
                self.desenhar(tela, 3)
                
            else:
                self.desenhar(tela, 0)
                
            if alvo.retangulo.centerx > self.retangulo.centerx:
                self.flip = False
            else:
                self.flip = True
                
                
                

            self.retangulo.y = self.fisica.aplicar_gravidade(self.retangulo.y, altura - self.retangulo.height)
        
        if op == 2:
            if teclas[pygame.K_a]:
                self.retangulo.x -= 5
                self.desenhar(tela, 1)
                if self.retangulo.x < 0:
                    self.retangulo.x = 0

            elif teclas[pygame.K_d]:
                self.retangulo.x += 5
                self.desenhar(tela, 1)
                if self.retangulo.right > largura:
                    self.retangulo.right = largura

            elif teclas[pygame.K_w] and not self.fisica.pulo and self.retangulo.y == altura - self.retangulo.height:
                self.fisica.iniciar_pulo()
                self.desenhar(tela, 2)

            elif teclas[pygame.K_f]: 
                self.attack(tela, alvo)
                self.desenhar(tela, 3)
            else:
                self.desenhar(tela, 0)
                
                
            if alvo.retangulo.centerx > self.retangulo.centerx:
                self.flip = False
            else:
                self.flip = True

            self.retangulo.y = self.fisica.aplicar_gravidade(self.retangulo.y, altura - self.retangulo.height)
    
    def attack(self, superficie, alvo):
        if self.flip:
            attacking_rect = pygame.Rect(
                self.retangulo.left - self.retangulo.width,  # ataque para trás
                self.retangulo.top,
                self.retangulo.width,
                self.retangulo.height
            )
        else:
            attacking_rect = pygame.Rect(
                self.retangulo.right,  # ataque para frente
                self.retangulo.top,
                self.retangulo.width,
                self.retangulo.height
            )
        if attacking_rect.colliderect(alvo.retangulo):
            alvo.vida -= 10
         
        #171x212
    def barra_vida(self, vida, x, y):
        razao = vida / 100
        pygame.draw.rect(tela, (255, 255, 255), (x - 2, y - 2, 304, 34))
        pygame.draw.rect(tela, (255, 0, 0), (x, y, 300, 30))
        pygame.draw.rect(tela, (0, 255, 0), (x, y, 300 * razao, 31))
        
        
    def desenhar(self, superficie, indice: int):
        imagem = self.spritess.percorrer(indice)
        imagem_flipada = pygame.transform.flip(imagem, self.flip, False)
        superficie.blit(imagem_flipada, self.retangulo)

run = True
player = Personagem("cris_tonaldo", [3, 3, 4, 3, 4, 1, 8, 3], 10, altura - 150)
player2 = Personagem("cris_tonaldo", [3, 3, 4, 3, 4, 1, 8, 3], 400, altura - 150)
clock = pygame.time.Clock()

while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()
            

    tela.fill((0, 0, 0))
    player.actions(altura, largura, tela, player2, 1)      
    player.barra_vida(player.vida, 10, 20)
    player2.actions(altura, largura, tela, player, 2)    
    player.barra_vida(player2.vida, 490, 20)
    pygame.display.flip() 
            
pygame.quit()
