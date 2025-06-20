import pygame
from botoes import Botao
from jogador import Jogador
from inimigo import Inimigo
from tela_jogar import Tela_Jogar
import random
from tela_select import Tela_Select
class Menu:
    def __init__(self, x, y, lista_personagens: list, lista_mini: list, lista_default: list, lista_sons_select: list, som_hit, lista_n_sprites: list):
        self.__titulo = None
        self.__posicao_titulo = (x, y)
        self.titulo_renderizado = None
        self.__listas_select = [lista_personagens, lista_mini, lista_default, lista_sons_select, lista_n_sprites]
        #0 = tonaldo, 1 = africa, 2 = ferro, 3 = nessi
        self.__botoes = [] 
        self.__volume_ef = 0.5
        self.__volume_mus = 0.5
    
    @property
    def listas_select(self):
        return self.__listas_select
    
    @listas_select.setter
    def listas_select(self, val: list):
        self.__listas_select = val
    
    @property
    def volume_ef(self):
        return self.__volume_ef
    
    @property
    def volume_mus(self):
        return self.__volume_mus
    
    @volume_ef.setter
    def volume_ef(self, val: float):
        self.__volume_ef = val
        
    @volume_mus.setter
    def volume_mus(self, val: float):
        self.__volume_mus = val
    
    @property
    def botoes(self):
        return self.__botoes

    @property
    def largura(self):
        return self.__largura
    
    @property
    def altura(self):
        return self.__altura
    
    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def posicao_titulo(self):
        return self.__posicao_titulo
    
    @botoes.setter
    def botoes(self, lista_botoes):
        self.__botoes = lista_botoes

    @largura.setter
    def largura(self, valor):
        self.__largura = valor
    
    @altura.setter
    def altura(self, valor):
        self.__altura = valor

    @titulo.setter
    def titulo(self, valor):
        self.__titulo = valor

    @posicao_titulo.setter
    def posicao_titulo(self, posicao):
        self.__posicao_titulo = posicao

#------------------------------------------------------

    def tela(self, largura, altura):
        pygame.display.set_caption("Menu")
        return pygame.display.set_mode((largura, altura))
    
    def fundo_tela(self, largura, altura,img):
        fundo = pygame.image.load(img).convert_alpha()
        fundo = pygame.transform.scale(fundo, (largura, altura))
        return fundo
    
    def titulo_menu(self, fonte, tamanho, texto, cor):
        fonte_render = pygame.font.Font(fonte, tamanho)
        self.titulo_renderizado = fonte_render.render(texto, True, cor) 
    
    def desenha_titulo_menu(self, tela):
        if self.titulo_renderizado:
            tela.blit(self.titulo_renderizado, self.posicao_titulo)

    def verifica_click(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            for i in range(len(self.botoes)):
                opcao = self.botoes[i]
                if opcao.rect.collidepoint(evento.pos):  # Verifica se clicou no botão
                    return i
        return None           

    def criar_botao(self):
        texto_botoes = ["Jogar", "Continuar", "Ranking", "Configuracoes", "Sair"]
        botoes_criados = []

        for i in range(len(texto_botoes)):
            texto = texto_botoes[i]
            pos_botao = Botao(300, 170 + i * 50)
            pos_botao.titulo_botao("MKX Title.ttf", 35, texto, (255, 255, 0))
            botoes_criados.append(pos_botao)
        self.botoes = botoes_criados

    def acoes_menu(self, evento, superficie, altura, largura, fonte, fundo):
        
        clique = self.verifica_click(evento)
        if clique is not None:
            if clique == 0:
                print("vamoo")
                 #LUGAR QUE EU CHAMO A FUNÇÃO DO JOGO
            elif clique == 1:
                
                select = Tela_Select(self.listas_select[0], self.listas_select[1], self.listas_select[2], self.listas_select[3], self.volume_ef, self.volume_mus)
                res = select.exibir(superficie, fonte, fundo)
                nome = self.listas_select[0][res]
                tam_sprites = self.listas_select[4][res] 
                pygame.mixer.music.stop()
                self.volume_ef = select.volume_ef
                self.volume_mus = select.volume_mus
                player = Jogador(nome, tam_sprites, 10, altura - 150)
                #rand aqui em baixo
                sorteio = random.randint(0,3)
                nome_bot = self.listas_select[0][sorteio]
                sprites_bot = self.listas_select[4][sorteio]
                bot = Inimigo(nome_bot, sprites_bot, 400, altura - 150)
                
                
                
                jogar = Tela_Jogar(player, bot, fundo, self.volume_ef * 100, self.volume_mus * 100)
                sorteio = random.randint(1,2)
                res = jogar.tela_fighting(superficie, altura, largura, fonte, fundo, sorteio)
                res_pausa = jogar.pausa(superficie, fonte, fundo, res)
                if res == 0 or res_pausa == 0:
                    return
                self.volume_ef = jogar.volume_ef
                self.volume_mus = jogar.volume_mus
                print("Essa ")#LUGAR QUE EU CHAMO A FUNÇÃO DE CONTINUAR O JOGO
            elif clique == 2:
                print("Botão Ranking clicado") #LUGAR QUE EU CHAMO A FUNÇÃO DO RANKING
            elif clique == 3:
                print("Botão Configurações clicado") #LUGAR QUE EU CHAMO
            elif clique == 4:
                print("Botão Sair clicado")  # LUGAR QUE EU CHAMO
                pygame.quit()    
                exit()
    
    def tocar_musica(self, musica):
        pygame.mixer.music.load(musica)
        pygame.mixer.music.set_volume(self.volume_mus)
        pygame.mixer.music.play(-1)
         
        
