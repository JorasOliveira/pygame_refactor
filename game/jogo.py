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


class Background(pygame.sprite.Sprite):
    def __init__(self):

        imagem = os.path.join('Imagem', 'fundo.png')
        print(imagem)
        try:  # Importanto a imagem
            BackGround = pygame.image.load(imagem)  # da tela de fundo
        except pygame.error:
            print("Erro ao carregar imagem de fundo")
            sys.exit()

        pygame.sprite.Sprite.__init__(self)

        self.image = BackGround


class Startscreen(pygame.sprite.Sprite):
    def __init__(self):

        imagem = os.path.join('Imagem', 'startscreen.png')
        print(imagem)
        try:  # Importanto a imagem
            StartScreen = pygame.image.load(imagem)  # da Tela Inicial
        except pygame.error:
            print("Erro ao carregar imagem inicial")
            sys.exit()

        pygame.sprite.Sprite.__init__(self)

        self.image = StartScreen


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
        self.speedX = 0
        self.speedY = 0

    def update(self):
        self.rect.x += self.speedX
        self.rect.y += self.speedY


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
        self.speedX = 0
        self.speedY = 0

    def update(self):
        self.rect.x += self.speedX
        self.rect.y += self.speedY


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
        self.speedX = 0
        self.speedY = 0

    def update(self):
        self.rect.x += self.speedX
        self.rect.y += self.speedY


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


class Endscreen(pygame.sprite.Sprite):
    def __init__(self):

        imagem = os.path.join('Imagem', 'endscreen.png')
        print(imagem)
        try:  # Importanto a imagem
            EndScreen = pygame.image.load(imagem)  # da endscreen
        except pygame.error:
            print("Erro ao carregar imagem final")
            sys.exit()

        pygame.sprite.Sprite.__init__(self)

        self.image = EndScreen


