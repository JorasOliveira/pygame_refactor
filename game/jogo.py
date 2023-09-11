import sys
import os
import pygame
import random

# Criando a gravidade
GRAVITY = 3.5
ATRITO = 1.005
ATRITO_P = 1.001

# Definindo algumas cores
BLACK = (0, 0, 0)
GREY = (127, 127, 127)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)


def calcula_colisao_chao(sprite):
    if sprite.rect.bottom > 672:  # com o chao
        sprite.rect.bottom = 672
        sprite.speed_y = 0

    sprite.rect.x = max(0,sprite.rect.x)
    sprite.rect.x = min(1336 - sprite.rect.width, sprite.rect.x)

class Background(pygame.sprite.Sprite):
    def __init__(self):

        imagem = os.path.join('Imagem', 'fundo.png')
        print(imagem)
        try:  # Importanto a imagem
            back_ground = pygame.image.load(imagem)  # da tela de fundo
        except pygame.error:
            print("Erro ao carregar imagem de fundo")
            sys.exit()

        pygame.sprite.Sprite.__init__(self)

        self.image = back_ground


class Startscreen(pygame.sprite.Sprite):
    def __init__(self):

        imagem = os.path.join('Imagem', 'startscreen.png')
        print(imagem)
        try:  # Importanto a imagem
            start_screen = pygame.image.load(imagem)  # da Tela Inicial
        except pygame.error:
            print("Erro ao carregar imagem inicial")
            sys.exit()

        pygame.sprite.Sprite.__init__(self)

        self.image = start_screen


class Jogador1(pygame.sprite.Sprite):
    def __init__(self,column, row, block):

        imagem = os.path.join('Imagem', 'ribamar.png')
        print(imagem)
        try:  # Importanto a imagem
            player1Img = pygame.image.load(imagem)  # do jogador 1
        except pygame.error:
            print("Erro ao carregar imagem do jogador 1")
            sys.exit()

        pygame.sprite.Sprite.__init__(self)

        self.image = player1Img
        self.blocks = block
        self.rect = self.image.get_rect()
        self.rect.x = column
        self.rect.bottom = row
        self.mask = pygame.mask.from_surface(self.image)
        self.score = 0
        self.speed_x = 0
        self.speed_y = 0

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y


class Jogador2(pygame.sprite.Sprite):
    def __init__(self, colum, row, block):

        imagem = os.path.join('Imagem', 'mece.png')

        print(imagem)
        try:  # Importanto a imagem
            player2Img = pygame.image.load(imagem)  # do jogador 2
        except pygame.error:
            print("Erro ao carregar imagem do jogador 2")
            sys.exit()

        pygame.sprite.Sprite.__init__(self)

        self.image = player2Img
        self.blocks = block
        self.rect = self.image.get_rect()
        self.rect.x = colum
        self.rect.bottom = row
        self.mask = pygame.mask.from_surface(self.image)
        self.score = 0
        self.speed_x = 0
        self.speed_y = 0

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y


class Bola(pygame.sprite.Sprite):
    def __init__(self, colum, row, block):

        imagem = os.path.join('Imagem', 'jabulani.png')
        print(imagem)
        try:  # Importanto a imagem
            ball = pygame.image.load(imagem)  # da bola
        except pygame.error:
            print("Erro ao carregar a bola")
            sys.exit()

        pygame.sprite.Sprite.__init__(self)

        self.image = ball
        self.blocks = block
        self.rect = self.image.get_rect()
        self.rect.x = colum
        self.rect.bottom = row
        self.mask = pygame.mask.from_surface(self.image)
        self.speed_x = 0
        self.speed_y = 0

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y


class Campo(pygame.sprite.Sprite):
    def __init__(self):

        imgfield = os.path.join('Imagem', 'field.png')
        print(imgfield)
        try:  # Importando a imagem
            pitch = pygame.image.load(imgfield)  # do campo
        except pygame.error:
            print("Erro ao carregar o campo")
            sys.exit()

        pygame.sprite.Sprite.__init__(self)

        self.image = pitch
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()


