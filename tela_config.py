import pygame
import sys
from botoes import Botao

class Tela_Config:
    def __init__(self, volume_ef: float, volume_mus: float, fundo: str, fundo_mais: str, fundo_menos: str):
        self.__volume_ef = volume_ef
        self.__volume_mus = volume_mus
        self.__fundo = fundo
        self.__fundo_volume = [fundo_mais, fundo_menos]

    @property
    def volume_mus(self):
        return self.__volume_mus

    @volume_mus.setter
    def volume_mus(self, val: float):
        self.__volume_mus = max(0.0, min(1.0, val))

    @property
    def volume_ef(self):
        return self.__volume_ef

    @volume_ef.setter
    def volume_ef(self, val: float):
        self.__volume_ef = max(0.0, min(1.0, val))

    @property
    def fundo(self):
        return self.__fundo

    def cria_botoes_config(self, fonte, fonte_titulo):
        titulo = Botao(245, 55)
        voltar = Botao(620, 500)
        musc = Botao(340, 150)
        ef = Botao(340, 280)

        musc.titulo_botao(fonte, "Musica", (255, 255, 0))
        ef.titulo_botao(fonte, "Efeitos", (255, 255, 0))
        titulo.titulo_botao(fonte_titulo, "Configuracoes", (0, 0, 0))
        voltar.titulo_botao(fonte, "Voltar", (255, 0, 0))

        botoes = [titulo, voltar, musc, ef]
        return botoes

    def desenha_botoes_config(self, superficie, botoes):
        for botao in botoes:
            botao.render_botao(superficie)

    def desenha_barras_volume(self, superficie):
        largura_max = 200
        altura = 20
        x = 290

        # Música
        y_mus = 225
        largura_mus = int(self.__volume_mus * largura_max)
        pygame.draw.rect(superficie, (80, 80, 80), (x, y_mus, largura_max, altura))
        pygame.draw.rect(superficie, (0, 200, 255), (x, y_mus, largura_mus, altura))

        # Efeitos
        y_ef = 350
        largura_ef = int(self.__volume_ef * largura_max)
        pygame.draw.rect(superficie, (80, 80, 80), (x, y_ef, largura_max, altura))
        pygame.draw.rect(superficie, (0, 255, 100), (x, y_ef, largura_ef, altura))

    def config(self, superficie, fonte, fonte_titulo):
        print("Entrou na tela de configurações")

        imagem = pygame.image.load(self.fundo).convert()
        imagem = pygame.transform.scale(imagem, (800, 600))

        icone_mais = pygame.image.load(self.__fundo_volume[0]).convert_alpha()
        icone_menos = pygame.image.load(self.__fundo_volume[1]).convert_alpha()

        # POSIÇÕES
        pos_menos_mus = (250, 215)
        pos_mais_mus = (490, 215)
        pos_menos_ef = (250, 340)
        pos_mais_ef = (490, 340)

        # Retângulos de clique
        ret_menos_mus = pygame.Rect(*pos_menos_mus, icone_menos.get_width(), icone_menos.get_height())
        ret_mais_mus = pygame.Rect(*pos_mais_mus, icone_mais.get_width(), icone_mais.get_height())
        ret_menos_ef = pygame.Rect(*pos_menos_ef, icone_menos.get_width(), icone_menos.get_height())
        ret_mais_ef = pygame.Rect(*pos_mais_ef, icone_mais.get_width(), icone_mais.get_height())

        botoes = self.cria_botoes_config(fonte, fonte_titulo)
        voltar = botoes[1] 

        rodando = True
        while rodando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                    rodando = False
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    if ret_menos_mus.collidepoint(evento.pos):
                        self.volume_mus -= 0.1
                        pygame.mixer.music.set_volume(self.volume_mus)
                    elif ret_mais_mus.collidepoint(evento.pos):
                        self.volume_mus += 0.1
                        pygame.mixer.music.set_volume(self.volume_mus)
                    elif ret_menos_ef.collidepoint(evento.pos):
                        self.volume_ef -= 0.1
                    elif ret_mais_ef.collidepoint(evento.pos):
                        self.volume_ef += 0.1
                    elif voltar.rect.collidepoint(evento.pos):
                        rodando = False

            superficie.blit(imagem, (0, 0))

            superficie.blit(icone_menos, pos_menos_mus)
            superficie.blit(icone_mais, pos_mais_mus)
            superficie.blit(icone_menos, pos_menos_ef)
            superficie.blit(icone_mais, pos_mais_ef)

            self.desenha_botoes_config(superficie, botoes)
            self.desenha_barras_volume(superficie)

            pygame.display.flip()
