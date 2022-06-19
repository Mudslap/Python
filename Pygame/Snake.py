import pygame
import random
import time
from pygame.locals import *
pygame.init()
foodx=(random.randint(0,900 )//10)*10
foody=(random.randint(0,900 )//10)*10
snakex=(random.randint(0,900) //10)*10
snakey=(random.randint(0,900) //10)*10
red=((255,0,0))
green=((0,255,0))
down=0
up=0
right=0
left=0
speed=15
screen=pygame.display.set_mode((900,900))
fpsclock = pygame.time.Clock()
snakelist=[]
points=0
def point(msg,x,y,color):
        fontobj=pygame.font.SysFont("freesans",32)
        msgobj=fontobj.render(msg,False,color)
        screen.blit(msgobj,(x,y))
def tail(msg,x,y,color):
        fontobj=pygame.font.SysFont("freesans",32)
        msgobj=fontobj.render(msg,False,color)
        screen.blit(msgobj,(x,y))
while True:
        snakelist.insert(0,[snakex,snakey])
        pygame.draw.rect(screen, red, (foodx, foody, 10, 10))
        for segment in snakelist:
                pygame.draw.rect(screen, green, segment+[10,10])
        pygame.display.update()
        snakelist.pop()
        fpsclock.tick(speed)
        screen.fill((0,0,0))
        point("points: "+str(points),700,70,red)
        for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit()
                        exit()
                elif event.type == KEYDOWN:
                        if event.key == K_DOWN and not(up):
                                down=1
                                left=0
                                up=0
                                right=0
                        if event.key == K_UP and not(down):
                                up=1
                                left=0
                                right=0
                                down=0
                        if event.key == K_LEFT and not(right):
                                left=1
                                up=0
                                right=0
                                down=0
                        if event.key == K_RIGHT:
                                right=1
                                up=0
                                left=0
                                down=0
        if down:
                snakey = snakey+10
        if right:
                snakex = snakex+10
        if left:
                snakex = snakex-10
        if up:
                snakey = snakey-10
        if snakex==foodx and snakey==foody:
                points=points+1
                snakelist.insert(0,[snakex,snakey])
                foodx=(random.randint(0,900) //10)*10
                foody=(random.randint(0,900 )//10)*10
        if snakex==0 or snakex==900:
                exit()
        if snakey==0 or snakey==900:
                exit()
        if [snakex,snakey] in snakelist[1:]:
                tail("You Touched Your Tail!",450,450,red)
                time.sleep(5)
                exit()
        if points==10:
                speed=speed+10
                segment=1
                fpsclock(speed)
