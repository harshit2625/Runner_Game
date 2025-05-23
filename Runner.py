import pygame  # as pg
#from sys import exit

def display_score():
    current_time = int(pygame.time.get_ticks()/1000) - start_time
    score_surf = test_font.render(f'Score{current_time}',False,(64,64,64))
    score_rect = score_surf.get_rect(center =(400,50))
    screen.blit(score_surf,score_rect)

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner Game')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf',50)
game_active = True
start_time = int(pygame.time.get_ticks()/1000)
#keys = pygame.K_SPACE

Sky_Surface = pygame.image.load('sky/sky.png').convert_alpha()#create a copy with a desgired pipxel format
ground_surface = pygame.image.load('ground/ground.png').convert_alpha()
# score_surf = test_font.render('MY GAME',False,(64,64,64))
# score_rect = score_surf.get_rect(center = (400,50))
snail_surf = pygame.image.load('snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomright =(600,300))#snail_rect = snail_surface.get_rect(toplift = ())
player_surface = pygame.image.load('jump/player_walk_1.png')
player_rect = player_surface.get_rect(midbottom   = (80,300))
player_gravity = 0
#test_surface = pygame.Surface((100,200))
#test_surface.fill('Red')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit() 
        #if event.type == pygame.MOUSEBUTTONUP:#MOUSEBUTTONDOWN:#MOUSEMOTION:
            #print('Mouse up')#'mouse down')#(event.pos)     
        #if event.type == pygame.MOUSEMOTION:
            #print(event.pos) 
        
    if game_active:        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos)and player_rect.bottom >=300:
                player_gravity =-20
                # print('collision')     
        if event.type == pygame.KEYDOWN:
            if player_rect.y > 200:
                if event.key == pygame.K_SPACE:
                    player_gravity =-22
                    #print('jump') 
    else:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: 
            game_active = True
            snail_rect.left = 800
            start_time = pygame.time.get_ticks()
        keys = pygame.key.get_pressed()
        


        


    if game_active:   
        screen.blit(Sky_Surface,(0,0))#blit use karne se ek display surfae k upper dusri aate hai        
        screen.blit(ground_surface,(0,300))
        # pygame.draw.rect(screen,'#c0e8ec',score_rect)
        # pygame.draw.rect(screen,'#c0e8ec',score_rect,10)
        #pygame.draw.line(screen,'Gold',(0,0),pygame.mouse.get_pos(),10)
        #pygame.draw.ellipse(screen,'Brown',pygame.Rect(50,200,100,100))
        # screen.blit(score_surf,score_rect)
        display_score()

        snail_rect.x -=5 #.x show kar raha hai ki humne x ki position me kuch change kie hai
        screen.blit(snail_surf,snail_rect)

    #player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300  
        screen.blit(player_surface,player_rect)

    #collision
        if snail_rect.colliderect(player_rect):
            game_active = False 

        if snail_rect.x<-100: #snai_x_pos = (800)
            snail_rect.x = 800 
 
        if player_rect.y <= 150:
            player_rect == 200


    else:
        if keys[pygame.K_SPACE]:
            game_active = True
            snail_rect.x = 800
   
        if player_rect.colliderect(snail_rect):
            snail_rect.x += 4
            print("collision")
            print(snail_rect.x)
            score_surf = test_font.render('Game Over',False,(64,64,64))
   

         
    pygame.display.update()
    clock.tick(60)
