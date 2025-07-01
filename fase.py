import pygame
from inimigo import Inimigo
from jogador import Jogador

class Fase:
    def __init__(self, player: Jogador, inimigo: Inimigo):
        self.__round = 1
        self.__objplayer = player
        self.__objbot = inimigo
        self.__rounds_ganhos = [0, 0]  # [0] player, [1] bot
        self.__ganhador = -1  # ninguém
        self.__streak = 0
        self.__pontos = 0

    @property
    def pontos(self):
        return self.__pontos
    
    @pontos.setter
    def pontos(self, val: int):
        self.__pontos = val

    @property
    def streak(self):
        return self.__streak
    
    @streak.setter
    def streak(self, val: int):
        self.__streak = val
        
    @property
    def ganhador(self):
        return self.__ganhador
    
    @ganhador.setter
    def ganhador(self, val: int):
        self.__ganhador = val
    
    @property
    def rounds_ganhos(self):
        return self.__rounds_ganhos
    
    @property
    def objplayer(self):
        return self.__objplayer
    
    @property
    def round(self):
        return self.__round
    
    @property
    def objbot(self):
        return self.__objbot
    
    @objplayer.setter
    def objplayer(self, val: Jogador):
        self.__objplayer = val
        
    @objbot.setter
    def objbot(self, val: Inimigo):
        self.__objbot = val
        
    @round.setter
    def round(self, val: int):
        self.__round = val
        
    @rounds_ganhos.setter
    def rounds_ganhos(self, val: list):
        self.__rounds_ganhos = val
        
    def loopmain(self):
        if self.rounds_ganhos[0] < 2 and self.rounds_ganhos[1] < 2: 
            if self.objplayer.vida <= 0:
                self.rounds_ganhos[1] += 1
                self.round += 1
                self.reset_atributos()
            elif self.objbot.vida <= 0:
                self.rounds_ganhos[0] += 1
                self.round += 1
                self.reset_atributos()        
        else:
            if self.rounds_ganhos[0] > self.rounds_ganhos[1]:
                self.ganhador = 0
                self.pontos += 300
                self.streak += 1
            else:
                self.ganhador = 1
                self.pontos -= 50
                self.streak = 0
            self.reset_atributos()
            print(f"Ganhador: {self.ganhador}")
            print(f"Streak: {self.streak}")
            print(f"Pontos: {self.pontos}")
            self.reset_fase()
    
    def get_dados_finais(self):
            return self.pontos, self.streak

    def reset_atributos(self):
        # Resetando os atributos dos personagens
        self.objplayer.estados.resetar_todos()
        self.objbot.estados.resetar_todos()
        self.objplayer.vida = 100
        self.objbot.vida = 100
        self.objplayer.especial = 0
        self.objbot.especial = 0
        self.objplayer.retangulo.x = 10
        self.objbot.retangulo.x = 490
        self.objbot.ataquecdr = 0
        self.objplayer.ataquecdr = 0
        pygame.time.delay(1000)
        
    def reset_fase(self):
        # Resetando a fase após o fim do round
        self.round = 1
        self.rounds_ganhos = [0, 0]
        self.__ganhador = -1
