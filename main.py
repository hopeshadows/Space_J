import pygame
import time
from random import randint

pygame.init()

fps=60; fpsclock=pygame.time.Clock(); screen=pygame.display.set_mode((1000,600)); pygame.display.set_caption("Space Joter")

start_screen=1
pause=0
play_screen=0
settings_screen=0
credit_sreen=0
position_credits=-170

bg = pygame.image.load("data\\bg\\bg.png")
menu = pygame.image.load("data\\font\\menu.png")
settings = pygame.image.load("data\\font\\settings.png"); select = pygame.image.load("data\\font\\select.png"); leave = pygame.image.load("data\\font\\leave.png"); pause_bg = pygame.image.load("data\\bg\\pause.png")

#Score
fichier = open("data\\data.txt", "r"); score_max = fichier.read(); fichier.close; score=0

#Player
pl = pygame.image.load("data\\None.png"); hbp = pygame.Rect(50,250, 111, 70)
X = 50; Y = 250; step=5

#Astéroides
rect1 = pygame.Rect(1000,100, 80, 80); rect2 = pygame.Rect(1300,400, 48, 48)
rect3 = pygame.Rect(1600,200, 80, 80); rect4 = pygame.Rect(1600,200, 48, 48)

enemie1 = pygame.image.load("data\\enemy\\as.png"); enemie2 = pygame.image.load("data\\enemy\\cs.png")
enemie3 = pygame.image.load("data\\enemy\\es.png"); enemie4 = pygame.image.load("data\\enemy\\gs.png")

a=1000; b=randint(0,5)*100
c=1300; d=randint(0,10)*50
e=1500; f=randint(0,5)*100
g=1800; h=randint(0,10)*50

diffilculte=10; diffilculte_select=2; vitesse=2

#Explosion
ex=0; frame=10

while True:
    screen.blit(bg,(0,0))
    screen.blit(pl,(X,Y))

    #Astéroides boucle
    rect1.center = ((a+10)-vitesse,b)
    rect2.center = (c-vitesse,d)
    rect3.center = ((e+10)-vitesse,f)
    rect4.center = (g-vitesse,h)

    screen.blit(enemie1, (a-vitesse, b)); screen.blit(enemie2, (c-vitesse, d))
    screen.blit(enemie3, (e-vitesse, f)); screen.blit(enemie4, (g-vitesse, h))

    a=a-vitesse; c=c-vitesse*0.9; e=e-vitesse; g=g-vitesse*0.95

    if a<-100: a=1000; b=randint(0,2)*100
    if c<-48: c=1000; d=randint(0,5)*50
    if e<-100: e=1000; f=randint(3,5)*100
    if g<-48: g=1000; h=randint(6,10)*50

    #Obligation
    key_input = pygame.key.get_pressed()
    for eve in pygame.event.get():
        mouse = pygame.mouse.get_pos()
        if eve.type==pygame.QUIT or eve.type == pygame.MOUSEBUTTONDOWN and 940<mouse[0]<990 and 540<mouse[1]<590:
            pygame.quit()
            del pygame, time
            exit()
    
    #Pause
    if pause==1:
        screen.blit(pause_bg,(0,0))
        play_screen=0
        vitesse=0
        if key_input[pygame.K_RETURN]==True:
            pause=0
            play_screen=1
            vitesse=diffilculte

    #Play screen
    if play_screen==1:
        hbp.center = (X,Y)
        if key_input[pygame.K_LEFT]:
            X=X-step
        if key_input[pygame.K_RIGHT]:
            X=X+step
        if key_input[pygame.K_UP]:
            Y=Y-step
            pl = pygame.image.load("data\\player\\player3.png")
        if key_input[pygame.K_DOWN]:
            Y=Y+step
            pl = pygame.image.load("data\\player\\player2.png")
        if key_input[pygame.K_UP] == False and key_input[pygame.K_DOWN] == False:
            pl = pygame.image.load("data\\player\\player1.png")

        #Max screen
        if key_input[pygame.K_UP] == True or key_input[pygame.K_DOWN] == True or key_input[pygame.K_LEFT]==True or key_input[pygame.K_RIGHT]==True:
            if X<0: X=0
            if Y<0: Y=0
            if X>896: X=896
            if Y>516: Y=516

        #Pause
        if key_input[pygame.K_ESCAPE]==True:
            pause=1


        #Collisions
        collide = hbp.colliderect(rect1) or hbp.colliderect(rect2) or hbp.colliderect(rect3) or hbp.colliderect(rect4)
        if collide and score>50:
            play_screen=0
            ex=1
            if int(score_max)<score:
                fichier = open("data\\data.txt", "w")
                fichier.write(str(score))
                fichier.close
                fichier = open("data\\data.txt", "r")
                score_max = fichier.read()
                fichier.close
            score=0

            hbp.center = (0,-100)
            pl = pygame.image.load("data\\None.png")
            a=1000
            c=1250
            e=1500
            g=1750
            vitesse=2

        #Score
        text = pygame.font.SysFont("Segoe UI Black",50).render(str(score),1,(255,255,255))
        screen.blit(text,(20,0))
        score=score+diffilculte_select

