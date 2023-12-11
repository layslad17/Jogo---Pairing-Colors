import pygame, random
from pygame.locals import MOUSEBUTTONDOWN, Rect, QUIT
from sys import exit


def confimar(indice):
   global carta1, carta2, carta3, c_cor, situ, score, resposta_certa
   if indice == 0:
       if carta1 == f'maca.{c_cor}.png':
           situ = 'correto'
           score += 1
           resposta_certa.play()
       else:
           situ = 'incorreto'
           resposta_errada.play()
   if indice == 1:
       if carta2 == f'maca.{c_cor}.png':
           situ = 'correto'
           score += 1
           resposta_certa.play()
       else:
           situ = 'incorreto'
           resposta_errada.play()
   if indice == 2:
       if carta3 == f'maca.{c_cor}.png':
           situ = 'correto'
           score += 1
           resposta_certa.play()
       else:
           situ = 'incorreto'
           resposta_errada.play()

def teste_vitoria():
   global score, situ
   if situ == 'correto':
       score += 1
       print('está correto')

def texto():
   global c_cor
   arial = pygame.font.SysFont('arial', 45)
   mens = arial.render(f'selecione o objeto {c_cor}', (0, 0, 0), 250)
   display.blit(mens, (70, 50))

def pontos(score):
   arial = pygame.font.SysFont('arial', 25)
   pnts = arial.render(f' sua pontuação é: {score} ', (0, 0, 0), 250)
   display.blit(pnts, (10, 10))

def testa_pos():
   global situ
   for p in rec:
       if event.type == MOUSEBUTTONDOWN and p.collidepoint(mouse_pos):
           if p == rect1:
               confimar(0)
           if p == rect2:
               confimar(1)
           if p == rect3:
               confimar(2)


def desenhar_tabu():
   pygame.draw.line(display, (105, 105, 105), (235, 150), (235, 560), 10)
   pygame.draw.line(display, (105, 105, 105), (370, 150), (370, 560), 10)
   pygame.draw.line(display, (105, 105, 105), (100, 280), (500, 280), 10)
   pygame.draw.line(display, (105, 105, 105), (100, 420), (500, 420), 10)
   display.blit(pygame.image.load(carta1), (110, 300))
   display.blit(pygame.image.load(carta2), (250, 300))
   display.blit(pygame.image.load(carta3), (390, 300))

pygame.init()

display = pygame.display.set_mode((600, 600), 0, 32)
pygame.display.set_caption("Pairing Colors")

fundo = pygame.image.load("fundo.png")
display.blit(fundo, (0, 0))
cartas = ["maca.azul.png", "maca.rosa.png", "maca.roxo.png", "maca.verde.png", "maca.vermelho.png"]
cor = ['azul', 'rosa', 'roxo', 'verde', 'vermelho']
marca_tabu = [0, 1, 2]
score = 0
situ = 'correto'

resposta_certa = pygame.mixer.Sound('resposta.certa.mp3')
resposta_errada = pygame.mixer.Sound('resposta.errada.mp3')

conjunto = cartas.copy()
carta1 = random.choice(conjunto)
conjunto.remove(carta1)
carta2 = random.choice(conjunto)
conjunto.remove(carta2)
carta3 = random.choice(conjunto)

cores_cartas = []
for carta in [carta1, carta2, carta3]:
   partes = carta.split(".")
   cores_cartas.append(partes[1])

c_cor = random.choice(cores_cartas)

rect1 = Rect((110, 300), (100, 100))
rect2 = Rect((250, 300), (100, 100))
rect3 = Rect((390, 300), (100, 100))

rec = [rect1, rect2, rect3]
estado = 'jogando'

while True:
   mouse_pos = pygame.mouse.get_pos()
   texto()
   pontos(score)
   if estado == 'jogando':
       desenhar_tabu()
       pontos(score)

       for event in pygame.event.get():
           if event.type == QUIT:
               pygame.quit()
               exit()
           if event.type == MOUSEBUTTONDOWN:
               testa_pos()
               if situ == 'correto':
                   # escolher cartas novamente
                   conjunto = cartas.copy()
                   carta1 = random.choice(conjunto)
                   conjunto.remove(carta1)
                   carta2 = random.choice(conjunto)
                   conjunto.remove(carta2)
                   carta3 = random.choice(conjunto)
                   # pegar uma das cores pra ser a correta
                   cores_cartas = []
                   for carta in [carta1, carta2, carta3]:
                       partes = carta.split(".")
                       cores_cartas.append(partes[1])

                   c_cor = random.choice(cores_cartas)
                   # atualizar interface (desenha tabu)
                   display.blit(fundo, (0, 0))
                   desenhar_tabu()

   pygame.display.flip()
