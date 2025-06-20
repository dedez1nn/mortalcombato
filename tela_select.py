import pygame, sys


class Tela_Select:
    def __init__(self, lista_personagens: list, lista_mini: list, lista_default: list, lista_sons_select: list, vol_ef: float, vol_mus: float):
        self.__lista_personagens = lista_personagens
        self.__lista_mini = lista_mini
        self.__lista_default = lista_default
        self.__selecionado = -1
        self.__lista_sons_select = lista_sons_select
        self.__volume_ef = vol_ef
        self.__volume_mus = vol_mus
    
    @property
    def volume_ef(self):
        return self.__volume_ef
    
    @volume_ef.setter
    def volume_ef(self, val: float):
        self.__volume_ef = val
        
    @property
    def volume_mus(self):
        return self.__volume_mus
    
    @volume_mus.setter
    def volume_mus(self, val: float):
        self.__volume_mus = val
     
    @property
    def selecionado(self):
        return self.__selecionado
    
    @selecionado.setter
    def selecionado(self, selecionado: int):
        self.__selecionado = selecionado
        
    @property
    def lista_personagens(self):
        return self.__lista_personagens
    
    @property
    def lista_mini(self):
        return self.__lista_mini
    
    @property
    def lista_default(self):
        return self.__lista_default
    
    @lista_personagens.setter
    def lista_personagens(self, lista_personagens: list):
        self.__lista_personagens = lista_personagens
        
    @lista_mini.setter
    def lista_mini(self, lista_mini: list):
        self.__lista_mini = lista_mini
        
    @lista_default.setter
    def lista_default(self, lista_default: list):
        self.__lista_default = lista_default
        
    
    def exibir(self, superficie, fonte, fundo):
        pegar_x_mini = []
        for i in range(len(self.lista_mini)):
            pegar_x_mini.append(250 + (i * 100))
        ret_selecionado = 0
        ultimo_selecionado = -1
        
        
        rodando = True
        while rodando:
            superficie.blit(fundo, (0, 0))
            
            
            '''pygame.draw.rect(superficie, (0, 0, 0), (pegar_x_mini[0] - 50, 400, pegar_x_mini[3] - pegar_x_mini[0] + 150, 50))'''
            for i in range(len(self.lista_mini)):
                superficie.blit(self.lista_mini[i], (pegar_x_mini[i], 400))
            
            pygame.draw.rect(superficie, (255, 255, 0), (pegar_x_mini[ret_selecionado] + 1, 400, 50, 50), 2)
            superficie.blit(self.lista_default[ret_selecionado], (350, 100))
            
            texto_selecionado = self.lista_personagens[ret_selecionado]
            texto_selecionado = texto_selecionado.upper()
            texto_selecionado = texto_selecionado.replace("_", " ")
            texto_selecionado = fonte.render(texto_selecionado, True, (0, 0, 0))
            superficie.blit(texto_selecionado, (350,460))
            
            cooldown_sons = [0, 0, 0, 0]
            if ret_selecionado != ultimo_selecionado and cooldown_sons[ret_selecionado] == 0:
                for som in self.__lista_sons_select:
                   som.stop()          
                self.__lista_sons_select[ret_selecionado].set_volume(self.volume_ef)
                self.__lista_sons_select[ret_selecionado].play()
                ultimo_selecionado = ret_selecionado
                self.__lista_sons_select[ret_selecionado].play()
                cooldown_sons[ret_selecionado] = 10
            cooldown_sons[ret_selecionado] -= 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        ret_selecionado = (ret_selecionado + 1) % len(self.lista_mini)
                    elif event.key == pygame.K_LEFT:
                        ret_selecionado = (ret_selecionado - 1) % len(self.lista_mini)
                    elif event.key == pygame.K_RETURN:
                        print(self.lista_personagens[ret_selecionado])
                        rodando = False
            pygame.display.update()
        if ret_selecionado == 0:
            return 0
        elif ret_selecionado == 1:
            return 1
        elif ret_selecionado == 2:    
            return 2
        elif ret_selecionado == 3:
            return 3
        
        
        
        
        
        
                    
            
