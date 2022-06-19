import pygame
import random
import time
pygame.init()
from pygame.locals import*
yellow=((255,255,0))
green=((0,255,0))
r=((255,0,0))
o=((255,165,0))
wh=((255,255,255))
b=((0,0,0))
t=((210,180,140))
g=(32,216,47)
xt=500
yt=500
x=500
y=500
gap=200
xe=925
score=0
screen=pygame.display.set_mode((1000,1000))
ychange = 1
h=random.randint(0,800)
def w(msg,xr,yr,r):
        f=pygame.font.SysFont("freesans",32)
        m=f.render(msg,False,r)
        screen.blit(m,(xr,yr))
def youlose(msg,xt,yt,r):
        f=pygame.font.SysFont("freesans",32)
        m=f.render(msg,False,r)
        screen.blit(m,(xt,yt))
def flappy():
        pygame.draw.circle(screen,yellow,(x,y),50)
        pygame.draw.circle(screen,o,(x+50,y),15)
        pygame.draw.circle(screen,wh,(x+10,y),20)
        pygame.draw.circle(screen,b,(x+10,y),15)
        pygame.draw.circle(screen,t,(x-40,y+5),25)
        pygame.draw.circle(screen,t,(x-50,y+5),25)
def bg():
        screen.fill((0,255,255))
        pygame.draw.rect(screen,g,(0,900,1000,100))
        pygame.draw.circle(screen,wh,(100,120),50)
        pygame.draw.circle(screen,wh,(130,120),50)
        pygame.draw.circle(screen,wh,(140,130),50)
        pygame.draw.circle(screen,wh,(400,230),50)
        pygame.draw.circle(screen,wh,(430,220),50)
        pygame.draw.circle(screen,wh,(440,230),50)
        pygame.draw.circle(screen,wh,(140,130),50)
        pygame.draw.circle(screen,wh,(810,230),50)
        pygame.draw.circle(screen,wh,(800,220),50)
        pygame.draw.circle(screen,wh,(860,230),50)
while True:
        pygame.display.update()
        screen.fill((0,0,0))
        bg()
        pygame.draw.rect(screen,green,(xe,0,75,h))
        flappy()
        pygame.draw.rect(screen,green,(xe,h+gap,75,1000-h-gap))
        y = y +ychange
        xe=xe-1
        w(str(score),10,10,r)
        if xe==0:
                h=random.randint(0,800)
                xe=925
        if x+50==xe and 0<y<h:
                print('collision')
                youlose(str('YOU lOSE'),500,500,r)
                pygame.display.update()
                time.sleep(1)
                quit()
        if xe<=x<=xe+75 and h+gap<y<1000:
                print('collision')
                youlose(str('YOU lOSE'),500,500,r)
                pygame.display.update()
                time.sleep(1)
                quit()
        if xe<=x<=xe+75 and h+gap<y+50<1000:
                print('collision')
                youlose(str('YOU lOSE'),500,500,r)
                pygame.display.update()
                time.sleep(1)
                quit()
        if xe<=x<=xe+75 and 0<y-50<h:
                print('collision')
                youlose(str('YOU lOSE'),500,500,r)
                pygame.display.update()
                time.sleep(1)
                quit()
        if xe==450:
                score=score+1
        if y==0:
                youlose(str('YOU lOSE'),500,500,r)
                pygame.display.update()
                time.sleep(1)
                quit()
        if y==1000:
                youlose(str('YOU lOSE'),500,500,r)
                pygame.display.update()
                time.sleep(1)
                quit()
        for event in pygame.event.get():
                if event.type==QUIT:
                        pygame.quit()
                        exit()
                if event.type==KEYDOWN:
                        if event.key==K_SPACE:
                                ychange=-2
                if event.type==KEYUP:
                        if event.key==K_SPACE:
                                ychange=1
