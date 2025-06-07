import pygame
import sys
from abc import ABC, abstractmethod
from fisica import Fisica
from carregar_sprites import Sprites
from estado_animacoes import Estados
from carregar_sprites import Sprites
from jogador import Jogador
from inimigo import Inimigo1


def main():
    pygame.init()
    #nada

    largura = 800
    altura = 600
    tela = pygame.display.set_mode((largura, altura))

    pygame.display.set_caption("pescocoviado")



    run = True
    player = Jogador("cris_tonaldo", [3, 3, 4, 3, 4, 1, 8, 3], 10, altura - 150)
    player2 = Inimigo1("cris_tonaldo", [3, 3, 4, 3, 4, 1, 8, 3], 400, altura - 150)
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
                

        tela.fill((0, 0, 0))
        player.actions(tela, altura, largura, player2)      
        #(self, superficie, vida, x, y)
        player.barra_vida(tela, player.vida, 10, 20)
        player2.actions(tela, altura, largura, player)    
        player2.barra_vida(tela, player2.vida, 490, 20)
        pygame.display.flip() 
                
    pygame.quit()
    
    
if __name__ == "__main__":
    main()
