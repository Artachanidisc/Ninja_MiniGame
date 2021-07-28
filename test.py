from pygame_functions import *
import pygame
import sys
from pygame.locals import *
import math
import random
import time
import pyautogui

screen=screenSize(1800,480,None,None,True) 
# screen = screenSize(1800,480)
setBackgroundImage("back1.png")
setBackgroundImage([["back1.png", "back1.png"]])

agent = makeSprite("1bg.png")
block1 = makeSprite("decx.png")
enemy = makeSprite("eneleft.png")
bullet = makeSprite("fire.png")
enemy = makeSprite("eneleft.png")
build = makeSprite("build.png")
bridge = makeSprite("decx.png")
boss = makeSprite("boss.png")
health5 = makeSprite("health5.png")




addSpriteImage(agent, "2bg.png")
addSpriteImage(agent, "3bg.png")
addSpriteImage(agent, "4bg.png")
addSpriteImage(agent, "5bg.png")
addSpriteImage(agent, "6bg.png")
addSpriteImage(agent, "7bg.png")
addSpriteImage(agent, "8bg.png")
addSpriteImage(agent, "9bg.png")

addSpriteImage(agent, "l1bg.png")
addSpriteImage(agent, "l2bg.png")
addSpriteImage(agent, "l3bg.png")
addSpriteImage(agent, "l4bg.png")
addSpriteImage(agent, "l5bg.png")
addSpriteImage(agent, "l6bg.png")
addSpriteImage(agent, "l7bg.png")
addSpriteImage(agent, "l8bg.png")
addSpriteImage(agent, "l9bg.png")
addSpriteImage(agent, "hit11.png")
addSpriteImage(agent, "hit12.png")
addSpriteImage(agent, "hit11l.png")
addSpriteImage(agent, "hit12l.png")
addSpriteImage(agent, "dmg.png")


addSpriteImage(enemy,"eneright.png")
addSpriteImage(enemy,"done.png")


addSpriteImage(boss, "bossl.png")

addSpriteImage(health5,"health4.png")
addSpriteImage(health5,"health3.png")
addSpriteImage(health5,"health2.png")
# addSpriteImage(health5,"health0.png")

x = 50
y = 400
# bulletImg = pygame.image.load('shuriken.png')
bulletX = x
bulletY = y
# bulletX_change = 15
# bullet_state = "ready"

agentX = 20
agentY = 400       
agentY_change = 0
agentImage = 0     
moveSprite(agent, agentX, agentY)
showSprite(agent)

enemyX = 600
enemyY = 380
moveSprite(enemy, enemyX, enemyY)
showSprite(enemy)


block1X = 200
block1Y = 400
moveSprite(block1, block1X, block1Y)
showSprite(block1)

buildX = 580
buildY = 320
moveSprite(build, buildX, buildY)
showSprite(build)

bridgeX = 1050   
bridgeY = 320
moveSprite(bridge, bridgeX, bridgeY)
showSprite(bridge)

# health5X = 10
# health5Y = 10
# moveSprite(health5, health5X, health5Y)
# showSprite(health5)



def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    moveSprite(bullet, x, y)
    showSprite(bullet)

def move_towards_player(self, player):
    
    dx, dy = player.rect.x - self.rect.x, player.rect.y - self.rect.y
    dist = math.hypot(dx, dy)
    if dist !=0:
      dx, dy = dx / dist, dy / dist

    self.rect.x += dx * 4
    self.rect.y += dy * 4


def move_towards_player_boss(self, player):
    global bossX
    dx, dy = player.rect.x - self.rect.x, player.rect.y - self.rect.y
    dist = math.hypot(dx, dy)
    if dist >20:
      dx, dy = dx / dist, dy / dist

    change= dx * 30
    self.rect.x += change
    bossX+=change

def show_lifes(amount):
    health5X = 10
    health5Y = 10
    moveSprite(health5, health5X, health5Y)
    if amount==5:
        showSprite(health5)
    elif amount<5 and amount>-1:
        changeSpriteImage(health5,1)  
    elif amount<=-1 and amount >=-5:
        changeSpriteImage(health5,2)
    elif amount<-5 and amount >=-10:
        changeSpriteImage(health5,3)
    else:
        hideSprite(health5)          
           
