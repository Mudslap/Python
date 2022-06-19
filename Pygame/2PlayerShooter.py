import pygame
import random
import time
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((500,500))
totaltime=0
blah=100
class Guy:
    def __init__(self):
        self.x=400
        self.y=400
        self.speedx=0
        self.speedy=0
        self.color=(0,0,255)
    def draw(self):
        pygame.draw.rect(screen,self.color,(self.x,self.y,20,20))
    def movex(self):
        self.x=self.x+self.speedx
    def movey(self):
        self.y=self.y+self.speedy
guy=Guy()
class Guy2:
    def __init__(self):
        self.x=400
        self.y=300
        self.speedx=0
        self.speedy=0
        self.color=(255,0,0)
    def draw(self):
        pygame.draw.rect(screen,self.color,(self.x,self.y,20,20))
    def movex(self):
        self.x=self.x+self.speedx
    def movey(self):
        self.y=self.y+self.speedy
gy=Guy2()

        
class ShooterLeft:
    def __init__(self):
        self.x=0
        self.y=20
        self.yspeed=1
    def draw(self):
        pygame.draw.rect(screen,(255,165,0),(self.x,self.y,20,40))
    def movey(self):
        self.y=self.y+self.yspeed
shooter1=ShooterLeft()
class bulletleft:
    def __init__(self):
        self.x=shooter1.x+20
        self.y=shooter1.y+25
        self.speedx=2
    def draw(self):
        pygame.draw.rect(screen,(255,165,0),(self.x,self.y,10,5))
    def move(self):
        self.x += self.speedx
bulletleftlist=[]

string =''

def lose(text,x,y,size):
    font=pygame.font.SysFont('freesans',size)
    msg=font.render(text,True,((255,0,0)))
    screen.blit(msg,(x,y))
def text(msg,x,y,size):
    fontobj=pygame.font.SysFont("freesans",size)
    msgobj=fontobj.render(msg,False,((0,0,0)))
    screen.blit(msgobj,(x,y))
def prgram():
    start= time.time()
    st= time.time()
    death=0
    global string
    while True:
        pygame.display.update()
        screen.fill((53,60,81))
        e=time.time()
        guy.draw()
        guy.movex()
        guy.movey()
        lose("TIME: "+str(round(e-start,2)),0,0,40)
        text(string,guy.x-(len(string)*10)+32,guy.y-20,20)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_w:
                    guy.speedy=-2
                if event.key == K_s :
                    guy.speedy=2
                if event.key == K_a:
                    guy.speedx=-2
                if event.key == K_d:
                    guy.speedx=2
            elif event.type == KEYUP:
                if event.key == K_w:
                    guy.speedy=0
                if event.key == K_s:
                    guy.speedy=0
                if event.key == K_a:
                    guy.speedx=0
                if event.key == K_d:
                    guy.speedx=0
        if guy.y>=450:
            guy.y=450
        if guy.y<=30:
            guy.y=30
        if guy.x>=450:
            guy.x=450
        if guy.x<=30:
            guy.x=30

            
        shooter1.draw()
        shooter1.movey()
        if shooter1.y>=440:
            shooter1.yspeed=-1
        if shooter1.y<=20:
            shooter1.yspeed=1
        randomleft=random.random()*10
        end=time.time()
        if end-st>0.1*randomleft:
            bulletleftlist.append(bulletleft())
            st=time.time()
        for b in bulletleftlist:
            b.draw()
            b.move()
            if b.x>=500:
                bulletleftlist.remove(b)

            if b.x==guy.x and guy.y<b.y<guy.y+20:
                death=death+1
                guy.x=240
                guy.y=240
                lose("Death "+str(death),180,200,50)
                pygame.display.update()
                time.sleep(1)
                if death==3:
                    totaltime=round(e-start,2)
                    
                    blah=50
                    global totaltime
                    global blah
                    bulletleftlist.remove(b)
                    
                    lose("You Lost", 180,250,45)
                    pygame.display.update()
                    time.sleep(1)
                    menu()
