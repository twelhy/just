import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
running = True
zero = 0
speed = 5
FPS = 60
player_color = (255, 0, 0)
player_rect = pygame.Rect(325, 225, 50, 50)

map_width = 400
map_height = 300
map_color = (0, 102, 0)
map_rect = pygame.Rect(player_rect.x, player_rect.y, map_width, map_height)

obstacle_width = 300
obstacle_height = 20
obstacle_color = (0, 0, 255)

obstacle1_width = 20
obstacle1_height = 200

obstacle2_width = 230
obstacle2_height = 20
obstacle2_x = 0
obstacle2_y = 200 - obstacle2_height

obstacle3_width = 20
obstacle3_height = 200
obstacle3_x = 300 - obstacle3_width
obstacle3_y = 0



fill_color = (0, 0, 0)


pygame.display.flip()



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and map_rect.y < player_rect.y and player_rect.move(zero, -speed).colliderect(obstacle_rect) == False and player_rect.move(zero, -speed).colliderect(obstacle_rect1) == False and player_rect.move(zero, -speed).colliderect(obstacle_rect2) == False and player_rect.move(zero, -speed).colliderect(obstacle_rect3) == False:
        map_rect.y += speed
    if keys[pygame.K_s] and map_rect.y > -map_height + player_rect.height + player_rect.y and player_rect.move(zero, speed).colliderect(obstacle_rect) == False and player_rect.move(zero, speed).colliderect(obstacle_rect1) == False and player_rect.move(zero, speed).colliderect(obstacle_rect2) == False and player_rect.move(zero, speed).colliderect(obstacle_rect3) == False:
        map_rect.y -= speed
    if keys[pygame.K_a] and map_rect.x < player_rect.x and player_rect.move(-speed, zero).colliderect(obstacle_rect) == False and player_rect.move(-speed, zero).colliderect(obstacle_rect1) == False and player_rect.move(-speed, zero).colliderect(obstacle_rect2) == False and player_rect.move(-speed, zero).colliderect(obstacle_rect3) == False:
        map_rect.x += speed
    if keys[pygame.K_d] and map_rect.x > -map_width + player_rect.width + player_rect.x and player_rect.move(speed, zero).colliderect(obstacle_rect) == False and player_rect.move(speed, zero).colliderect(obstacle_rect1) == False and player_rect.move(speed, zero).colliderect(obstacle_rect2) == False and player_rect.move(speed, zero).colliderect(obstacle_rect3) == False:
        map_rect.x -= speed
    obstacle_rect = pygame.Rect(map_rect.x + player_rect.width, map_rect.y + player_rect.height, obstacle_width, obstacle_height)
    obstacle_rect1 = pygame.Rect(map_rect.x + player_rect.width, map_rect.y + player_rect.height, obstacle1_width, obstacle1_height)
    obstacle_rect2 = pygame.Rect(map_rect.x + player_rect.width + obstacle2_x, map_rect.y + player_rect.height + obstacle2_y, obstacle2_width, obstacle2_height)
    obstacle_rect3 = pygame.Rect(map_rect.x + player_rect.width + obstacle3_x, map_rect.y + player_rect.height + obstacle3_y, obstacle3_width, obstacle3_height)
    
    
    screen.fill(fill_color)
    pygame.draw.rect(screen, map_color, map_rect)
    pygame.draw.rect(screen, player_color, player_rect)
    pygame.draw.rect(screen, obstacle_color, obstacle_rect)
    pygame.draw.rect(screen, obstacle_color, obstacle_rect1)
    pygame.draw.rect(screen, obstacle_color, obstacle_rect2)
    pygame.draw.rect(screen, obstacle_color, obstacle_rect3)

    pygame.display.flip()
    clock.tick(FPS)
    
pygame.quit()