def main():  # main routine
    pygame.init()

    # dimensoes do display, em X e Y
    DISPLAY_X = 1336
    DISPLAY_Y = 752

    surf = pygame.display.set_mode([DISPLAY_X, DISPLAY_Y])  # cria o display

    backGround = Background()

    startScreen = Startscreen()

    endScreen = Endscreen()

    # Criando o booleano para configurar a tela inicial:
    start = True

    pygame.display.update()

    fontScore = pygame.font.Font(pygame.font.get_default_font(), 35)
    fontInstructions = pygame.font.Font(pygame.font.get_default_font(), 20)

    clock = pygame.time.Clock()

    # n tem contstante no python, mas letra maiuscula indica constante
    POS_Y = int(DISPLAY_Y / 4)
    POS_X = int(DISPLAY_X / 6)
    DELTA_POS_X = 1.75
    DELTA_POS_Y = 100

    # cria os objetos dos jogadores/suas sprites
    p1 = Jogador1(POS_X, POS_Y, 'block')
    p2 = Jogador2(1336 - 350, POS_Y, 'block')
    jabulani = Bola(DISPLAY_X / 2, DISPLAY_X / 2, 'block')
    cancha = Campo()
    golEsq = GolEsquerdo()
    golDir = GolDireito()

    sprites = pygame.sprite.Group()  # criando o grupo de sprites
    sprites.add(p1, p2, jabulani)  # adiciona as sprites ao grupo de sprites

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
        jabulani.rect.x = DISPLAY_X / 2
        jabulani.rect.y = DISPLAY_X / 2
        jabulani.speedX = 0
        jabulani.speedY = 0

        p1.rect.x = POS_X
        p1.rect.y = POS_Y
        p1.speedX = 0
        p1.speedY = 0

        p2.rect.x = 1336 - 350
        p2.rect.y = POS_Y
        p2.speedX = 0
        p2.speedY = 0

    def move_player():
        # jogador 1, se move com W,A,D
        if event.key == pygame.K_a:  # a para esquerda
            if p1.speedX >= 0.1:
                p1.speedX = 0
            p1.speedX -= DELTA_POS_X
            p1.rect.x -= DELTA_POS_X

        if event.key == pygame.K_d:  # d para direita
            if p1.speedX <= -0.1:
                p1.speedX = 0
            p1.speedX += DELTA_POS_X
            p1.rect.x += DELTA_POS_X

        # jogador 2, se move com as setas
        if event.key == pygame.K_LEFT:  # seta da esquerda para esquerda
            if p2.speedX >= 0.1:
                p2.speedX = 0
            p2.speedX -= DELTA_POS_X
            p2.rect.x -= DELTA_POS_X

        if event.key == pygame.K_RIGHT:  # seta da direita para direita
            if p2.speedX <= -0.1:
                p2.speedX = 0
            p2.speedX += DELTA_POS_X
            p2.rect.x += DELTA_POS_X

        if event.key == pygame.K_w:  # w faz o jogador 1 pular
            p1.rect.y -= DELTA_POS_Y
            pulo.play()

        if event.key == pygame.K_UP:  # seta para cima faz o jogador 2 pular
            p2.rect.y -= DELTA_POS_Y
            pulo.play()

    def calcula_colisao_p_bola(player1, player2, bola):
        if pygame.sprite.collide_mask(player1, bola):  # player 1 com  a bola, garantido que ele soh possa
            # chutar para o gol do p2
            if player1.speedX >= 0:
                bola.speedX = player1.speedX * (random.uniform(1, 3))
                bola.speedY = (-1) * random.randint(12, 18) + player1.speedY * (random.uniform(0.1, 0.7))
                chute.play()
            else:
                bola.speedX = player1.speedX * (random.uniform(1, 3)) * (-1)
                bola.speedY = -player1.speedY * (random.uniform(2, 4))
                chute.play()

        if pygame.sprite.collide_mask(player2, bola):  # player 2 com  a bola, garantido que ele soh possa
            # chutar para o gol do p1

            if player2.speedX <= 0:
                bola.speedX = player2.speedX * (random.uniform(1, 3))
                bola.speedY = (-1) * random.randint(12, 18) + player2.speedY * (random.uniform(0.1, 0.7))
                chute.play()

            else:
                bola.speedX = player2.speedX * (random.uniform(1, 3)) * (-1)
                bola.speedY = -player2.speedY * (random.uniform(2, 4))
                chute.play()

    def calcula_colisao_chao(sprite):
        if sprite.rect.bottom > 672:  # com o chao
            sprite.rect.bottom = 672
            sprite.speedY = 0

        if sprite.rect.x <= 0:
            sprite.rect.x = 0

        if sprite.rect.x >= 1336 - sprite.rect.width:
            sprite.rect.x = 1336 - sprite.rect.width

    def calcula_colisao_gol(gol_dir, gol_esq, bola):
        if pygame.sprite.collide_rect(bola, gol_dir):

            if bola.rect.top >= gol_dir.rect.top:
                p1.score += 1
                gol.play()

                reset()

            elif bola.rect.bottom >= gol_dir.rect.top:
                bola.rect.bottom = gol_esq.rect.top
                bola.speedX = -bola.speedX
                bola.speedY = -bola.speedY

        if pygame.sprite.collide_rect(bola, gol_esq):

            if bola.rect.top >= gol_esq.rect.top:
                p2.score += 1
                gol.play()

                reset()

            elif bola.rect.bottom >= gol_esq.rect.top:
                bola.rect.bottom = gol_esq.rect.top
                bola.speedX = -bola.speedX
                bola.speedY = -bola.speedY

    while True:
        surf.fill(BLACK)

        events = pygame.event.get()

        # inicia as variaveis para os placares
        placarEsquerda = p1.score
        placarDireita = p2.score

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
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and (p1.score >= 7 or p2.score >= 7):
                p1.score = 0
                p2.score = 0

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
            surf.blit(p1.image, p1.rect)
            surf.blit(p2.image, p2.rect)
            surf.blit(jabulani.image, jabulani.rect)
            surf.blit(startScreen.image, [DISPLAY_X / 10, DISPLAY_X / 10])

        # sai da tela inicial e comeca o jogo
        else:

            # calculando colisoes
            for sprite in sprites:

                calcula_colisao_chao(sprite)

                # colisao player com bola
                calcula_colisao_p_bola(p1, p2, jabulani)

                # colisões com o gol, toca o som, aumenta o placar, e reseta todos os sprites para a posicao inicial,
                # com, velocidade X e Y = 0

                calcula_colisao_gol(golDir, golEsq, jabulani)

                # gravidade, e atrito na bola
                jabulani.speedY += GRAVITY / 20
                p1.speedY += GRAVITY / 30
                p2.speedY += GRAVITY / 30
                jabulani.speedX /= ATRITO

                # para garantir que os sprites nao fiquem patinando pelo campo
                if 0.1 >= jabulani.speedX >= -0.5:
                    jabulani.speedX = 0

                p1.speedX /= ATRITO_P
                if 0.1 >= p1.speedX >= -0.5:
                    p1.speedX = 0

                p2.speedX /= ATRITO_P
                if 0.1 >= p2.speedX >= -0.5:
                    p2.speedX = 0

            sprites.update()

            # Adicionando as imagens do jogo
            surf.blit(backGround.image, [0, 0])  # imagem de fundo
            surf.blit(p1.image, p1.rect)  # player 1
            surf.blit(p2.image, p2.rect)  # player 2
            surf.blit(jabulani.image, jabulani.rect)  # bola
            surf.blit(cancha.image, [0, 672])  # campo
            surf.blit(golEsq.image, [0, 320])  # gol da esquerda
            surf.blit(golDir.image, [1177, 320])  # gol da direita

            # Adicionando os placares:
            textoEsquerda = fontScore.render("Ribamar: {0}".format(placarEsquerda), True, YELLOW)
            textoDireita = fontScore.render("Messi Careca: {0}".format(placarDireita), True, YELLOW)
            surf.blit(textoEsquerda, (10, 0))
            surf.blit(textoDireita, (1045, 0))

            # Adicionando a tela final do jogo:
            if p1.score >= 7:
                surf.fill(BLACK)
                surf.blit(endScreen.image, [DISPLAY_X / 5, DISPLAY_X / 5])
                textoVencedor1 = fontInstructions.render("Jogador 1 venceu!", True, WHITE)
                textoInstrucoes1 = fontInstructions.render("Pressione 'Enter' para jogar novamente", True, WHITE)
                textoInstrucoes2 = fontInstructions.render("Pressione 'ESC' para sair", True, WHITE)
                surf.blit(p1.image, (DISPLAY_X * 0.47, DISPLAY_X / 3))
                surf.blit(textoVencedor1, [DISPLAY_X * 4 / 9, DISPLAY_X / 3])
                surf.blit(textoInstrucoes1, [DISPLAY_X * 4 / 11, DISPLAY_X * 3 / 5])
                surf.blit(textoInstrucoes2,
                          [(DISPLAY_X / 2) - (textoInstrucoes2.get_rect().width / 2), DISPLAY_X * 11 / 17])

            if p2.score >= 7:
                surf.fill(BLACK)
                surf.blit(endScreen.image, [DISPLAY_X / 5, DISPLAY_X / 5])
                textoVencedor1 = fontInstructions.render("Jogador 2 venceu!", True, WHITE)
                textoInstrucoes1 = fontInstructions.render("Pressione 'Enter' para jogar novamente", True, WHITE)
                textoInstrucoes2 = fontInstructions.render("Pressione 'ESC' para sair", True, WHITE)
                surf.blit(p2.image, (DISPLAY_X * 0.47, DISPLAY_X / 3))
                surf.blit(textoVencedor1, [DISPLAY_X * 4 / 9, DISPLAY_X / 3])
                surf.blit(textoInstrucoes1, [DISPLAY_X * 4 / 11, DISPLAY_X * 3 / 5])
                surf.blit(textoInstrucoes2,
                          [(DISPLAY_X / 2) - (textoInstrucoes2.get_rect().width / 2), DISPLAY_X * 11 / 17])

        pygame.display.flip()  # faz o update da imagine, usando troca de memory bugger


if __name__ == '__main__':
    main()
