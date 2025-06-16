import pygame 

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

    def opcoes_menu(self):
        if self.botoes:
            
   
