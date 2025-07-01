import pygame
import random
from botoes import Botao
from jogador import Jogador
from inimigo import Inimigo
from tela_jogar import Tela_Jogar
from tela_select import Tela_Select
from tela_config import Tela_Config
from tela_ranking import Tela_Ranking
from manager_ranking import ManagerRanking
from jogador_ranking import JogadorRanking
from tela_inicial import Tela_Inicial
from menu import Menu
import sys

def main():
    pygame.init()
    pygame.mixer.init()

    largura = 800
    altura = 600
    tela = pygame.display.set_mode((largura, altura))
    fonte = pygame.font.Font("MKX Title.ttf", 38)
    fonte_titulo = pygame.font.Font("MKX Title.ttf", 50)
    fundo = pygame.image.load("fundo/1.png").convert_alpha()
    pygame.display.set_caption("pescocoviado")
    musica = "MusicaMenu.mp3"
    caminho_fundo = "fundo/1.png"
    inicio = Tela_Inicial(caminho_fundo)
    inicio.inicial(tela, fonte_titulo, fonte)
    nomejogador = inicio.get_nome_jogador()

    # Dados dos personagens
    sprites_tonaldo = [3, 3, 4, 3, 4, 1, 8, 5]
    sprites_africa = [3, 3, 4, 6, 2, 1, 10, 5]
    sprites_ferro = [3, 3, 5, 6, 2, 1, 9, 4]
    sprites_nessi = [3, 3, 4, 3, 3, 1, 8, 8]

    lista_n_sprites = [sprites_tonaldo, sprites_africa, sprites_nessi, sprites_ferro]
    lista_personagens = ["cris_tonaldo", "cap_africa", "lionel_nessi", "ryan_man"]
    lista_mini = []
    lista_default = []
    lista_sons_select = []
    sofreu_dano = pygame.mixer.Sound("assets/sofrer_dano.mp3")

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
    fundo_menu = menu.fundo_tela(800, 600, "fundo/1.png")
    menu.titulo_menu(fonte_titulo, "Mortal Kombat", (0, 0, 0))
    menu.criar_botao(fonte)
    menu.tocar_musica(musica)

    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()

            clique = menu.acoes_menu(event)

            if clique == 0:
                # === JOGAR ===
                pygame.mixer.music.stop()
                select = Tela_Select(
                    lista_personagens, lista_mini, lista_default, lista_sons_select,
                    menu.volume_ef, menu.volume_mus
                )
                res = select.exibir(tela, fonte, fundo)
                nome = lista_personagens[res]
                tam_sprites = lista_n_sprites[res]
                menu.volume_ef = select.volume_ef
                menu.volume_mus = select.volume_mus

                player = Jogador(nome, tam_sprites, 10, altura - 150)

                # Inimigo aleatório
                sorteio = random.randint(0, 3)
                nome_bot = lista_personagens[sorteio]
                sprites_bot = lista_n_sprites[sorteio]
                bot = Inimigo(nome_bot, sprites_bot, 400, altura - 150)

                jogar = Tela_Jogar(player, bot, fundo, menu.volume_ef * 100, menu.volume_mus * 100)
                sorteio = random.randint(1, 2)

                res = jogar.tela_fighting(tela, altura, largura, fonte, fundo, sorteio)
                res_pausa = jogar.pausa(tela, fonte, fundo, res)

                if res == 0 or res_pausa == 0:

                    menu.volume_ef = jogar.volume_ef
                    menu.volume_mus = jogar.volume_mus
                    pontos, sequencia = jogar.fase.get_dados_finais()                
                    manager_ranking = ManagerRanking()
                    manager_ranking.carrega_arquivo("ranking.json")
                    manager_ranking.add_jogador(JogadorRanking(nomejogador, pontos, sequencia))
                    manager_ranking.salvar_ranking("ranking.json")
                    break

            elif clique == 1:
                ranking = Tela_Ranking("fundo/1.png")
                ranking.ranking(tela, fonte, fonte_titulo)

            elif clique == 2:
                config = Tela_Config(0.5, 0.5, "fundo/1.png", "fundo/3.png", "fundo/2.png")
                config.config(tela, fonte, fonte_titulo)

            elif clique == 3:
                run = False
                pygame.quit()
                sys.exit()

        tela.blit(fundo_menu, (0, 0))
        menu.desenha_titulo_menu(tela)
        for botao in menu.botoes:
            botao.render_botao(tela)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
