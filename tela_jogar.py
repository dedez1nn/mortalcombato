from jogador import Jogador
from inimigo import Inimigo
import pygame, sys


class Tela_Jogar:
    def __init__(self, player: Jogador, bot: Inimigo, fundo: str, volume: int):
        self.__player = player
        
        self.__bot = bot
        self.__fundo = fundo
        self.__volume = volume
        self.__pause = False
    
    @property
    def pause(self):
        
        return self.__pause
    
    @property
    def player(self):
        return self.__player  
    
    @property
    def bot(self):
        return self.__bot
    
    @property
    def fundo(self):
        return self.__fundo
    
    @property
    def volume(self):
        return self.__volume
    
    @player.setter
    def player(self, val: Jogador):
        self.__player = val
        
    @bot.setter
    def bot(self, val: Inimigo):
        self.__bot = val
        
    @fundo.setter
    def fundo(self, val: str):
        self.__fundo = val
        
    @volume.setter
    def volume(self, val: int):
        self.__volume = val
        
    @pause.setter
    def pause(self, val: bool):
        self.__pause = val

    def tela_fighting(self, superficie, altura, largura, fonte, fundo):
        '''imagem = self.spritess.percorrer(indice, vel)
        imagem_flipada = pygame.transform.flip(imagem, self.flip, False)'''
        superficie.blit(fundo, (0, 0))
        texto_bloco_3 = fonte.render("Continuar", True, (0, 0, 0))
        texto_bloco_2 = fonte.render("Configuracoes", True, (0, 0, 0))
        texto_bloco_1 = fonte.render("Sair", True, (0, 0, 0))
        lista_textos = [texto_bloco_1, texto_bloco_2, texto_bloco_3]         
        ret_selecionado = 2
        pegar_y = []
        teclas = pygame.key.get_pressed()    
        if teclas[pygame.K_p]:    
            self.pause = True
        self.player.actions(superficie, altura, largura, self.bot)
        self.bot.actions(superficie, altura, largura, self.player) 
        self.player.barra_vida(superficie, 10, 20)
        self.bot.barra_vida(superficie, 490, 20)
        while self.pause:
            for i in range(3):
                y = 300 - i * 50
                pygame.draw.rect(superficie, (255, 255, 255), (300, y, 200, 40))
                superficie.blit(lista_textos[i], (305, y + 5))
                pegar_y.append(y)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        ret_selecionado = (ret_selecionado - 1) % len(lista_textos)
                    elif event.key == pygame.K_UP:
                        ret_selecionado = (ret_selecionado + 1) % len(lista_textos)
                    elif event.key == pygame.K_RETURN:
                        if ret_selecionado == 2:
                            self.pause = False
                            break
                        elif ret_selecionado ==1:
                            print("Configuracoes")
                            break
                        elif ret_selecionado == 0:
                            sys.exit()
                            break
            pygame.draw.rect(superficie, (255, 255, 0), (299, pegar_y[ret_selecionado], 200, 40), 5)
            
            
               
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
