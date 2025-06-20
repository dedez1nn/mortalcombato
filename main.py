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
from nome_jogador import TelaInputNome
from tela_select import Tela_Select # Mantido a importação da tela de digitar nome

def main():
    pygame.init()
    pygame.mixer.init()

    largura = 800
    altura = 600
    tela = pygame.display.set_mode((largura, altura))
    fonte = pygame.font.SysFont(None, 38)
    fundo = pygame.image.load("fundoo.jpg").convert_alpha()
    pygame.display.set_caption("pescocoviado")
    musica = "MusicaMenu.mp3"

    input_nome = TelaInputNome()
    nome_jogador = input_nome.exibir(tela)
    print(f"Nome escolhido: {nome_jogador}")
    
    sprites_tonaldo = [3, 3, 4, 3, 4, 1, 8, 5]
    sprites_africa = [3, 3, 4, 6, 2, 1, 10, 5]
    sprites_ferro = [3, 3, 5, 6, 2, 1, 9, 4]
    sprites_nessi = [3, 3, 4, 3, 3, 1, 8, 8]
    
    lista_n_sprites = [sprites_tonaldo, sprites_africa, sprites_nessi, sprites_ferro]
    
    

    player = Jogador("cris_tonaldo", [3, 3, 4, 3, 4, 1, 8, 5], 10, altura - 150)

    player2 = Inimigo("cris_tonaldo", [3, 3, 4, 3, 4, 1, 8, 5], 400, altura - 150)

    
    lista_personagens = ["cris_tonaldo", "cap_africa", "lionel_nessi", "ryan_man"]
    lista_mini = []
    lista_default = []
    lista_sons_select = []
    sofreu_dano = pygame.mixer.Sound("assets/sofrer_dano.mp3")
    for i in range(len(lista_mini)):
        print(i)
    try:
        for i in range(len(lista_personagens)):
            mini = pygame.image.load(f"assets/tela_select/imagens/{lista_personagens[i]}_mini.png").convert_alpha()
            mini = pygame.transform.scale(mini, (50, 50))
            lista_mini.append(mini)
            default = pygame.image.load(f"assets/tela_select/imagens/{lista_personagens[i]}_grande.png").convert_alpha()
            lista_default.append(default)
            lista_sons_select.append(pygame.mixer.Sound(f"assets/tela_select/sons/{lista_personagens[i]}.mp3"))
    except Exception as e:
        print(e)   

    menu = Menu(245, 55, lista_personagens, lista_mini, lista_default, lista_sons_select, sofreu_dano, lista_n_sprites)
    fundo_menu = menu.fundo_tela(800, 600, "fundoo.jpg")  
    menu.titulo_menu("MKX Title.ttf", 50, "Mortal Kombat", (0, 0, 0))
    menu.criar_botao()        

    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            menu.acoes_menu(event, tela, altura, largura, fonte, fundo)
            break
            
        tela.blit(fundo, (0, 0))  
        menu.desenha_titulo_menu(tela)
        for botao in menu.botoes:
            botao.desenha_botao(tela)

        pygame.display.flip() 
                
    pygame.quit()

if __name__ == "__main__":
    main()
