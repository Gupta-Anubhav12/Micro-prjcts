import pygame
import time
import random
pygame.init()
gray = (119,118,110)
black = (255,255,255)
display_height = 600
display_width = 800

gamedisplays=pygame.display.set_mode((display_height,display_height))
pygame.display.set_caption('car game')

clock = pygame.time.Clock()
carimg = pygame.image.load('car1.png')
back_left = pygame.image.load("left.png")
back_right = pygame.image.load("right.png")
road = pygame.image.load("road.png")
car_width = 23

def obstacle(obs_startx,obs_starty,obs):
    if obs == 0:
        obs_pic=pygame.image.load('car1.png')
    elif obs==1:
        obs_pic=pygame.image.load('car2.png')
    elif obs==2:
        obs_pic=pygame.image.load('car3.png')
    gamedisplays.blit(obs_pic,(obs_startx,obs_starty))   
    
def text_objects(text,font):
    textsurface = font.render(text,True,black)
    return textsurface,textsurface.get_rect()
def message_display(text):
    largetext = pygame.font.Font('raavi.ttf',55)
    textsurface,textrect =text_objects(text,largetext)
    textrect.center=((display_width/3),(display_height/2))
    gamedisplays.blit(textsurface,textrect)
    pygame.display.update()
    time.sleep(3)
    game_loop()
    
def crash():
    message_display("ਦਾਰੂ ਨਾ ਪਿਆ ਕਰ")


def background():
    gamedisplays.blit(back_left,(50,0))
    gamedisplays.blit(back_right,(350,0))
    gamedisplays.blit(road,(180,120))
    gamedisplays.blit(road,(180,240))
    gamedisplays.blit(road,(180,0))
    gamedisplays.blit(road,(180,360))
    
def car(x,y):

    gamedisplays.blit(carimg,(x,y))

def game_loop():
    x=(display_width*0.36)
    y=(display_height*0.9)
    x_change=0
    obstacle_speed=9
    obs=0
    y_change=0
    obs_startx = random.randrange(185,280)
    obs_starty = -750
    obs_width = 23
    obs_height = 47
    
    bumped = False
    
    while not bumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bumped = True
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -2
            if event.key == pygame.K_RIGHT:
                x_change = 2
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_LEFT or  event.key==pygame.K_RIGHT:
                x_change=0   
            
        x+=x_change
        gamedisplays.fill(gray)
        background()
        obs_starty-=(obstacle_speed/4)
        obstacle(obs_startx,obs_starty,obs)
        obs_starty+=obstacle_speed
        car(x,y)
        if x< 185 or x>320:
            crash()
        if obs_starty >display_height:
            obs_starty =0-obs_height
            obs_startx=random.randrange(170,(display_width-170))
            obs=random.randrange(1,3)
            
        if y<obs_starty+obs_height:
            if x>obs_startx and x<obs_startx + obs_width or x+obs_width>obs_startx and x < obs_startx:
                crash()
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
