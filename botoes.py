import pygame
class Botao:
    def __init__(self, x, y):
        self.__posicao_botao = (x, y)
        self.__titulo_renderizado = None  
        self.__rect = None 

    @property
    def rect(self):
        return self.__rect
    
    @rect.setter
    def rect(self, valor):
        self.__rect = valor

    @property
    def posicao_botao(self):
        return self.__posicao_botao
    
    @posicao_botao.setter
    def posicao_botao(self, posicao):
        self.__posicao_botao = posicao
    # Getter para titulo_renderizado
    @property
    def titulo_renderizado(self):        
        return self.__titulo_renderizado

    # Setter para titulo_renderizado
    @titulo_renderizado.setter
    def titulo_renderizado(self, valor):
        self.__titulo_renderizado = valor

    def titulo_botao(self, fonte, tamanho, texto, cor):
        fonte_render = pygame.font.Font(fonte, tamanho)
        self.titulo_renderizado = fonte_render.render(texto, True, cor)
        self.rect = self.titulo_renderizado.get_rect(topleft=self.posicao_botao)

    def desenha_botao(self, tela):
        if self.titulo_renderizado:
            tela.blit(self.titulo_renderizado, self.posicao_botao)






import pygame
from menu import Menu
import sys

def main():
    pygame.init()
    
    menu = Menu(245, 55)
    menu.largura = 800
    menu.altura = 600
    tela = menu.tela()
    fundo = menu.fundo_tela("fundo/1.png")  
    menu.titulo_menu("MKX Title.ttf", 50, "Mortal Kombat", (0, 0, 0))  
    botao1 = Botao(300, 200)
    botao1.titulo_botao("Arial.ttf", 30, "Jogar", (255, 255, 255))

    botao2 = Botao(300, 300)
    botao2.titulo_botao("Arial.ttf", 30, "Sair", (255, 255, 25)
    
    menu.botoes = [botao1, botao2] 


    run = True
    clock = pygame.time.Clock()
    
    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()

        tela.blit(fundo, (0, 0))  
        menu.desenha_titulo_menu(tela)  

        pygame.display.flip()  
    
    pygame.quit()

if __name__ == "__main__":
    main()
            