class GolEsquerdo(pygame.sprite.Sprite):
    def __init__(self):

        imggol1 = os.path.join('Imagem', 'gol-esq.png')

        print(imggol1)
        try:  # Importando a imagem
            g_esq = pygame.image.load(imggol1)  # do gol esquerdo
        except pygame.error:
            print("Erro ao carregar imagem do gol esquerdo")
            sys.exit()

        pygame.sprite.Sprite.__init__(self)

        self.image = g_esq
        self.rect = self.image.get_rect()
        self.rect.x = -100
        self.rect.bottom = 672
        self.mask = pygame.mask.from_surface(self.image)


class GolDireito(pygame.sprite.Sprite):
    def __init__(self):

        imggol2 = os.path.join('Imagem', 'gol-dir.png')

        print(imggol2)
        try:  # Impotando a imagem
            g_dir = pygame.image.load(imggol2)  # do gol direito
        except pygame.error:
            print("Erro ao carregar imagem do gol direito")
            sys.exit()

        pygame.sprite.Sprite.__init__(self)

        self.image = g_dir
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 1277
        self.rect.bottom = 672


class End_screen(pygame.sprite.Sprite):
    def __init__(self):

        imagem = os.path.join('Imagem', 'end_screen.png')
        print(imagem)
        try:  # Importanto a imagem
            End_screen = pygame.image.load(imagem)  # da end_screen
        except pygame.error:
            print("Erro ao carregar imagem final")
            sys.exit()

        pygame.sprite.Sprite.__init__(self)

        self.image = End_screen


