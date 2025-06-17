import pygame
import sys
from abc import ABC, abstractmethod
from fisica import Fisica
from carregar_sprites import Sprites
from estado_animacoes import Estados
from carregar_sprites import Sprites
from jogador import Jogador
from inimigo import Inimigo
from fase import Fase
from tela_jogar import Tela_Jogar
from menu import Menu


def main():
    pygame.init()


    largura = 800
    altura = 600
    tela = pygame.display.set_mode((largura, altura))
    fonte = pygame.font.SysFont(None, 38)

    pygame.display.set_caption("pescocoviado")
    menu = Menu(245, 55)
    menu.largura = 800
    menu.altura = 600
    fundo_menu = menu.fundo_tela("fundo/1.png")  
    menu.titulo_menu("MKX Title.ttf", 50, "Mortal Kombat", (0, 0, 0))
    menu.criar_botao()
    menu.tocar_musica("MusicaMenu.mp3")


    fundo = pygame.image.load("fundo/1.png").convert_alpha()
    run = True
    player = Jogador("cris_tonaldo", [3, 3, 4, 3, 4, 1, 8, 5], 10, altura - 150)
    player2 = Inimigo("cris_tonaldo", [3, 3, 4, 3, 4, 1, 8, 5], 400, altura - 150)
    clock = pygame.time.Clock()
    '''telatest = Tela_Jogar(player, player2, fundo, 50, 50)
    fase = Fase(player, player2)'''

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            '''elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    player.pause()'''
            menu.acoes_menu(player, player2, event, tela, altura, largura, fonte, fundo)
            break  # Verifica o clique a cada evento
            
        tela.blit(fundo_menu, (0, 0))  
        menu.desenha_titulo_menu(tela)
        for botao in menu.botoes:
            botao.desenha_botao(tela)
                            
        '''fase.loopmain()
        telatest.tela_fighting(tela, altura, largura, fonte, fundo)'''
        '''player.actions(tela, altura, largura, player2)
        #(self, superficie, vida, x, y)
        player.barra_vida(tela, 10, 20)
        player2.actions(tela, altura, largura, player) 
        player2.barra_vida(tela, 490, 20)'''
        
        pygame.display.flip() 
                
    pygame.quit()
    
    
if __name__ == "__main__":
    main()