def game_over_text():
    enter_font = pygame.font.Font('freesansbold.ttf', 50) 
    over_font = pygame.font.Font('freesansbold.ttf', 120) 
    over_text = over_font.render("GAME OVER", True, (235, 85, 52))
    screen.blit(over_text, (550,150))
    enter_text = enter_font.render("Press enter to restart", True, (242, 163, 143))
    screen.blit(enter_text, (630,250))

clock = pygame.time.Clock()
bossX = 1300
moveToPlayer= USEREVENT + 1
pygame.time.set_timer(moveToPlayer,1500)
shoot= USEREVENT + 1
pygame.time.set_timer(shoot,1500)  
isJump = False
jumpCount = 10
speed = 23
left = bool
right = bool
run = True
contactMob = bool
contactBoss = bool
overHim=bool
total=bool
scroll=True
scrollCounter=0
bossMove=bool
bossLife=1
move=bool
time_elapsed_since_last_action = 0
clock = pygame.time.Clock()
lifes=5
collided=False
test=False
def game_run():
   global test,collided,lifes,clock,bossLife,move,bossMove,scrollCounter,scroll,total,overHim,contactBoss,contactMob
   global bossX,moveToPlayer,shoot,isJump,jumpCount,speed,left,right, run 
   global bridgeX,bridgeY,buildX,buildY,block1X,block1Y,enemyX,enemyY,agentImage,agentY_change,agentX,agentY
   global bulletX,bulletY,x,y,agent,block1,screen,enemy,bullet,build,bridge,boss,health5
   while run:
    # distanceBoss=abs(bossX-agentX)
    bullet_state="fire"
    scrollBackground(int(-0.1), 0)
    clock.tick(speed)
    contactMob=False
    contactBoss=False
    bossMove=False
    total=False 
    hitByBoss=False 
    bossY = 280
    if lifes<-11 or collided==True:
       while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    test=True
            if test:
                lifes=5
                collided=False
                contactBoss=True
                x = 50
                y = 400
                bulletX = x
                bulletY = y
                agentX = 20
                agentY = 400       
                agentY_change = 0
                agentImage = 0     
                moveSprite(agent, agentX, agentY)
                showSprite(agent)
                killSprite(boss)
                killSprite(bullet)
                test=False

                enemyX = 600
                enemyY = 380
                moveSprite(enemy, enemyX, enemyY)
                showSprite(enemy)

                block1X = 200
                block1Y = 400
                moveSprite(block1, block1X, block1Y)
                showSprite(block1)

                buildX = 580
                buildY = 320
                moveSprite(build, buildX, buildY)
                showSprite(build)

                bridgeX = 1050   
                bridgeY = 320
                moveSprite(bridge, bridgeX, bridgeY)
                showSprite(bridge)
                break    
    for event in pygame.event.get():
        if event.type== shoot and bossLife==0:
            bulletX=bossX
            bulletY=random.randrange(300,400)
            moveSprite(bullet,bulletX-15,bulletY)
            showSprite(bullet)
            move_towards_player_boss(boss,agent)
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    # if agent.rect.colliderect(block1.rect):
    #     print("collision!")
    # left = True
    # right = False

    # if abs(agentX-bossX)>500:
    #     bossMove=True    
    # elif abs(agentX-bossX)<450:
    #     bossMove=False
    
    if agentX>enemyX:
          changeSpriteImage(enemy, 1) 
    elif agentX<enemyX:
          changeSpriteImage(enemy, 0)    

    if keyPressed("right"):
        move=True
        if(keys[pygame.K_SPACE]):
            if left:
               changeSpriteImage(agent,18)
               changeSpriteImage(agent,19) 
               if agent.rect.colliderect(enemy.rect):
                changeSpriteImage(enemy, 2)
                contactMob = True
               if agent.rect.colliderect(boss.rect):
                contactBoss = True
            elif right:
               changeSpriteImage(agent,20)
               changeSpriteImage(agent,21)   
               if agent.rect.colliderect(enemy.rect):
                changeSpriteImage(enemy, 2)
                contactMob = True
               if agent.rect.colliderect(boss.rect):
                 contactBoss = True 
            #SUPER IMPORTANT DONT DELETE
            # bullet_state = "fire"
            # if left:
            #     bulletX = agentX
            # elif right:
            #     bulletX = agentX-40
            # fire_bullet(bulletX, bulletY)
            # x -= 5

     
        agentImage += 1       
        if agentImage > 8:   
            agentImage = 0
        changeSpriteImage(agent, agentImage)
        
        agentX += 9          
        if agentX < 20:      
            agentX = 20
        if agentX > 1000:
            agentX = 1000
        moveSprite(agent, agentX, agentY)  
        left = True
        right = False
        if scroll==True:
            time.sleep(0.01)
            scrollBackground(-10, 0)
            block1X -= 10
            scrollCounter+=10
            moveSprite(block1, block1X, block1Y)
            buildX -=10
            moveSprite(build, buildX, buildY)
            bridgeX -=10
            moveSprite(bridge, bridgeX, bridgeY)
            moveSprite(boss, bossX, bossY)
    elif keyPressed("left"):
        move=True
        if(keys[pygame.K_SPACE]):
            if left:
                changeSpriteImage(agent,18)
                changeSpriteImage(agent,19)
                if agent.rect.colliderect(enemy.rect):
                    changeSpriteImage(enemy, 2)
                    contactMob = True
            elif right:
                changeSpriteImage(agent,20)
                changeSpriteImage(agent,21) 
                if agent.rect.colliderect(enemy.rect):
                    changeSpriteImage(enemy, 2)
                    contactMob = True
            #SUPER IMPORTANT DONT DELETE
            # bullet_state = "fire"
            # if left:
            #     bulletX = agentX
            # elif right:
            #     bulletX = agentX-40
            # fire_bullet(bulletX, bulletY)
            # x -= 5
        if agentImage < 9:
            agentImage = 9
        agentImage += 1        # Move the animation on by one frame
        if agentImage > 17:    # We have 8 frames, so loop round to the start
            agentImage = 9
            # changeSpriteImage(enemy, 0)
        changeSpriteImage(agent, agentImage)

        agentX -= 9          
        if agentX < 20:      
            agentX = 20
        if agentX > 1000:
            agentX = 1000
        moveSprite(agent, agentX, agentY) 
        left = False
        right = True
        if scroll==True and bossLife==1:
            time.sleep(0.01)
            scrollBackground(10, 0)
            block1X += 10
            scrollCounter-=10
            moveSprite(block1, block1X, block1Y)
            buildX +=10
            moveSprite(build, buildX, buildY)
            bridgeX +=10
            moveSprite(bridge,bridgeX,bridgeY)
    elif keys[pygame.K_SPACE]:
        move=True
        if left:
            changeSpriteImage(agent,18)
            changeSpriteImage(agent,19)
            if agent.rect.colliderect(enemy.rect):
                changeSpriteImage(enemy, 2)
                contactMob = True
            if agent.rect.colliderect(boss.rect):
                 contactBoss = True    
        elif right:
          changeSpriteImage(agent,20)
          changeSpriteImage(agent,21) 
          if agent.rect.colliderect(enemy.rect):
                changeSpriteImage(enemy, 2)
                contactMob = True
          if agent.rect.colliderect(boss.rect):
                 contactBoss = True      
        #SUPER IMPORTANT DONT DELETE
        # bullet_state = "fire"
        # if left:
        #     bulletX = agentX
        # elif right:
        #     bullet_state = "fire"
        #     bulletX = agentX-40
        # fire_bullet(bulletX, bulletY)
        # x -= 5
    else:
        if left:
            agentImage = 0  # If the key is not being pressed, switch back to "standing" frame
            changeSpriteImage(agent, agentImage)
        elif right:
            agentImage = 9  # If the key is not being pressed, switch back to "standing" frame
            changeSpriteImage(agent, agentImage)
    if not(isJump):
        if keys[pygame.K_UP]:
            isJump = True
            walkCount = 0
    else:
        if jumpCount >= -10:
            agentY -= (jumpCount * abs(jumpCount)) * 0.3
            agentY_change = agentY
            jumpCount -= 1
            moveSprite(agent, agentX, agentY)
        else:
            jumpCount = 10
            isJump = False  

    #BLOCK IF NOT JUMPING        
    if build.rect.left-agentX<55 and build.rect.left-agentX>0:
        if not isJump:
            agentX=build.rect.left-55
            agentY = 400
            bulletY = agentY
            scroll=False
        else:
            scroll=True   
    if agentX-build.rect.right<15 and agentX-build.rect.right>1:
        if not isJump:
            agentX=build.rect.right+20
            agentY = 400
            bulletY = agentY
            scroll=False
        else:
            scroll=True    
    if block1.rect.left-agentX<55 and block1.rect.left-agentX>0:
        if not isJump:
            agentX=block1.rect.left-55
            agentY = 400
            bulletY = agentY
            scroll=False
        else:
            scroll=True   
    if agentX-block1.rect.right<25 and agentX-block1.rect.right>1:
        if not isJump:
            agentX=block1.rect.right+20
            agentY = 400
            bulletY = agentY
            scroll=False
        else:
            scroll=True

    # if bridge.rect.left-agentX<55 and bridge.rect.left-agentX>0:
    #     if not isJump:
    #         agentX=bridge.rect.left-55
    #         agentY = 400
    #         bulletY = agentY
    #         scroll=False
    #     else:
    #         scroll=True   
    # if agentX-bridge.rect.right<25 and agentX-bridge.rect.right>1:
    #     print(agentX-bridge.rect.right)
    #     if not isJump:
    #         agentX=bridge.rect.right+20
    #         agentY = 400
    #         bulletY = agentY
    #         scroll=False
    #     else:
    #         scroll=True            
    #BLOCK IF NOT JUMPING END

    #JUMP ON ENVIRONMENT
    if agent.rect.colliderect(block1.rect) and isJump:
        if left and abs(agentX-block1X) > 5:
            agentX += 15
        elif right and abs(agentX-block1X) > 5:
            agentX -= 15
        agentY = block1.rect.top-52
        moveSprite(agent, agentX, agentY)
        bulletY = agentY 

    if agent.rect.colliderect(build.rect) and isJump:
        if left and abs(agentX-buildX) > 5:
            agentX += 5
        elif right and abs(agentX-buildX) > 5:
            agentX -= 5
        agentY = build.rect.top-52
        moveSprite(agent, agentX, agentY)
        bulletY = agentY
      
    if agent.rect.colliderect(bridge.rect) and isJump:
        if left and abs(agentX-bridgeX) > 5:
            agentX += 5
        elif right and abs(agentX-bridgeX) > 5:
            agentX -= 5
        agentY = bridge.rect.top-52
        moveSprite(agent, agentX, agentY)
        bulletY = agentY

        
    if not isJump and not agent.rect.colliderect(build.rect) and not agent.rect.colliderect(bridge.rect) and not agent.rect.colliderect(block1.rect):
        if not isJump:
            agentY = 400
            bulletY = agentY
            if agentY==400:
                scroll=True
        agentY = 400
        bulletY = agentY
        moveSprite(agent, agentX, agentY)
        
    move_towards_player(enemy, agent)

    

    if abs(scrollCounter)==700 and not contactBoss and bossLife==1:
        moveSprite(boss,bossX,bossY)
        showSprite(boss)
        time.sleep(1)
        scrollCounter=0
        bossLife=0   
    if contactMob:
        time.sleep(0.07)
        killSprite(enemy)
        moveSprite(enemy,random.randint(0, 1120),random.randint(50, 150))
        showSprite(enemy)    
    if contactBoss: 
        time.sleep(0.07)
        killSprite(boss)
        killSprite(bullet)
        bossLife= -1
        
    
    if not contactBoss:
        bullet.rect.x-=20
    if agent.rect.colliderect(bullet.rect):
        hitByBoss=True
    if hitByBoss:
        changeSpriteImage(agent,22)
        lifes-=1
        print(lifes)
    if lifes<=-12:
        game_over_text()      
    show_lifes(lifes)    

                     
   pygame.display.update()


game_run()
