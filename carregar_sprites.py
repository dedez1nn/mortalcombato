import pygame

class Sprites:
    #(cris_tonaldo, [3, 4, 5, 6 ,7])
    def __init__(self, nome:str, numanim: list):
    #numidles: int, numwalk: int, numjump:int, numjkick:int, numkick:int, numpunch:int
        self.__sprites = {}
        self.__listanm = numanim
        self.__nomep = nome
        self.__sprite_atual = 0
        
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
        
    def addsprites(self):
        for i in range(len(self.__listanm)): # tratar exceções antes
            for j in range(self.__listanm[i]):
                temp = pygame.image.load(f'{self.nomep}/{i}/{j}.png').convert_alpha()
                temp = pygame.transform.scale(temp, (150, 150))
                self.__sprites[(i, j)] = temp
                
    def percorrer(self, indice: int):
        self.sprite_atual += 0.2
        if self.sprite_atual >= self.__listanm[indice]:
            self.sprite_atual = 0
        temp = self.__sprites[(indice, int(self.sprite_atual))]
        return temp
    
    def esperar_sprite(self, indice: int):
        pass
        
         
            
         
            
            
    
