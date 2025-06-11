import pygame
from fisica import Fisica
from carregar_sprites import Sprites
from estado_animacoes import Estados

class PersonagemBase:
    def __init__(self, nome: str, listar: list, x: int, y: int):
        self.__fisica = Fisica()
        self.__estados = Estados()
        self.__spritess = Sprites(nome, listar)
        self.__spritess.addsprites()
        self.__vida = 100
        self.__especial = 0
        self.__retangulo = pygame.Rect(x, y, 150, 150)
        self.__flip = False
        self.__ataquecdr = 0    
        
    @property
    def vida(self):
        return self.__vida

    @vida.setter
    def vida(self, val: int):
        self.__vida = val
        
    @property
    def especial(self):
        return self.__especial

    @especial.setter
    def especial(self, val: int):
        self.__especial = val

    @property
    def fisica(self):
        return self.__fisica

    @fisica.setter
    def fisica(self, val: Fisica):
        self.__fisica = val

    @property
    def estados(self):
        return self.__estados

    @estados.setter
    def estados(self, val: Estados):
        self.__estados = val

    @property
    def spritess(self):
        return self.__spritess

    @spritess.setter
    def spritess(self, val: Sprites):
        self.__spritess = val

    @property
    def retangulo(self):
        return self.__retangulo

    @retangulo.setter
    def retangulo(self, val: pygame.Rect):
        self.__retangulo = val

    @property
    def flip(self):
        return self.__flip

    @flip.setter
    def flip(self, val: bool):
        self.__flip = val

    @property
    def ataquecdr(self):
        return self.__ataquecdr

    @ataquecdr.setter
    def ataquecdr(self, val: int):
        self.__ataquecdr = val
    
        
    def attack(self, superficie, alvo, op):
        alcance = 10
        if self.flip:
            attacking_rect = pygame.Rect(self.retangulo.left, self.retangulo.top, alcance, self.retangulo.height)
        else:
            attacking_rect = pygame.Rect(self.retangulo.right, self.retangulo.top, alcance, self.retangulo.height)
            
        if self.ataquecdr == 0 and not alvo.estados.atingido and self.spritess.sprite_fim != -1 and op == 0:     
            if attacking_rect.colliderect(alvo.retangulo):
                if alvo.estados.defesa:
                    alvo.vida -= 0.5
                else:
                        pygame.time.delay(10)
                        alvo.vida -= 5
                        alvo.estados.atingido = True
                        if self.especial <= 90:
                            self.especial += 10
                        else:
                            self.especial = 100
        elif op == 1 and self.especial >= 100:
            if attacking_rect.colliderect(alvo.retangulo):
                if not alvo.estados.defesa:
                    alvo.vida -= 30
                    alvo.estados.atingido = True
            self.especial = 0
                    
            
                
                    
    def atualizar_animacao(self, superficie, alvo, cdr):
        vel = 0.2
        cooldown_time = 30
        if self.estados.special and not self.especial < 100:
            self.desenhar(superficie, 7, vel)
            if self.spritess.sprite_fim == 1:
                self.attack(superficie, alvo, 1)
                pygame.time.delay(cooldown_time)
                self.estados.special = False
        elif self.estados.soco and self.ataquecdr == 0:
            self.desenhar(superficie, 3, vel)
            if self.spritess.sprite_fim == 1:
                self.attack(superficie, alvo, 0)
                pygame.time.delay(cooldown_time)
                self.estados.soco = False
                self.ataquecdr = cdr
        elif self.estados.pulando:
                self.desenhar(superficie, 2, vel)
                if self.spritess.sprite_fim == 1:
                    pygame.time.delay(cooldown_time)
        elif self.estados.atingido:
                self.desenhar(superficie, 6, vel)
                if self.spritess.sprite_fim == 1:
                    self.estados.atingido = False
        elif self.estados.defesa:
                self.desenhar(superficie, 5, vel)
                if self.spritess.sprite_fim == 1:
                    self.estados.defesa = False
                    pygame.time.delay(cooldown_time)
        elif self.estados.andando and not self.retangulo.colliderect(alvo.retangulo):
                self.desenhar(superficie, 1, vel)
                if self.spritess.sprite_fim == 1:
                    pygame.time.delay(cooldown_time)
        else:
                self.desenhar(superficie, 0, vel)
                if self.spritess.sprite_fim == 1:
                    pygame.time.delay(cooldown_time)          
        
        
            
    def barra_vida(self, superficie, vida, x, y):
        razao = vida / 100
        pygame.draw.rect(superficie, (255, 255, 255), (x - 2, y - 2, 304, 34))
        pygame.draw.rect(superficie, (255, 0, 0), (x, y, 300, 30))
        pygame.draw.rect(superficie, (0, 255, 0), (x, y, 300 * razao, 31))
        
        esp_y = y + 40  # Posição Y da barra de especial
        razao_esp = self.especial / 100
        # Moldura do especial (fundo branco)
        pygame.draw.rect(superficie, (255, 255, 255), (x - 2, esp_y - 2, 154, 24))
        # Fundo do especial (cinza escuro)
        pygame.draw.rect(superficie, (50, 50, 50), (x, esp_y, 150, 20))
        # Especial atual (azul ou outra cor de sua escolha)
        pygame.draw.rect(superficie, (0, 100, 255), (x, esp_y, 150 * razao_esp, 20))
        
        
        
    def desenhar(self, superficie, indice: int, vel: float):
        imagem = self.spritess.percorrer(indice, vel)
        imagem_flipada = pygame.transform.flip(imagem, self.flip, False)
        superficie.blit(imagem_flipada, self.retangulo)