def prgrm2():
    start= time.time()
    st= time.time()
    p1death=0
    p2death=0
    global string
    while True:
        pygame.display.update()
        screen.fill((53,60,81))
        e=time.time()
        player1lives=3-p1death
        player2lives=3-p2death
        guy.draw()
        gy.draw()
        guy.movex()
        gy.movex()
        guy.movey()
        gy.movey()
        lose("TIME: "+str(round(e-start,2)),0,0,40)
        text(string,guy.x-(len(string)*10)+32,guy.y-20,20)
        lose("Player 1 Lives:"+str(player1lives),0,50,30)
        lose("Player 2 Lives:"+str(player2lives),250,50,30)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_w:
                    guy.speedy=-2
                if event.key == K_s :
                    guy.speedy=2
                if event.key == K_a:
                    guy.speedx=-2
                if event.key == K_d:
                    guy.speedx=2

                if event.key == K_UP:
                    gy.speedy=-2
                if event.key == K_DOWN :
                    gy.speedy=2
                if event.key == K_LEFT:
                    gy.speedx=-2
                if event.key == K_RIGHT:
                    gy.speedx=2
            elif event.type == KEYUP:
                if event.key == K_w:
                    guy.speedy=0
                if event.key == K_s:
                    guy.speedy=0
                if event.key == K_a:
                    guy.speedx=0
                if event.key == K_d:
                    guy.speedx=0


                if event.key == K_UP:
                    gy.speedy=0
                if event.key == K_DOWN:
                    gy.speedy=0
                if event.key == K_LEFT:
                    gy.speedx=0
                if event.key == K_RIGHT:
                    gy.speedx=0
        if guy.y>=450:
            guy.y=450
        if guy.y<=30:
            guy.y=30
        if guy.x>=450:
            guy.x=450
        if guy.x<=30:
            guy.x=30

        if gy.y>=450:
            gy.y=450
        if gy.y<=30:
            gy.y=30
        if gy.x>=450:
            gy.x=450
        if gy.x<=30:
            gy.x=30

##Shooter
        shooter1.draw()
        shooter1.movey()
        if shooter1.y>=440:
            shooter1.yspeed=-1
        if shooter1.y<=20:
            shooter1.yspeed=1
        randomleft=random.random()*10
        end=time.time()
        if end-st>0.1*randomleft:
            bulletleftlist.append(bulletleft())
            st=time.time()
##Player1 Death
        for b in bulletleftlist:
            b.draw()
            b.move()
            if b.x>=500:
                bulletleftlist.remove(b)

            if b.x==guy.x and guy.y<b.y<guy.y+20:
                p1death=p1death+1
                guy.x=240
                guy.y=240
                lose("Player 1 Deaths: "+str(p1death),100,200,50)
                pygame.display.update()
                time.sleep(1)
                if p1death==3:
                    totaltime=round(e-start,2)
                    
                    blah=50
                    global totaltime
                    global blah
                    bulletleftlist.remove(b)
                    
                    lose("Player 2 Won", 180,250,45)
                    pygame.display.update()
                    time.sleep(1)
                    menu()
##Player 2 Death
        for b in bulletleftlist:
            b.draw()
            b.move()
            if b.x>=500:
                bulletleftlist.remove(b)

            if b.x==gy.x and gy.y<b.y<gy.y+20:
                p2death=p2death+1
                gy.x=240
                gy.y=240
                lose("Player 2 Deaths: "+str(p2death),100,200,50)
                pygame.display.update()
                time.sleep(1)
                if p2death==3:
                    totaltime=round(e-start,2)
                    
                    blah=50
                    global totaltime
                    global blah
                    bulletleftlist.remove(b)
                    
                    lose("Player 1 Won", 180,250,45)
                    pygame.display.update()
                    time.sleep(1)
                    menu()

                        
def menu():
    global highscore
    highscore=totaltime
    nameposx=220
    nameposy=310 
    global string
    while True:
        text(string,nameposx,nameposy,30)
        pygame.display.update()
        screen.fill((53,60,81))
        lose("Bullet Dodger",120,100,45)
        pygame.draw.rect(screen,((0,255,150)),(140,160,210,55))
        lose("1 player mode",150,170,30)
        pygame.draw.rect(screen,((0,255,150)),(140,220,210,55))
        lose("2 player mode",150,230,30)
        pygame.draw.rect(screen,((255,255,255)),(120,300,270,50))
        text("Name: ",130,310,30)
        text("High Score: "+str(highscore),blah,20,50)
        
        for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    exit()
                elif event.type == KEYDOWN:
                    keyk=chr(event.key)
                   
                        
                    if len(string)<=6:
                        string += keyk
                    if len(string)==0:
                        string=="Guest"
                    if event.key==K_BACKSPACE:
                        string=string[:-2]
                    
                elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                    x,y = event.pos

                    if x in range(140,350) and y in range(160,215):
                        prgram()
                    if x in range(140,350) and y in range(160,275):
                        prgrm2()
                    if x in range(10,90) and y in range(10,90):
                        settings()
menu()
