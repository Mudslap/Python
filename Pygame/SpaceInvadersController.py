import pygame
import random
import time
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((800,800))
x1=400
y1=700
bulletx=x1
bullety=700
r=random.randint(-3,3)
yellow=((255,255,255))
class Guy:
    def __init__(guy,x,y,image):
        guy.x=x1
        guy.y=y1
        guy.image=image
        guy.speed=r
    def draw(guy):
        image=pygame.image.load("/home/pi/chungusball.png")
        image=pygame.transform.scale(image,(100,100))
        screen.blit(image,(guy.x,guy.y))
        if guy.x > 800 - 100:
            guy.speed = 0
            guy.x = 800-100
        guy.x += guy.speed
        if guy.x< 0:
            guy.speed = 0
            guy.x = 5
        guy.x+=guy.speed
g=Guy(x1,y1,("/home/pi/chungusball.png"))

class Bullet:
    def __init__(self,x):
        self.color = (255,165,0)
        self.x= x
        self.y= 700
        self.radius = 10
        self.yspeed = -3
        #self.surface= pygame.Surface((40,40))
    def draw(self):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius)
    def move(self):
        self.y += self.yspeed
bulletlist=[]

        

class Zombie:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.image= pygame.image.load('/home/pi/zombie1.png')
        self.image2=pygame.transform.scale(self.image,(70,100))
        self.speed = 2
       
        
    def draw(self):
        
        screen.blit(self.image2,(self.x,self.y))
    def move(self):
        self.x=self.x+self.speed

    

class Zombie_bullet:
    def __init__(self,x,y):
        self.color=(255,0,255)
        self.yspeed= 30
        self.x=x
        self.y=y
    def draw(self):
        pygame.draw.circle(screen,self.color,(self.x,self.y),10)
    def move(self):
        self.y += self.yspeed
zombie_bulletlist=[]


        


        
zombie_list = []
for x in range(20,720,70):
    zombie_list.append(Zombie(x,20))

class Zombie2:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.image= pygame.image.load('/home/pi/zombie2.jpeg')
        self.image2=pygame.transform.scale(self.image,(70,100))
        self.speed = 2
        
    def draw(self):
        screen.blit(self.image2,(self.x,self.y))
    def move(self):
        self.x=self.x+self.speed
        
zombie2_list = []
for x in range(0,700,70):
    zombie2_list.append(Zombie2(x,80))
class Zombie3:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.image= pygame.image.load('/home/pi/zombie3.png')
        self.image2=pygame.transform.scale(self.image,(70,100))
        self.speed = 2
        
    def draw(self):
        screen.blit(self.image2,(self.x,self.y))
    def move(self):
        self.x=self.x+self.speed
        
zombie3_list = []
for x in range(0,700,80):
    zombie3_list.append(Zombie3(x,220))

def lose(text,x,y):
        font=pygame.font.SysFont('freesans',45)
        msg=font.render(text,True,yellow)
        screen.blit(msg,(x,y))

while True:
    pygame.display.update()
    screen.fill((135,206,235))
   
    #draw the G
    g.draw()
    #draw the zombies
    for x in zombie_list:
        x.draw()
        x.move()
        
       
       
        if x.x<=0:
            x.speed=5
        if x.x>=700:
            x.speed=-5
        for b in bulletlist:
            b.draw()
            b.move()
            
            if b.x in range(x.x,x.x+50) and b.y <x.y:
                if x in zombie_list and b in bulletlist:
                    zombie_list.remove(x)
                    bulletlist.remove(b)
                    ex=pygame.image.load('/home/pi/explosion.png')
                    ex=pygame.transform.scale(ex,(70,70))
                    screen.blit(ex,(x.x,x.y))
                    time.sleep(0.05)
            if b.y < -10 and b in bulletlist:
                bulletlist.remove(b)

                
    for z in zombie_bulletlist:
            z.draw()
            z.move()
            if z.x in range(g.x,g.x+55):
                if z.y in range(g.y,800):
                    ex=pygame.image.load('/home/pi/explosion.png')
                    ex=pygame.transform.scale(ex,(70,70))
                    screen.blit(ex,(g.x,g.y))
                    zombie_bulletlist.remove(z)
                    lose("You Lose",400,400)
                    pygame.display.update()
                    time.sleep(1)
                    exit()
                    
            if z.y > 800:
                zombie_bulletlist.remove(z)
                    
    for z in zombie_list:
        if random.randint(1,100) == 1:
            zombie_bulletlist.append(Zombie_bullet(z.x,z.y))
    for z in zombie2_list:
        if random.randint(1,100) == 1:
            zombie_bulletlist.append(Zombie_bullet(z.x,z.y))
    for z in zombie3_list:
        if random.randint(1,100) == 1:
            zombie_bulletlist.append(Zombie_bullet(z.x,z.y))
            
                
                    
    for z in zombie2_list:
        z.draw()
        z.move()
        if z.x<=0:
            z.speed=5
        if z.x>=700:
            z.speed=-5
        for b in bulletlist:
            b.draw()
            b.move()
         
            if b.x in range(z.x,z.x+55) and b.y<z.y:
                if z in zombie2_list and b in bulletlist:
            
                    print('collision')
                    zombie2_list.remove(z)
                    bulletlist.remove(b)
                    ex=pygame.image.load('/home/pi/explosion.png')
                    ex=pygame.transform.scale(ex,(70,70))
                    screen.blit(ex,(z.x,z.y))
                    pygame.display.update()
                    time.sleep(0.05)
            if b.y < -10 and b in bulletlist:
                bulletlist.remove(b)  
                  
    for x in zombie3_list:
        x.draw()
        x.move()
        if x.x<=0:
            x.speed=5

            
        if x.x>=700:
            x.speed=-5
        for b in bulletlist:
            b.draw()
            b.move()
            if b.x in range(x.x,x.x+75) and b.y <x.y:
               if x in zombie3_list and b in bulletlist:
        
                    print('collision')
                    zombie3_list.remove(x)
                    bulletlist.remove(b)
                    ex=pygame.image.load('/home/pi/explosion.png')
                    ex=pygame.transform.scale(ex,(70,70))
                    screen.blit(ex,(x.x,x.y))
                    pygame.display.update()
                    time.sleep(0.05)
                    
            if b.y < -10 and b in bulletlist:
                bulletlist.remove(b)
    if zombie_list==[] and zombie2_list==[] and zombie3_list==[]:
        lose("You Win",400,400)
        pygame.display.update()
        time.sleep(1)
        exit()
                    

    #event getter
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_a:
                g.speed=-5
            if event.key == K_d:
                g.speed = 5
            if event.key== K_SPACE:
                bulletlist.append(Bullet(g.x))
            if event.key== K_l:
                lose("You Win",400,400)
                pygame.display.update()
                time.sleep(1)
                exit()
            if event.key== K_w:
                lose("You lose.",400,400)
                lose("The Air is",400,450)
                lose("poisonous",400,500)
                pygame.display.update()
                time.sleep(1)
                exit()
        elif event.type == KEYUP:
            if event.key == K_a:
                g.speed=0
            if event.key == K_d:
                g.speed=0
            
            
        

