import pygame
import sys
from main import main as iniciar_jogo
from botoes import BotaoTexto

def main():
    pygame.init()
    WIDTH, HEIGHT = 800, 600
    tela = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Menu")

    PRETO = (0, 0, 0)
    AMARELO = (255, 255, 0)
    VERMELHO = (255, 0, 0)
    FUNDO_CINZA = (200, 200, 200)
    CINZA = (180, 180, 180)

    try:
        pygame.mixer.music.load("MusicaMenu.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
    except pygame.error:
        print("Erro ao carregar a música de fundo.")

    try:
        fonte_titulo = pygame.font.Font("MKX Title.ttf", 60)
        fonte_botoes = pygame.font.Font("MKX Title.ttf", 30)
    except FileNotFoundError:
        fonte_titulo = pygame.font.Font(None, 60)
        fonte_botoes = pygame.font.Font(None, 30)

    try:
        fundo = pygame.image.load("fundo/1.png").convert()
        fundo = pygame.transform.scale(fundo, (WIDTH, HEIGHT))
    except:
        fundo = None

    clock = pygame.time.Clock()
    rodando = True

    def sair_menu_para_jogo():
        nonlocal rodando
        rodando = False
        pygame.mixer.music.stop()
        iniciar_jogo()

    def tela_configuracoes():
        volume_musica = pygame.mixer.music.get_volume()
        volume_efeitos = 0.5
        rodando_config = True
        titulo_config = fonte_titulo.render("Configuracoes", True, PRETO)
        botao_voltar = BotaoTexto("Voltar", (WIDTH - 100, HEIGHT - 50), fonte_botoes)

        while rodando_config:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    mx, my = evento.pos

                    if 100 <= mx <= 300 and 200 <= my <= 220:
                        volume_musica = (mx - 100) / 200
                        volume_musica = max(0.0, min(1.0, volume_musica))
                        pygame.mixer.music.set_volume(volume_musica)

                    elif 100 <= mx <= 300 and 300 <= my <= 320:
                        volume_efeitos = (mx - 100) / 200
                        volume_efeitos = max(0.0, min(1.0, volume_efeitos))

                    elif botao_voltar.rect.collidepoint((mx, my)):
                        rodando_config = False

            if fundo:
                tela.blit(fundo, (0, 0))
            else:
                tela.fill(FUNDO_CINZA)

            tela.blit(titulo_config, (WIDTH // 2 - titulo_config.get_width() // 2, 50))

            def desenha_slider(label, valor, x, y):
                texto = fonte_botoes.render(f"{label}: {int(valor * 100)}%", True, AMARELO)
                tela.blit(texto, (x, y - 30))
                pygame.draw.rect(tela, CINZA, (x, y, 200, 20))
                pygame.draw.rect(tela, VERMELHO, (x, y, int(valor * 200), 20))

            desenha_slider("Volume da Música", volume_musica, 260, 200)
            desenha_slider("Volume dos Efeitos", volume_efeitos, 260, 300)

            mouse_pos = pygame.mouse.get_pos()
            botao_voltar.desenhar(tela, mouse_pos)

            pygame.display.update()
            clock.tick(60)

    # Criar os botões com ações associadas
    botoes = [
        {"obj": BotaoTexto("Mortal Kombat", (WIDTH // 2, HEIGHT // 2 - 215), fonte_titulo, destaque=False), "acao": None},
        {"obj": BotaoTexto("Jogar", (WIDTH // 2, HEIGHT // 2 - 120), fonte_botoes), "acao": sair_menu_para_jogo},
        {"obj": BotaoTexto("Continuar", (WIDTH // 2, HEIGHT // 2 - 70), fonte_botoes), "acao": lambda: print("Continuar clicado!")},
        {"obj": BotaoTexto("Pontuacao", (WIDTH // 2, HEIGHT // 2 - 20), fonte_botoes), "acao": lambda: print("Pontuação clicada!")},
        {"obj": BotaoTexto("Configuracoes", (WIDTH // 2, HEIGHT // 2 + 30), fonte_botoes), "acao": tela_configuracoes},
        {"obj": BotaoTexto("Sair", (WIDTH // 2, HEIGHT // 2 + 80), fonte_botoes), "acao": lambda: sys.exit()},
    ]

    while rodando:
        if fundo:
            tela.blit(fundo, (0, 0))
        else:
            tela.fill(FUNDO_CINZA)

        mouse_pos = pygame.mouse.get_pos()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                for botao in botoes:
                    if botao["obj"].rect.collidepoint(evento.pos) and botao["acao"]:
                        botao["acao"]()

        for botao in botoes:
            botao["obj"].desenhar(tela, mouse_pos)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
