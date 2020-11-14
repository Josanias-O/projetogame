#Etapa 1 - importando pygame e biblioteca Randint

import pygame
from random import randint
pygame.init()

#Etapa 2 - já definindo as variaveis globais do jogo (posso voltar e alterar toda vez q necessario)

x=250
y=100
pos_x = 230
pos_y = 1200
pos_y_a = 600
pos_y_b = 600
pos_y_c = 600
pos_y_d = 600
pos_y_e = 600
tempo = 0
tempo_corrido = 0
velocidade_principal = 50
outra_velocidade = 5

#Etapa 2.1 - anexando as imagens do jogo em variaveis
fundotela = pygame.image.load('imagemfundo.PNG')
carro_principal = pygame.image.load('motogrannde.png')
caminhao = pygame.image.load('big.png')
carro_laranja = pygame.image.load('caryellow.png')
carro_roxo = pygame.image.load('carroroxo.png')
carro_azul = pygame.image.load('carblue.png')
caminhao_rosa = pygame.image.load('caminhaorosa.png')

#Etapa 3- linha abaixo irá criar o temporizador
fonte = pygame.font.SysFont('Chiller',28)
msg = fonte.render('Tempo',False,(128,196,255),(84,130,53))
local_msg = msg.get_rect()
local_msg.center = (680,20)





#Etapa 4- linhas abaixo é criando o tamanho da janela em pixels

janela = pygame.display.set_mode((800,483))
pygame.display.set_caption('Criando meu primeiro jogo no pyhton, Uhuuull :-) ')

#Etapa 5 - linhas abaixo é para criar um loop while (bool), para que a janela permaneça aberta até que alguem feche

janela_aberta = True
while janela_aberta:
    pygame.time.delay(50) #a velocidade de rodagem do veiculo

    for event in pygame.event.get(): #for criado para cair na condição indicada se houver alguma ação (x)
        if event.type == pygame.QUIT:
            janela_aberta = False


#Etapa 6 - abaixo vamos criar uma variavel chamada 'comando' para utilizar as setas do note, com o 'K_'
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_LEFT] and x >=70:
        x -= velocidade_principal
    if comandos[pygame.K_RIGHT] and x <=430:
        x += velocidade_principal

#Etapa 6.1 Vou criar mais um if, para poder detectar a colisão do carro
    if ((x + 40 > pos_x and y +10 >pos_y)):     #colisão direita
        y = 2400


    if (pos_y < -90):      #pos da moto (principal)
        pos_y
    if (pos_y_a <= -90):       #pos do caminhao grande
        pos_y_a = randint(1400,20000)
    if (pos_y_b <= -90):        #pos do carro azul
        pos_y_b = 6500
    if (pos_y_c <= -90):             #pos do carro laranja
        pos_y_c = randint(2400,30000)
    if (pos_y_d <= -80):               #pos do carro roxo
        pos_y_d = randint(3000, 4000)
    if (pos_y_e <= -80):               #pos do caminhao rosa
        pos_y_e = randint(3400,5000)

    if ((x + 80 > pos_x and y +300 >pos_y)):
        y = 1200

    if (pos_y < -40):
        pos_y = randint(800,1000)
    if (pos_y_a <= -90):       #pos do caminhao grande
        pos_y_a = randint(1400,2000)
    if (pos_y_b <= -90):        #pos do carro azul
        pos_y_b = 500
    if (pos_y_c <= -90):             #pos do carro laranja
        pos_y_c = randint(2400,3000)
    if (pos_y_d <= -80):               #pos do carro roxo
        pos_y_d = randint(3000, 3400)
    if (pos_y_e <= -80):               #pos do caminhao rosa
        pos_y_e = randint(3400,4000)

















#Etapa 6.2 - Agora criei o if para o temporizador, ainda dentro do while, para que ele possa fazer a comparação se o temporizador esta correto
    if (tempo <20):
        tempo += 1
    else:
        tempo_corrido += 1
        msg = fonte.render('Tempo: '+str(tempo_corrido), False, (128, 196, 255), (84, 130, 53))
        tempo = 0


#Etapa 7 - linha abaixo vou pedir pro veiculo da pos_y ficar sempre rodando de baixo pra cima
    pos_y -= outra_velocidade
    pos_y_a -= outra_velocidade +2
    pos_y_b -= outra_velocidade +10
    pos_y_c -= outra_velocidade +15
    pos_y_d -= outra_velocidade +20
    pos_y_e -= outra_velocidade


    #linha abaixo utilizada para criar o objeto inicial de circulo, (depois trocamos pela imagem)
    #pygame.draw.circle(janela, (0,198,0), (x,y),50)

#Etapa 8 - utilizada a  função 'blit' para trazer imagens de fundo e de objetos e inserir o carro principal
    janela.blit(fundotela, (0,0))
    janela.blit(carro_principal, (x,y))
    janela.blit((caminhao), (pos_x-65,pos_y_a+5))
    janela.blit(carro_azul, (pos_x-160,pos_y_b))
    janela.blit(carro_laranja, (pos_x+155, pos_y_c-100))
    janela.blit(carro_roxo, (pos_x+255, pos_y_d-800))
    janela.blit(caminhao_rosa, (pos_x+40, pos_y_e+10))
    janela.blit(msg,local_msg)
    pygame.display.update()

pygame.quit()