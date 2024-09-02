class Tile_Images:
    
    DEFAULT_IMAGE_SIZE = (80, 84)
    
    lista_tiles = []
    
    @classmethod
    def load_images(cls, pygame):
        cls.lista_tiles.append(pygame.image.load('images/tiles/tile_1.png'))
        cls.lista_tiles[-1] = pygame.transform.scale(cls.lista_tiles[-1],cls.DEFAULT_IMAGE_SIZE)
        
        cls.lista_tiles.append(pygame.image.load('images/tiles/tile_2.png'))
        cls.lista_tiles[-1] = pygame.transform.scale(cls.lista_tiles[-1],cls.DEFAULT_IMAGE_SIZE)
        
        cls.lista_tiles.append(pygame.image.load('images/tiles/tile_3.png'))
        cls.lista_tiles[-1] = pygame.transform.scale(cls.lista_tiles[-1],cls.DEFAULT_IMAGE_SIZE)
        
        cls.lista_tiles.append(pygame.image.load('images/tiles/tile_4.png'))
        cls.lista_tiles[-1] = pygame.transform.scale(cls.lista_tiles[-1],cls.DEFAULT_IMAGE_SIZE)
        
    @classmethod    
    def draw_tile(cls, screen, image, isoX, isoY, screen_width, rombo_height, rombo_width):
        screen.blit(image, (isoX + screen_width // 2 - rombo_width//2, isoY + rombo_height*3))
    
        