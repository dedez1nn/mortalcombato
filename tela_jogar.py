from jogador import Jogador
from inimigo import Inimigo
import pygame, sys
from fase import Fase


class Tela_Jogar:
    def __init__(self, player: Jogador, bot: Inimigo, fundo: str, volume_ef: int, volume_mus: int):
        self.__player = player
        self.__bot = bot
        self.__fundo = fundo
        self.__volume_ef = volume_ef
        self.__volume_mus = volume_mus
        self.__pause = False
        self.__fase = Fase(player, bot)
        self.acabou = False
    
    @property
    def fase(self):
        return self.__fase
    
    @fase.setter
    def fase(self, val: Fase):
        self.__fase = val
    
    @property
    def volume_ef(self):
        return self.__volume_ef
    
    @property
    def volume_mus(self):
        return self.__volume_mus
    
    @volume_ef.setter
    def volume_ef(self, val: int):
        self.__volume_ef = val
        
    @volume_mus.setter
    def volume_mus(self, val: int):
        self.__volume_mus = val
    
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
    
    @player.setter
    def player(self, val: Jogador):
        self.__player = val
        
    @bot.setter
    def bot(self, val: Inimigo):
        self.__bot = val
        
    @fundo.setter
    def fundo(self, val: str):
        self.__fundo = val
        
    @pause.setter
    def pause(self, val: bool):
        self.__pause = val
        
    def define_volumes(self, ef: float, mus: float):
        self.volume_ef = ef
        self.volume_mus = mus

    def tela_fighting(self, superficie, altura, largura, fonte, fundo, sorteio):
        rodando = True
        clock = pygame.time.Clock()

        while rodando and not self.acabou:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            superficie.blit(fundo, (0, 0))
            texto_round = fonte.render(f"ROUND {self.fase.round}", True, (0, 0, 0))
            superficie.blit(texto_round, (350, 20))


            self.player.actions(superficie, altura, largura, self.bot)
            if sorteio == 1:
                self.bot.actions(superficie, altura, largura, self.player) 
            else:
                self.bot.actions_2(superficie, altura, largura, self.player) 
            self.player.barra_vida(superficie, 10, 20)
            self.bot.barra_vida(superficie, 490, 20)

            self.fase.loop_main()

            if self.fase.ganhador != -1:
                self.acabou = True
                rodando = False
                pygame.time.delay(2000)
                self.fase.reset_fase()
                return 0
            
            teclas = pygame.key.get_pressed()
            if teclas[pygame.K_p]:
                if not self.pause: 
                    self.pause = True
                    tela_congelada = superficie.copy()
                    if self.pausa(superficie, fonte, fundo, tela_congelada) == 0:
                        self.pause = False
                        self.fase.reset_fase()
                        pygame.time.delay(200)
                        return 0

            pygame.display.update()
            clock.tick(60)  # 60 FPS para garantir que a tela será atualizada

    def pausa(self, superficie, fonte, fundo, tela_congelada):
        texto_bloco_3 = fonte.render("Continuar", True, (0, 0, 0))
        texto_bloco_2 = fonte.render("Configuracoes", True, (0, 0, 0))
        texto_bloco_1 = fonte.render("Sair", True, (0, 0, 0))
        lista_textos = [texto_bloco_1, texto_bloco_2, texto_bloco_3]
        ret_selecionado = 2
        pegar_y = []

        while self.pause:
            superficie.blit(tela_congelada, (0, 0))  # fundo congelado

            pegar_y = []
            for i in range(3):
                y = 300 - i * 50
                pygame.draw.rect(superficie, (255, 255, 255), (300, y, 200, 40))
                superficie.blit(lista_textos[i], (305, y + 5))
                pegar_y.append(y)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        ret_selecionado = (ret_selecionado - 1) % len(lista_textos)
                    elif event.key == pygame.K_UP:
                        ret_selecionado = (ret_selecionado + 1) % len(lista_textos)
                    elif event.key == pygame.K_RETURN:
                        if ret_selecionado == 2:
                            self.pause = False
                        elif ret_selecionado == 1:
                            self.configuracoes(superficie, fonte, fundo, tela_congelada)
                        elif ret_selecionado == 0:  # Sair
                            return 0

            pygame.draw.rect(superficie, (255, 255, 0), (299, pegar_y[ret_selecionado], 200, 40), 5)
            pygame.display.flip() 
    
    def configuracoes(self, superficie, fonte, fundo, tela_congelada):
        config = True
        ret_selecionado = 0
        
        while config:
            superficie.blit(tela_congelada, (0, 0))
            razao = [(self.volume_ef)/ 100, (self.volume_mus) / 100]
            texto_bloco_1 = fonte.render("Volume", True, (0, 0, 0))
            texto_bloco_2 = fonte.render("Musica", True, (0, 0, 0))
            texto_bloco_3 = fonte.render("Voltar", True, (0, 0, 0))
            lista_textos = [texto_bloco_1, texto_bloco_2, texto_bloco_3]
            pegar_y = []
            
            for i in range(2):
                y = 300 - i * 50
                pygame.draw.rect(superficie, (255, 255, 255), (300, y, 150, 40))
                superficie.blit(lista_textos[i], (305, y + 5))
                pygame.draw.rect(superficie, (0, 0, 0), (500, y, 100 * razao[i], 40))
                pegar_y.append(y)
            pygame.draw.rect(superficie, (255, 255, 255), (300, 350, 150, 40))
            superficie.blit(texto_bloco_3, (300, 350))
            pegar_y.append(350)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        config = False
                    elif event.key == pygame.K_UP:
                        ret_selecionado = (ret_selecionado + 1) % len(lista_textos)
                    elif event.key == pygame.K_DOWN:
                        ret_selecionado = (ret_selecionado - 1) % len(lista_textos)
                    elif event.key == pygame.K_LEFT:
                        if ret_selecionado == 0:
                            self.volume_ef -= 10
                        elif ret_selecionado == 1:
                            self.volume_mus -= 10
                    elif event.key == pygame.K_RIGHT:
                        if ret_selecionado == 0:
                            self.volume_ef += 10
                        elif ret_selecionado == 1:
                            self.volume_mus += 10
                    elif event.key == pygame.K_RETURN:
                        if ret_selecionado == 2:
                            config = False
                            break

                pygame.draw.rect(superficie, (255, 255, 0), (299, pegar_y[ret_selecionado], 150, 40), 5)
                pygame.display.flip()
            if self.volume_ef >= 100:
                self.volume_ef = 100
            elif self.volume_ef <= 0:
                self.volume_ef = 0
            elif self.volume_mus >= 100:
                self.volume_mus = 100
            elif self.volume_mus <= 0:
                self.volume_mus = 0
    
    def game_over(self, superficie, fonte, tela_congelada):
        rodando = True
        if self.player.vida <= 0:
            while rodando:
                texto_titulo = fonte.render("Game Over", True, (0, 0, 0))
                texto_bloco_1 = fonte.render("Tentar Novamente", True, (0, 0, 0))
                texto_bloco_2 = fonte.render("Tentar Novamente", True, (0, 0, 0))
                lista_textos = [texto_bloco_1, texto_bloco_2]
                
                pegar_y = []
                for i in range(2):
                    y = 300 - i * 50
                    pygame.draw.rect(superficie, (255, 255, 255), (300, y, 150, 40))
                    superficie.blit(lista_textos[i], (305, y + 5))
                    pegar_y.append(y) 
                
                texto_round = fonte.render("GAME OVER!", True, (255, 0, 0))
                superficie.blit(texto_round, (350, 20))
                      
                 
