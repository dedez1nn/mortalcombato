import pygame
import sys
from botoes import Botao # precisa ser passado quando chamar a tela

class Tela_Inicial:
    def __init__(self, fundo: str):
        self.__fundo = fundo 
        self.__nome_jogador = ""
        self.__ativo = False  # Inicialmente a caixa de texto está inativa

    @property
    def ativo(self):
        return self.__ativo

    @ativo.setter
    def ativo(self, val: bool):
        self.__ativo = val
    @property
    def fundo(self):
        return self.__fundo
    
    @fundo.setter

    def fundo(self, val):
        self.__fundo = val

    @property
    def nome_jogador(self):
        return self.__nome_jogador
    
    @nome_jogador.setter
    def nome_jogador(self, nome):
        self.__nome_jogador = nome
        
    def inicial(self, superficie, fonte_titulo, fonte):
        fundo_img = pygame.image.load(self.fundo).convert()
        fundo_img = pygame.transform.scale(fundo_img, (800, 600))

        input_rect = pygame.Rect(250, 300, 300, 50)
        color_inativo = pygame.Color("gray15")
        color_ativo = pygame.Color("lightskyblue3")
        cor_atual = color_inativo

        botao_entrar = Botao(330, 400)
        botao_entrar.titulo_botao(fonte, "Entrar", (255, 255, 255))

        rodando = True
        while rodando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect.collidepoint(evento.pos):
                        self.ativo = True
                        cor_atual = color_ativo
                    else:
                        self.ativo = False
                        cor_atual = color_inativo

                    if botao_entrar.rect.collidepoint(evento.pos):
                        if self.nome_jogador.strip():
                          
                            return self.nome_jogador

                elif evento.type == pygame.KEYDOWN and self.ativo:
                    if evento.key == pygame.K_BACKSPACE:
                        self.nome_jogador = self.nome_jogador[:-1]
                    elif len(self.nome_jogador) < 15:
                        self.nome_jogador += evento.unicode

            superficie.blit(fundo_img, (0, 0))

            pygame.draw.rect(superficie, cor_atual, input_rect, 2)
            texto = fonte.render(self.nome_jogador, True, (255, 255, 255))
            superficie.blit(texto, (input_rect.x + 5, input_rect.y + 10))

            texto_titulo = fonte_titulo.render("Digite seu nome", True, (255, 255, 0))
            superficie.blit(texto_titulo, (240, 120))

            botao_entrar.render_botao(superficie)
            pygame.display.flip()
    
    def get_nome_jogador(self):
        return self.nome_jogador