################################ ANIMATION EXPLOSION #####################################
    if ex==1:
        if frame%10==0 and frame<=50:
            explosion = pygame.image.load("data\\sprites\\explosion"+str(frame//10)+".png")
            frame=frame+2
        elif frame==60:
            ex=0
            frame=10
            start_screen=1
        else:
            screen.blit(explosion,(X,Y))
            frame=frame+2
##########################################################################################

    #Menu
    if start_screen==1:
        screen.blit(menu,(395,410)); screen.blit(leave,(940,540))
        pb = pygame.font.SysFont("Segoe UI Black",25).render("Personal Best: " +score_max,1,(255,255,255))
        screen.blit(pb,(390,10))
        if eve.type == pygame.MOUSEBUTTONDOWN and 457<mouse[0]<558 and 410<mouse[1]<455 or key_input[pygame.K_RETURN]:
            start_screen=0
            play_screen=1
            vitesse=diffilculte
            pl = pygame.image.load("data\\player\\player1.png")
            X = 50
            Y = 250
        if eve.type == pygame.MOUSEBUTTONDOWN and 435<mouse[0]<580 and 534<mouse[1]<573:
            test = pygame.image.load("data\\font\\credits.png")
            credit_sreen=1
            start_screen=0
        if eve.type == pygame.MOUSEBUTTONDOWN and 416<mouse[0]<600 and 472<mouse[1]<524:
            settings_screen=1
            start_screen=0

    #Settings
    if settings_screen==1:
        if eve.type == pygame.MOUSEBUTTONDOWN and 279<mouse[0]<367 and 119<mouse[1]<257:
            diffilculte=7
            diffilculte_select=1
        elif eve.type == pygame.MOUSEBUTTONDOWN and 450<mouse[0]<550 and 119<mouse[1]<257:
            diffilculte=10
            diffilculte_select=2
        elif eve.type == pygame.MOUSEBUTTONDOWN and 633<mouse[0]<721 and 119<mouse[1]<257:
            diffilculte=15
            diffilculte_select=3
        if key_input[pygame.K_ESCAPE]:
            settings_screen=0
            start_screen=1
        if diffilculte_select==1:
            screen.blit(select,(310,274))
        elif diffilculte_select==2:
            screen.blit(select,(487,274))
        else:
            screen.blit(select,(664,274))
        screen.blit(settings,(0,0))

    #Credit
    if credit_sreen==1:
        if key_input[pygame.K_ESCAPE]:
            position_credits=-170
            credit_sreen=0
            start_screen=1
        elif position_credits<663:
            screen.blit(test, (395, position_credits))
            position_credits+=vitesse
        else:
            position_credits=-170
            credit_sreen=0
            start_screen=1

    pygame.display.flip()
    fpsclock.tick(fps)
