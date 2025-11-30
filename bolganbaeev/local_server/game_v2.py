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

map_width = 800
map_height = 600
map_color = (0, 102, 0)
map_rect = pygame.Rect(player_rect.x, player_rect.y, map_width, map_height)

obstacle_color = (0, 0, 255)
fill_color = (0, 0, 0)


obstacle = [[300, 20, 0, 0],
            [20, 200, 0, 0],
            [210, 20, 0, 180],
            [20, 200, 280, 0],
            [20, 110, 140, 90],
            [350, 20, -50, 400]]

pygame.display.flip()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    def can_move(dx, dy):
        new_rect = player_rect.move(dx,dy)
        return not any(new_rect.colliderect(obstacle_func(rect)) for rect in range(len(obstacle)))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and map_rect.y < player_rect.y and can_move(0, -speed):
        map_rect.y += speed
    if keys[pygame.K_s] and map_rect.y > -map_height + player_rect.height + player_rect.y and can_move(0, speed):
        map_rect.y -= speed
    if keys[pygame.K_a] and map_rect.x < player_rect.x and can_move(-speed, 0):
        map_rect.x += speed
    if keys[pygame.K_d] and map_rect.x > -map_width + player_rect.width + player_rect.x and can_move(speed, 0):
        map_rect.x -= speed
    
    def obstacle_func(qatar):
        return pygame.Rect(map_rect.x + player_rect.width + obstacle[qatar][2], map_rect.y + player_rect.height + obstacle[qatar][3], obstacle[qatar][0], obstacle[qatar][1])
    
    screen.fill(fill_color)
    pygame.draw.rect(screen, map_color, map_rect)
    pygame.draw.rect(screen, player_color, player_rect)
    for rect in range(len(obstacle)):
        pygame.draw.rect(screen, obstacle_color, obstacle_func(rect))

    pygame.display.flip()
    clock.tick(FPS)
    
pygame.quit()