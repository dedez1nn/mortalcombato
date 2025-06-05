import pygame
import sys
from fisica import Fisica
from spriteteste import Sprites

pygame.init()

largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("pescocoviado")

class Personagem(pygame.sprite.Sprite, Fisica):
    def __init__(self, nome: str, listar: list, x: int, y: int):
        super().__init__()
        self.__fisica = Fisica()
        self.__spritess = Sprites(nome, listar)
        self.__spritess.addsprites()
        self.__estados = {
            'parado': True,
            'andando': False,
            'pulando': False,
            'soco': False,
            'chute': False,
            'defesa': False,
            'atingido': False,
            'chutepulo': False,
            'flip': False
        }
        self.__vida = 100
        self.__retangulo = pygame.Rect(x, y, 150, 150)
        self.__flip = False

        # Flags e timers para ataque
        self.__attack_f_pressed_last = False
        self.__attack_r_pressed_last = False
        self.attack_cooldown = 0
        self.ataque_em_andamento = False
        self.ataque_timer = 0

    @property
    def vida(self):
        return self.__vida

    @property
    def estados(self):
        return self.__estados

    @property
    def fisica(self):
        return self.__fisica

    @property
    def flip(self):
        return self.__flip

    @property
    def spritess(self):
        return self.__spritess

    @property
    def retangulo(self):
        return self.__retangulo

    @vida.setter
    def vida(self, val: int):
        self.__vida = max(val, 0)

    @retangulo.setter
    def retangulo(self, x: int, y: int, wid: int, hei: int):
        if x < 0 or y < 0 or wid < 0 or hei < 0:
            raise Exception("Erro, valor ou valores inválido(s)!")
        else:
            self.__retangulo = pygame.Rect(x, y, wid, hei)

    @fisica.setter
    def fisica(self, val: Fisica):
        self.__fisica = val

    @spritess.setter
    def spritess(self, val: Sprites):
        self.__spritess = val

    @flip.setter
    def flip(self, val: bool):
        self.__flip = val

    @estados.setter
    def estados(self, novo: dict):
        for i, val in novo.items():
            self.__estados[i] = val

    def actions(self, altura, largura, tela, alvo, op: int):
        teclas = pygame.key.get_pressed()

        andando = False
        atacando = False

        # Diminui cooldown
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1

        # Reduz timer de ataque ativo
        if self.ataque_em_andamento:
            self.ataque_timer -= 1
            atacando = True
            if self.ataque_timer <= 0:
                self.ataque_em_andamento = False

        if op == 1:
            if teclas[pygame.K_LEFT]:
                self.retangulo.x -= 5
                andando = True
                if self.retangulo.x < 0:
                    self.retangulo.x = 0

            if teclas[pygame.K_RIGHT]:
                self.retangulo.x += 5
                andando = True
                if self.retangulo.right > largura:
                    self.retangulo.right = largura

            if teclas[pygame.K_UP] and not self.fisica.no_ar:
                self.fisica.iniciar_pulo()

            if teclas[pygame.K_f]:
                if not self.__attack_f_pressed_last and not self.ataque_em_andamento and self.attack_cooldown == 0:
                    self.attack(tela, alvo)
                    self.ataque_em_andamento = True
                    self.ataque_timer = 10
                    self.attack_cooldown = 20
                self.__attack_f_pressed_last = True
            else:
                self.__attack_f_pressed_last = False

        if op == 2:
            if teclas[pygame.K_a]:
                self.retangulo.x -= 5
                andando = True
                if self.retangulo.x < 0:
                    self.retangulo.x = 0

            if teclas[pygame.K_d]:
                self.retangulo.x += 5
                andando = True
                if self.retangulo.right > largura:
                    self.retangulo.right = largura

            if teclas[pygame.K_w] and not self.fisica.pulo:
                self.fisica.iniciar_pulo()

            if teclas[pygame.K_r]:
                if not self.__attack_r_pressed_last and not self.ataque_em_andamento and self.attack_cooldown == 0:
                    self.attack(tela, alvo)
                    self.ataque_em_andamento = True
                    self.ataque_timer = 10
                    self.attack_cooldown = 20
                self.__attack_r_pressed_last = True
            else:
                self.__attack_r_pressed_last = False

        if alvo.retangulo.centerx > self.retangulo.centerx:
            self.flip = False
        else:
            self.flip = True

        self.retangulo.y = self.fisica.aplicar_gravidade(self.retangulo.y, altura - self.retangulo.height)

        self.atualizar_animacao(tela, andando, atacando)

    def atualizar_animacao(self, superficie, andando, atacando):
        if self.fisica.pulo:
            self.desenhar(superficie, 2)
        elif atacando:
            self.desenhar(superficie, 3)
        elif andando:
            self.desenhar(superficie, 1)
        else:
            self.desenhar(superficie, 0)

    def attack(self, superficie, alvo):
        if self.flip:
            attacking_rect = pygame.Rect(self.retangulo.left - self.retangulo.width, self.retangulo.top,
                                         self.retangulo.width, self.retangulo.height)
        else:
            attacking_rect = pygame.Rect(self.retangulo.right, self.retangulo.top,
                                         self.retangulo.width, self.retangulo.height)
        if attacking_rect.colliderect(alvo.retangulo):
            alvo.vida -= 10

    def barra_vida(self, vida, x, y):
        razao = vida / 100
        pygame.draw.rect(tela, (255, 255, 255), (x - 2, y - 2, 304, 34))
        pygame.draw.rect(tela, (255, 0, 0), (x, y, 300, 30))
        pygame.draw.rect(tela, (0, 255, 0), (x, y, 300 * razao, 31))

    def desenhar(self, superficie, indice: int):
        imagem = self.spritess.percorrer(indice)
        imagem_flipada = pygame.transform.flip(imagem, self.flip, False)
        superficie.blit(imagem_flipada, self.retangulo)


# ===== Loop principal básico =====

run = True
player = Personagem("cris_tonaldo", [3, 3, 4, 3, 4, 1, 8, 3], 10, altura - 150)
player2 = Personagem("cris_tonaldo", [3, 3, 4, 3, 4, 1, 8, 3], 400, altura - 150)
clock = pygame.time.Clock()

while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()

    tela.fill((0, 0, 0))
    player.actions(altura, largura, tela, player2, 1)
    player.barra_vida(player.vida, 10, 20)

    player2.actions(altura, largura, tela, player, 2)
    player2.barra_vida(player2.vida, 490, 20)

    pygame.display.flip()

pygame.quit()
