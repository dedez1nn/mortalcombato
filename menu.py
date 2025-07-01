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
from fase import Fase
from tela_inicial import Tela_Inicial

class Menu:
    def __init__(self, x, y, lista_personagens, lista_mini, lista_default, lista_sons_select, som_hit, lista_n_sprites):
        self.__titulo = None
        self.__posicao_titulo = (x, y)
        self.titulo_renderizado = None
        self.__listas_select = [lista_personagens, lista_mini, lista_default, lista_sons_select, lista_n_sprites]
        self.__botoes = []
        self.__volume_ef = 0.5
        self.__volume_mus = 0.5

    @property
    def listas_select(self):
        return self.__listas_select

    @listas_select.setter
    def listas_select(self, val):
        self.__listas_select = val

    @property
    def volume_ef(self):
        return self.__volume_ef

    @property
    def volume_mus(self):
        return self.__volume_mus

    @volume_ef.setter
    def volume_ef(self, val):
        self.__volume_ef = val

    @volume_mus.setter
    def volume_mus(self, val):
        self.__volume_mus = val

    @property
    def botoes(self):
        return self.__botoes

    @botoes.setter
    def botoes(self, val):
        self.__botoes = val

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, val):
        self.__titulo = val

    @property
    def posicao_titulo(self):
        return self.__posicao_titulo

    @posicao_titulo.setter
    def posicao_titulo(self, val):
        self.__posicao_titulo = val

    def tela(self, largura, altura):
        pygame.display.set_caption("Menu")
        return pygame.display.set_mode((largura, altura))

    def fundo_tela(self, largura, altura, img):
        fundo = pygame.image.load(img).convert_alpha()
        fundo = pygame.transform.scale(fundo, (largura, altura))
        return fundo

    def titulo_menu(self, fonte, texto, cor):
        self.titulo_renderizado = fonte.render(texto, True, cor)

    def desenha_titulo_menu(self, tela):
        if self.titulo_renderizado:
            tela.blit(self.titulo_renderizado, self.posicao_titulo)

    def verifica_click(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            for i, botao in enumerate(self.botoes):
                if botao.rect.collidepoint(evento.pos):
                    return i
        return None

    def criar_botao(self, fonte):
        texto_botoes = ["Jogar", "Ranking", "Configuracoes", "Sair"]
        botoes_criados = []

        for i, texto in enumerate(texto_botoes):
            botao = Botao(300, 170 + i * 50)
            botao.titulo_botao(fonte, texto, (255, 255, 0))
            botoes_criados.append(botao)

        self.botoes = botoes_criados

    def tocar_musica(self, musica):
        pygame.mixer.music.load(musica)
        pygame.mixer.music.set_volume(self.volume_mus)
        pygame.mixer.music.play(-1)

    def acoes_menu(self, evento):
        clique = self.verifica_click(evento)
        if clique is not None:
            if clique == 0:
                return 0

            elif clique == 1:
                return 1

            elif clique == 2:
                return 2

            elif clique == 3:
                return 3