def main():  # main routine
    pygame.init()

    # dimensoes do display, em X e Y
    display_x = 1336
    display_y = 752

    surf = pygame.display.set_mode([display_x, display_y])  # cria o display

    back_ground = Background()

    start_screen = Startscreen()

    end_screen = End_screen()

    # Criando o booleano para configurar a tela inicial:
    start = True

    pygame.display.update()

    font_score = pygame.font.Font(pygame.font.get_default_font(), 35)
    font_instructions = pygame.font.Font(pygame.font.get_default_font(), 20)


    # n tem contstante no python, mas letra maiuscula indica constante
    pos_y = int(display_y / 4)
    pos_x = int(display_x / 6)
    delta_pos_x = 1.75
    delta_pos_y = 100

    # cria os objetos dos jogadores/suas sprites
    p_1 = Jogador1(pos_x, pos_y, 'block')
    p_2 = Jogador2(1336 - 350, pos_y, 'block')
    jabulani = Bola(display_x / 2, display_x / 2, 'block')
    cancha = Campo()
    golEsq = GolEsquerdo()
    golDir = GolDireito()

    sprites = pygame.sprite.Group()  # criando o grupo de sprites
    sprites.add(p_1, p_2, jabulani)  # adiciona as sprites ao grupo de sprites

    # inicializa a musica de fundo
    torcida = os.path.join('Som', 'Torcida.ogg')  # Som ambiente de torcida
    pygame.mixer.music.load(torcida)  # Carrega som
    pygame.mixer.music.set_volume(0.2)  # Volume
    pygame.mixer.music.play(-1)  # Toca som

    # inicia os outros sons
    sompulo = os.path.join('Som', 'Pular.ogg')  # som do pulo
    pulo = pygame.mixer.Sound(sompulo)  # carrega som
    somchute = os.path.join('Som', 'Chute.ogg')  # som do chute
    chute = pygame.mixer.Sound(somchute)  # carrega som
    somgol = os.path.join('Som', 'Gol.ogg')  # som do gol
    gol = pygame.mixer.Sound(somgol)  # carrega som
    gol.set_volume(0.7)

    def reset():
        jabulani.rect.x = display_x / 2
        jabulani.rect.y = display_x / 2
        jabulani.speed_x = 0
        jabulani.speed_y = 0

        p_1.rect.x = pos_x
        p_1.rect.y = pos_y
        p_1.speed_x = 0
        p_1.speed_y = 0

        p_2.rect.x = 1336 - 350
        p_2.rect.y = pos_y
        p_2.speed_x = 0
        p_2.speed_y = 0

    def move_player():
        # jogador 1, se move com W,A,D
        if event.key == pygame.K_a:  # a para esquerda
            if p_1.speed_x >= 0.1:
                p_1.speed_x = 0
            p_1.speed_x -= delta_pos_x
            p_1.rect.x -= delta_pos_x

        if event.key == pygame.K_d:  # d para direita
            if p_1.speed_x <= -0.1:
                p_1.speed_x = 0
            p_1.speed_x += delta_pos_x
            p_1.rect.x += delta_pos_x

        # jogador 2, se move com as setas
        if event.key == pygame.K_LEFT:  # seta da esquerda para esquerda
            if p_2.speed_x >= 0.1:
                p_2.speed_x = 0
            p_2.speed_x -= delta_pos_x
            p_2.rect.x -= delta_pos_x

        if event.key == pygame.K_RIGHT:  # seta da direita para direita
            if p_2.speed_x <= -0.1:
                p_2.speed_x = 0
            p_2.speed_x += delta_pos_x
            p_2.rect.x += delta_pos_x

        if event.key == pygame.K_w:  # w faz o jogador 1 pular
            p_1.rect.y -= delta_pos_y
            pulo.play()

        if event.key == pygame.K_UP:  # seta para cima faz o jogador 2 pular
            p_2.rect.y -= delta_pos_y
            pulo.play()

    def calcula_colisao_p_bola(player1, player2, bola):
        if pygame.sprite.collide_mask(player1, bola):  
            # player 1 com  a bola, garantido que ele soh possa
            # chutar para o gol do p_2
            if player1.speed_x >= 0:
                bola.speed_x = player1.speed_x * (random.uniform(1, 3))
                bola.speed_y = (-1) * random.randint(12, 18) + player1.speed_y * (random.uniform(0.1, 0.7))
                chute.play()
            else:
                bola.speed_x = player1.speed_x * (random.uniform(1, 3)) * (-1)
                bola.speed_y = -player1.speed_y * (random.uniform(2, 4))
                chute.play()

        if pygame.sprite.collide_mask(player2, bola):  
            # player 2 com  a bola, garantido que ele soh possa
            # chutar para o gol do p_1

            if player2.speed_x <= 0:
                bola.speed_x = player2.speed_x * (random.uniform(1, 3))
                bola.speed_y = (-1) * random.randint(12, 18) + player2.speed_y * (random.uniform(0.1, 0.7))
                chute.play()

            else:
                bola.speed_x = player2.speed_x * (random.uniform(1, 3)) * (-1)
                bola.speed_y = -player2.speed_y * (random.uniform(2, 4))
                chute.play()


    def calcula_colisao_gol(gol_dir, gol_esq, bola):
        if pygame.sprite.collide_rect(bola, gol_dir):

            if bola.rect.top >= gol_dir.rect.top:
                p_1.score += 1
                gol.play()

                reset()

            elif bola.rect.bottom >= gol_dir.rect.top:
                bola.rect.bottom = gol_esq.rect.top
                bola.speed_x = -bola.speed_x
                bola.speed_y = -bola.speed_y

        if pygame.sprite.collide_rect(bola, gol_esq):

            if bola.rect.top >= gol_esq.rect.top:
                p_2.score += 1
                gol.play()

                reset()

            elif bola.rect.bottom >= gol_esq.rect.top:
                bola.rect.bottom = gol_esq.rect.top
                bola.speed_x = -bola.speed_x
                bola.speed_y = -bola.speed_y

    while True:
        surf.fill(BLACK)

        events = pygame.event.get()

        # inicia as variaveis para os placares
        placar_esquerda = p_1.score
        placar_direita = p_2.score

        # Editando as teclas do teclado para dar para jogar:
        for event in events:

            # quitando o jogo
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            # detectando o enter para iniciar o jogo
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                start = False

            # reincia o jogo caso queiram jogar denovo apos
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and (p_1.score >= 7 or p_2.score >= 7):
                p_1.score = 0
                p_2.score = 0

                reset()

            # quitando o jogo, fora da tela inicial
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            # detectando as key presses e fazendo o movimento referente
            if event.type == pygame.KEYDOWN:
                move_player()

        # Adicionando a tela inicial e fazendo o jogo rodar:
        if start:
            surf.blit(p_1.image, p_1.rect)
            surf.blit(p_2.image, p_2.rect)
            surf.blit(jabulani.image, jabulani.rect)
            surf.blit(start_screen.image, [display_x / 10, display_x / 10])

        # sai da tela inicial e comeca o jogo
        else:

            # calculando colisoes
            for sprite in sprites:

                calcula_colisao_chao(sprite)

                # colisao player com bola
                calcula_colisao_p_bola(p_1, p_2, jabulani)

                # colisões com o gol, toca o som, aumenta o placar, e reseta todos os sprites para a posicao inicial,
                # com, velocidade X e Y = 0

                calcula_colisao_gol(golDir, golEsq, jabulani)

                # gravidade, e atrito na bola
                jabulani.speed_y += GRAVITY / 20
                p_1.speed_y += GRAVITY / 30
                p_2.speed_y += GRAVITY / 30
                jabulani.speed_x /= ATRITO

                # para garantir que os sprites nao fiquem patinando pelo campo
                if 0.1 >= jabulani.speed_x >= -0.5:
                    jabulani.speed_x = 0

                p_1.speed_x /= ATRITO_P
                if 0.1 >= p_1.speed_x >= -0.5:
                    p_1.speed_x = 0

                p_2.speed_x /= ATRITO_P
                if 0.1 >= p_2.speed_x >= -0.5:
                    p_2.speed_x = 0

            sprites.update()

            # Adicionando as imagens do jogo
            surf.blit(back_ground.image, [0, 0])  # imagem de fundo
            surf.blit(p_1.image, p_1.rect)  # player 1
            surf.blit(p_2.image, p_2.rect)  # player 2
            surf.blit(jabulani.image, jabulani.rect)  # bola
            surf.blit(cancha.image, [0, 672])  # campo
            surf.blit(golEsq.image, [0, 320])  # gol da esquerda
            surf.blit(golDir.image, [1177, 320])  # gol da direita

            # Adicionando os placares:
            texto_esquerda = font_score.render("Ribamar: {0}".format(placar_esquerda), True, YELLOW)
            texto_direita = font_score.render("Messi Careca: {0}".format(placar_direita), True, YELLOW)
            surf.blit(texto_esquerda, (10, 0))
            surf.blit(texto_direita, (1045, 0))

            # Adicionando a tela final do jogo:
            if p_1.score >= 7:
                surf.fill(BLACK)
                surf.blit(end_screen.image, [display_x / 5, display_x / 5])
                texto_vencedor_1 = font_instructions.render("Jogador 1 venceu!", True, WHITE)
                texto_instrucoes_1 = font_instructions.render("Pressione 'Enter' para jogar novamente", True, WHITE)
                texto_instrucoes_2 = font_instructions.render("Pressione 'ESC' para sair", True, WHITE)
                surf.blit(p_1.image, (display_x * 0.47, display_x / 3))
                surf.blit(texto_vencedor_1, [display_x * 4 / 9, display_x / 3])
                surf.blit(texto_instrucoes_1, [display_x * 4 / 11, display_x * 3 / 5])
                surf.blit(texto_instrucoes_2,
                          [(display_x / 2) - (texto_instrucoes_2.get_rect().width / 2), display_x * 11 / 17])

            if p_2.score >= 7:
                surf.fill(BLACK)
                surf.blit(end_screen.image, [display_x / 5, display_x / 5])
                texto_vencedor_1 = font_instructions.render("Jogador 2 venceu!", True, WHITE)
                texto_instrucoes_1 = font_instructions.render("Pressione 'Enter' para jogar novamente", True, WHITE)
                texto_instrucoes_2 = font_instructions.render("Pressione 'ESC' para sair", True, WHITE)
                surf.blit(p_2.image, (display_x * 0.47, display_x / 3))
                surf.blit(texto_vencedor_1, [display_x * 4 / 9, display_x / 3])
                surf.blit(texto_instrucoes_1, [display_x * 4 / 11, display_x * 3 / 5])
                surf.blit(texto_instrucoes_2,
                          [(display_x / 2) - (texto_instrucoes_2.get_rect().width / 2), display_x * 11 / 17])

        pygame.display.flip()  # faz o update da imagine, usando troca de memory bugger


if __name__ == '__main__':
    main()
