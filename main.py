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
from nome_jogador import TelaInputNome  # Mantido a importação da tela de digitar nome

def main():
    pygame.init()

    largura = 800
    altura = 600
    tela = pygame.display.set_mode((largura, altura))
    fonte = pygame.font.SysFont(None, 38)
    pygame.display.set_caption("pescocoviado")

    input_nome = TelaInputNome()
    nome_jogador = input_nome.exibir(tela)
    print(f"Nome escolhido: {nome_jogador}")

    player = Jogador("cris_tonaldo", [3, 3, 4, 3, 4, 1, 8, 5], 10, altura - 150)
    player2 = Inimigo("cris_tonaldo", [3, 3, 4, 3, 4, 1, 8, 5], 400, altura - 150)

    menu = Menu(245, 55)
    fundo_menu = menu.fundo_tela(800, 600, "fundo/1.png")  
    menu.titulo_menu("MKX Title.ttf", 50, "Mortal Kombat", (0, 0, 0))
    menu.criar_botao()
    menu.tocar_musica("MusicaMenu.mp3")

    fundo = pygame.image.load("fundo/1.png").convert_alpha()
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            menu.acoes_menu(player, player2, event, tela, altura, largura, fonte, fundo)
            break
            
        tela.blit(fundo_menu, (0, 0))  
        menu.desenha_titulo_menu(tela)
        for botao in menu.botoes:
            botao.desenha_botao(tela)

        pygame.display.flip() 
                
    pygame.quit()

if __name__ == "__main__":
    main()
