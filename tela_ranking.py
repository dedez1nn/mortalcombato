import pygame
import sys
from botoes import Botao  # Importante: certifique-se do caminho correto
from manager_ranking import ManagerRanking

class Tela_Ranking:
    def __init__(self, fundo: str):
        self.__fundo = fundo
        self.__manager_ranking = ManagerRanking()
    
    @property
    def manager_ranking(self):
        return self.__manager_ranking
    
    @manager_ranking.setter
    def manager_ranking(self, val: ManagerRanking):
        self.__manager_ranking = val
    
    @property
    def fundo(self):
        return self.__fundo
    
    @fundo.setter
    def fundo(self, val: str):
        self.__fundo = val

    def cria_botoes_ranking(self, fonte, fonte_titulo):
        titulo_ranking = Botao(300, 55)
        voltar_ranking = Botao(620, 500)

        titulo_ranking.titulo_botao(fonte_titulo, "Ranking", (0, 0, 0))
        voltar_ranking.titulo_botao(fonte, "Voltar", (255, 0, 0))

        return [titulo_ranking, voltar_ranking]
    
    def desenha_botoes_ranking(self, superficie, botoes_ranking):
        for botao in botoes_ranking:
            botao.render_botao(superficie)

    def exibir_ranking(self, superficie, fonte):
        # Carrega os dados do ranking salvos em arquivo
        self.manager_ranking.carrega_arquivo("ranking.json")  # Carrega o arquivo de ranking
        jogadores = self.manager_ranking.jogadores  # Obtém a lista de jogadores

        # Renderiza o ranking na tela
        for i, jogador in enumerate(jogadores):
            texto = fonte.render(str(jogador), True, (255, 255, 255))  # Desenha o texto
            superficie.blit(texto, (100, 150 + i * 40))  # Ajuste de posição (espacamento)

    def ranking(self, superficie, fonte, fonte_titulo):
        # Carrega o fundo
        imagem_ranking = pygame.image.load(self.fundo).convert()
        imagem_ranking = pygame.transform.scale(imagem_ranking, (800, 600))

        botoes = self.cria_botoes_ranking(fonte, fonte_titulo)
        voltar = botoes[1]

        rodando = True
        while rodando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if voltar.rect.collidepoint(evento.pos):
                        rodando = False

            superficie.blit(imagem_ranking, (0, 0))
            self.desenha_botoes_ranking(superficie, botoes)
            # Chama o método para exibir o ranking na tela
            self.exibir_ranking(superficie, fonte)

            pygame.display.flip()
