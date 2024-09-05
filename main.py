import pygame
import sys
import math
import random
from entidades.protagonista import Protagonista
from util.tile_images import Tile_Images
from util.entity_images import Entity_Images
from util.some_methods import Some_Methods

rombo_height = 40
rombo_width = 80
             
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_width, screen_height = screen.get_size()

screen_color = (0, 0, 0)
clock = pygame.time.Clock()
showGrid = False
show_coor = False
deltaX = screen_width//2 - rombo_width//2
deltaY = rombo_height*3
map_origin = [0, 0]
p = [0, 0]
p2 = [0, 0]
right, left, up, down = False, False, False, False

map = Some_Methods.generate_map(random.randint)
prota = Protagonista(700,500, 4)
Tile_Images.load_images(pygame)
Entity_Images.load_images(pygame)
fuente = pygame.font.SysFont(None, 40)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                left = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                right = True
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                down = True
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                up = True
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                left = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                right = False
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                down = False
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                up = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g:
                showGrid = not showGrid 
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:
                show_coor = not show_coor 
            
    prota.move(left, right, up, down)
                    
    screen.fill(screen_color)
                
    for y in range(len(map)):
        for x in range(len(map[y])):
            isoX, isoY = Some_Methods.cart_to_iso(x, y, rombo_height)
            #draw_tile(screen, (20, 10, 200), (255, 255, 255),isoX, isoY)
            #draw_tile(screen, (36, 100, 200), (255, 255, 255),isoX, isoY)  
            Tile_Images.draw_tile(screen, Tile_Images.lista_tiles[map[y][x]], isoX, isoY, screen_width, rombo_height, rombo_width)
    
    prota.draw_prota(screen, Entity_Images.prota)
            
    mouseX, mouseY = pygame.mouse.get_pos()
    
    if show_coor:
        superficie_texto = fuente.render(f'X: {mouseX}, Y: {mouseY}', True, (255,255,255))
        screen.blit(superficie_texto, (50,50))
    
    mouseX -= deltaX
    mouseY -= deltaY
        
    prota.calculate_coordinates(math, p, p2, mouseX, mouseY, deltaX, deltaY, rombo_width, rombo_height, map_origin)
    
    if show_coor:
        superficie_texto = fuente.render(f'C: {p[0]}, R: {p[1]}', True, (255,255,255))
        screen.blit(superficie_texto, (50,100))
        
        superficie_texto = fuente.render(f'Cw: {p2[0]}, Rw: {p2[1]}', True, (255,255,255))
        screen.blit(superficie_texto, (50,150))

    if showGrid == True:
        Some_Methods.draw_grid(pygame.draw.rect, screen, p, rombo_width, rombo_height, deltaX, deltaY)
          
    pygame.display.flip() 

    clock.tick(60) 
    
pygame.quit()  
sys.exit()          