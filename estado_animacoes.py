import pygame

 #0 idle 
    #1 walk
    #2 jump
    #3 punch
    #4 kick
    #5 block
    #6 damage
    #7 jumpkick

class Estados:
    def __init__(self):
        self.__parado = True
        self.__andando = False
        self.__pulando = False
        self.__soco = False
        self.__defesa = False
        self.__atingido = False
        self.__special = False
        
    @property
    def parado(self):
        return self.__parado
    
    @property
    def pulando(self):
        return self.__pulando
    
    @property
    def andando(self):
        return self.__andando
    
    @property
    def soco(self):
        return self.__soco
    
    @property
    def atingido(self):
        return self.__atingido
    
    @property
    def special(self):
        return self.__special
    
    @property
    def defesa(self):
        return self.__defesa
    
    @parado.setter
    def parado(self, val: bool):
        self.__parado = val
        
    @atingido.setter
    def atingido(self, val:bool):
        self.__atingido = val
    
    
    @andando.setter
    def andando(self, val: bool):
        self.__andando = val
    
    
    @soco.setter
    def soco(self, val: bool):
        self.__soco = val
    
    @defesa.setter
    def defesa(self, val: bool):
        self.__defesa = val
    
    @pulando.setter
    def pulando(self, val: bool):
        self.__pulando = val
    
    @special.setter
    def special(self, val: bool):
        self.__special = val
        
    def resetar_estados(self):
        self.parado = True
        self.andando = False
        
    def resetar_todos(self):
        self.__parado = True
        self.__andando = False
        self.__pulando = False
        self.__soco = False
        self.__defesa = False
        self.__atingido = False
        self.__special = False
