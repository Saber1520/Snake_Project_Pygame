import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()


pygame.mixer.music.set_volume(0.05)
musica_de_fundo = pygame.mixer.music.load('one_0.mp3')
pygame.mixer.music.play(-1)

sound_collision = pygame.mixer.Sound('smw_coin.wav')


altura = 480
largura = 640
largura_objeto = 20
loop = True
x_player = int(largura/2) - largura_objeto/2
y_player = int(altura/2) - 50/2

velocidade = 10
x_controle = velocidade
y_controle = 0



x_apple = randint(40, 600)
y_apple = randint(50, 430)




pontos = 0
fonte = pygame.font.SysFont("arial", 20, bold=True,italic=True)


relogio = pygame.time.Clock()

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Mover Objeto")

lista_corpo = []
comprimento = 5
morreu = False

def corpo(lista_corpo):
    for XeY in lista_corpo:
        pygame.draw.rect(tela,(127,255,212), (XeY[0],XeY[1], largura_objeto, 20))

def restart_game():
    global pontos,velocidade,comprimento,x_player,y_player,lista_corpo,lista_cabeca,x_apple,y_apple,morreu,vitoria
    pontos = 0
    velocidade = 10
    comprimento = 5
    x_player = int(largura//2)//10*10
    y_player = int(altura//2)//10*10
    lista_corpo = []
    lista_cabeca = []
    x_apple = (randint(40, 600))//10*10
    y_apple = (randint(50, 430))//10*10
    morreu = False
    vitoria = False

while loop:
    tela.fill((79,79,79))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            loop = False
            pygame.quit()
            exit()
        
        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = -velocidade
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = velocidade

    x_player += x_controle
    y_player += y_controle

    if y_player < 0:
        y_player = altura
    if y_player > altura:
        y_player = 0
    if x_player > largura:
        x_player = 0
    if x_player < 0:
        x_player = largura
    
    player = pygame.draw.rect(tela,(127,255,212), (x_player, y_player, largura_objeto, 20))
    apple = pygame.draw.rect(tela,(255, 0, 0), (x_apple, y_apple, largura_objeto, 20))
    
    if player.colliderect(apple):

        x_apple = (randint(40, 600))//10*10
        y_apple = (randint(50, 430))//10*10
        pontos += 1
        sound_collision.play()
        comprimento += 1
        velocidade += 0.1
        if pontos == 100:
            fonte3 = pygame.font.SysFont('arial', 20, bold=True, italic=True)
            mensagem_vitoria = 'Parabéns por completar o jogo!! Aperte R para reiniciar.'
            texto_formatado3 = fonte3.render(mensagem_vitoria, True,(0,0,0))
            ret_texto3 = texto_formatado3.get_rect()
        
            vitoria = True
            while vitoria:
                tela.fill((79,79,79))
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        exit()
                    if event.type == KEYDOWN:
                        if event.key == K_r:
                            restart_game()
                ret_texto3.center = (largura//2, altura//2)
                tela.blit(texto_formatado3, ret_texto3)
                pygame.display.update()

    
    lista_cabeca = []
    lista_cabeca.append(x_player)
    lista_cabeca.append(y_player)

    lista_corpo.append(lista_cabeca)

    if lista_corpo.count(lista_cabeca) > 1:
        fonte2 = pygame.font.SysFont('arial', 20, bold=True, italic=True)
        mensagem_morte = 'Você morreu!! Aperte R para jogar novamente'
        texto_formatado2 = fonte2.render(mensagem_morte, True,(0,0,0))
        ret_texto = texto_formatado2.get_rect()

        morreu = True
        while morreu:
            tela.fill((79,79,79))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        restart_game()
            ret_texto.center = (largura//2, altura//2)
            tela.blit(texto_formatado2, ret_texto)
            tela.blit(texto_formatado, (450, 50))
            pygame.display.update()
    if len(lista_corpo) > comprimento:
        del lista_corpo[0]


    corpo(lista_corpo)
    

    tela.blit(texto_formatado, (450, 50))
    pygame.display.update()
    relogio.tick(30)
