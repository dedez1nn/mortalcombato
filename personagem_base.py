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
    
        
    def attack(self, alvo):
        alcance = 10
        if self.ataquecdr == 0 and not alvo.estados.atingido and self.spritess.sprite_fim != -1:
            if self.flip:
                attacking_rect = pygame.Rect(self.retangulo.left - alcance, self.retangulo.top, alcance, self.retangulo.height)
            else:
                attacking_rect = pygame.Rect(self.retangulo.right, self.retangulo.top, alcance, self.retangulo.height)
                
            if attacking_rect.colliderect(alvo.retangulo):
                if alvo.estados.defesa:
                    alvo.vida -= 0.5
                    alvo.retangulo.x += 2
                    self.retangulo.x -= 2
                else:
                    if not alvo.estados.soco: #não tomar dano se tiver na animação
                        pygame.time.delay(10)
                        alvo.vida -= 5
                        alvo.estados.atingido = True
            self.retangulo.x -= self.fisica.velocidade
            print("Atacou")
                    
    def atualizar_animacao(self, superficie, alvo):
        vel = 0.2
        cooldown_time = 30
        if self.estados.soco:
                    if self.estados.pulando:
                        self.desenhar(superficie, 7, 0.1)
                        if self.spritess.sprite_fim == 1:
                            self.attack(alvo)
                            pygame.time.delay(cooldown_time)
                            self.ataquecdr = 30
                            self.estados.soco = False
                    else:
                        self.desenhar(superficie, 3, vel)
                        if self.spritess.sprite_fim == 1:
                            self.attack(alvo)
                            pygame.time.delay(cooldown_time)
                            self.ataquecdr = 30
                            self.estados.soco = False
        elif self.estados.pulando:
                self.desenhar(superficie, 2, vel)
                if self.spritess.sprite_fim == 1:
                    pygame.time.delay(cooldown_time)
        elif self.estados.atingido:
                self.desenhar(superficie, 6, vel)
                if self.spritess.sprite_fim == 1:
                    pygame.time.delay(cooldown_time + 50)
                    self.estados.atingido = False
        elif self.estados.defesa:
                self.desenhar(superficie, 5, vel)
                if self.spritess.sprite_fim == 1:
                    self.estados.defesa = False
                    pygame.time.delay(cooldown_time)
        elif self.estados.andando:
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
        
        
        
    def desenhar(self, superficie, indice: int, vel: float):
        imagem = self.spritess.percorrer(indice, vel)
        imagem_flipada = pygame.transform.flip(imagem, self.flip, False)
        superficie.blit(imagem_flipada, self.retangulo)
