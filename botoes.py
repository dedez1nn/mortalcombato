import pygame

PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
AMARELO = (255, 255, 0)

class BotaoTexto:
    def __init__(self, texto, pos, fonte, destaque=True):
        self.texto = texto
        self.pos = pos
        self.fonte = fonte
        self.destaque = destaque
        self.rect = self.fonte.render(texto, True, (0, 0, 0)).get_rect(center=pos)

    def desenhar(self, tela, mouse_pos):
        if not self.destaque:
            cor = PRETO
        elif self.rect.collidepoint(mouse_pos):
            cor = VERMELHO
        else:
            cor = AMARELO

        render = self.fonte.render(self.texto, True, cor)
        tela.blit(render, self.rect)

    def clicado(self, mouse_pos, mouse_clique):
        return self.rect.collidepoint(mouse_pos) and mouse_clique[0]
    
    
