import pygame  

def display_score():
    current_time = int(pygame.time.get_ticks()/1000) - start_time
    score_surf = test_font.render(f'Score: {current_time}', False, (64,64,64))
    score_rect = score_surf.get_rect(center =(400,50))
    screen.blit(score_surf, score_rect)

# Initialization
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner Game')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = True
start_time = int(pygame.time.get_ticks() / 1000)

# Load assets
Sky_Surface = pygame.image.load('sky/sky.png').convert_alpha()
ground_surface = pygame.image.load('ground/ground.png').convert_alpha()

snail_surf = pygame.image.load('snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomright =(600,300))

player_surface = pygame.image.load('jump/player_walk_1.png')
player_rect = player_surface.get_rect(midbottom=(80,300))
player_gravity = 0

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit() 
        
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -22
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800
                start_time = int(pygame.time.get_ticks() / 1000)
                player_rect.bottom = 300
                player_gravity = 0
    # Game logic
    if game_active:   
        screen.blit(Sky_Surface, (0,0))      
        screen.blit(ground_surface, (0,300))
        
        display_score()

        snail_rect.x -= 5 
        screen.blit(snail_surf, snail_rect)

        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300  
        screen.blit(player_surface, player_rect)

        # Collision
        if snail_rect.colliderect(player_rect):
            game_active = False 

        if snail_rect.x < -100: 
            snail_rect.x = 800 
 
    else:
        screen.fill((94,129,162))  # Optional: Game over background
        score_surf = test_font.render('Game Over - Press SPACE', False, (64,64,64))
        score_rect = score_surf.get_rect(center=(400,200))
        screen.blit(score_surf, score_rect)

    pygame.display.update()
    clock.tick(60)

