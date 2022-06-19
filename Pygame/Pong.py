import pygame
import random
import time
from pygame.locals import*
pygame.init()
scoreone=0
scoretwo=0
green=((0,255,0))
blue=((0,0,255))
oney=450
twoy=450
screen=pygame.display.set_mode((900,900))
blue=(0,0,255)
aqua=(0,255,255)
color=[blue,aqua]
x=450
y=450
blue,aqua=aqua,blue
xco=1
yco=1
onex=0
twox=850
xchange=random.randint(1,5)
ychange=random.randint(1,5)
rpd = 0
rpu = 0
rpdo = 0
rpuo = 0
pygame.draw.circle(screen,color[0] ,(x,y),25)
def w(msg,xr,yr,color):
        f=pygame.font.SysFont("freesans",32)
        m=f.render(msg,False,color)
        screen.blit(m,(xr,yr))
def wewillwewillrockyu(msg,xr,yr,color):
        f=pygame.font.SysFont("freesans",32)
        m=f.render(msg,False,color)
        screen.blit(m,(xr,yr))
def briandea(msg,xr,yr,color):
        f=pygame.font.SysFont("freesans",32)
        m=f.render(msg,False,color)
        screen.blit(m,(xr,yr))
def briandea2(msg,xr,yr,color):
        f=pygame.font.SysFont("freesans",32)
        m=f.render(msg,False,color)
        screen.blit(m,(xr,yr))
while True:
        pygame.display.update()
        screen.fill((0,0,0))
        pygame.draw.rect(screen,green,(onex,oney,50,150))
        pygame.draw.rect(screen,green,(twox,twoy,50,150))
        for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit()
                        exit()
                elif event.type == KEYDOWN:
                        if event.key == K_s:
                                rpd = 1
                        if event.key == K_w:
                                rpu = 1
                        if event.key == K_DOWN:
                                rpdo = 1
                        if event.key == K_UP:
                                rpuo = 1
                elif event.type == KEYUP:
                        if event.key == K_s:
                                rpd = 0
                        if event.key == K_w:
                                rpu = 0
                        if event.key == K_DOWN:
                                rpdo = 0
      
                        if event.key == K_UP:
                                rpuo = 0
        if rpuo == 1:
               twoy=twoy-10
        if rpdo == 1:
               twoy=twoy+10
        if rpu == 1:
               oney=oney-10
        if rpd == 1:
               oney=oney+10
        w("player one score: "+str(scoreone),100,0,green)
        wewillwewillrockyu("player two score: "+str(scoretwo),500,0,green)
        if oney<=0:
                oney= 0
        if oney >=900-150:
                oney=900-150
        if twoy<=0:
                twoy= 0
        if twoy >=900-150:
                twoy=900-150
        if x<50 and oney<=y<=oney+150:
                aqua,blue=blue,aqua
                xco=1
                xchange=-xchange
        if x>850 and twoy<=y<=twoy+150:
                blue,aqua=aqua,blue
                xco=-1
                xchange=-xchange
        if y<0:
                aqua,blue=blue,aqua
                yco=1
                ychange=-ychange
        if y>900:
                blue,aqua=aqua,blue
                yco=-1
                ychange=-ychange
        if x<0:
                scoretwo=scoretwo+1
                print(scoretwo)
                x=450
                y=450
        if x>900:
                scoreone=scoreone+1
                print(scoreone)
                x=450
                y=450
        if x<=onex  and x>=onex-50:
                if y in range(oney,oney+150):
                        blue,aqua=aqua,blue
                        xco=1
                        xchange=-xchange
        if x<=twox and x>=twox-50:
                if y in range(twoy,twoy+150):
                        aqua,blue=blue,aqua
                        xco=-1
                        xchange=-xchange         
        pygame.draw.circle(screen,aqua ,(x,y),25)
        pygame.display.update()
        x=x+xco+xchange
        y=y+yco+ychange
        if scoreone ==10:
                briandea("player one won",450,450,blue)
                exit()
        if scoretwo ==10:
                briandea2("player two won",450,450,blue)
                exit()
