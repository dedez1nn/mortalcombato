import pygame

class Sprites:
    #(cris_tonaldo, [3, 4, 5, 6 ,7])
    def __init__(self, nome:str, numanim: list):
    #numidles: int, numwalk: int, numjump:int, numjkick:int, numkick:int, numpunch:int
        self.__sprites = {}
        self.__listanm = numanim
        self.__nomep = nome
        self.__sprite_atual = 0
        self.__sprite_fim = 0
        
    #0 idle 
    #1 walk
    #2 jump
    #3 punch
    #4 kick
    #5 block
    #6 damage
    #7 jumpkick
    
    @property
    def sprites(self):
        return self.__sprites
    
    @property 
    def listanm(self):
        return self.__listanm
    
    @property
    def sprite_fim(self):
        return self.__sprite_fim
    
    @property
    def sprite_atual(self):
        return self.__sprite_atual
    
    @property
    def nomep(self):
        return self.__nomep
    
    @sprite_atual.setter
    def sprite_atual(self, val: float):
        if val <= 0: #tratamento
            self.__sprite_atual = 0.1
        else:
            self.__sprite_atual = val
        
    @sprites.setter
    def sprites(self, val: dict):
        self.__sprites = val
        
    @listanm.setter
    def listanm(self, val: list):
        self.__listanm = val
    
    @nomep.setter
    def nomep(self, novo: str):
        self.__nomep = novo
        
    @sprite_fim.setter
    def sprite_fim(self, val: int):
        self.__sprite_fim = val
        
    def addsprites(self):
        for i in range(len(self.__listanm)): # tratar exceções antes
            for j in range(self.__listanm[i]):
                temp = pygame.image.load(f'{self.nomep}/{i}/{j}.png').convert_alpha()
                temp = pygame.transform.scale(temp, (150, 150))
                self.__sprites[(i, j)] = temp
                
    def percorrer(self, indice: int, vel: float):
        
        self.sprite_atual += vel
        if self.sprite_atual >= self.listanm[indice]:
            self.sprite_atual = 0
            self.sprite_fim = 1
        else:
            self.sprite_fim = -1
        temp = self.sprites[(indice, int(self.sprite_atual))]
        return temp
        
         
            
         
