import pygame
from botoes import Botao
from jogador import Jogador
from inimigo import Inimigo
from tela_jogar import Tela_Jogar
class Menu:
    def __init__(self, x, y):
        self.__largura = None
        self.__altura = None
        self.__titulo = None
        self.__posicao_titulo = (x, y)
        self.titulo_renderizado = None  
        self.__botoes = [] 

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

    def tela(self):
        pygame.display.set_caption("Menu")
        return pygame.display.set_mode((self.largura, self.altura))
    
    def fundo_tela(self, img):
        fundo = pygame.image.load(img).convert_alpha()
        fundo = pygame.transform.scale(fundo, (self.largura, self.altura))
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
    def acoes_menu(self, player, bot, evento, superficie, altura, largura, fonte, fundo):
        
        clique = self.verifica_click(evento)
        if clique is not None:
            if clique == 0:
                pass
                 #LUGAR QUE EU CHAMO A FUNÇÃO DO JOGO
            elif clique == 1:
                jogar = Tela_Jogar(player, bot, fundo, 50, 50)
                run = True
                while run:
                    jogar.tela_fighting(superficie, altura, largura, fonte, fundo) 
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
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

   

        
