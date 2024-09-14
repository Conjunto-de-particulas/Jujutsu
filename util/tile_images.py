from os import listdir

class Tile_Images:
    
    DEFAULT_IMAGE_SIZE = (80, 84)
    
    lista_tiles = []
    lista_estado = []
    
    @classmethod
    def load_images(cls, pygame):
                
        list = listdir('images/tiles')
        
        for i in list:
            cls.lista_tiles.append(pygame.image.load(f'images/tiles/{i}'))
            cls.lista_tiles[-1] = pygame.transform.scale(cls.lista_tiles[-1],cls.DEFAULT_IMAGE_SIZE)
            
        cls.lista_estado.append(True)
        cls.lista_estado.append(True)
        cls.lista_estado.append(True)
        cls.lista_estado.append(True)
        cls.lista_estado.append(True)
        cls.lista_estado.append(True)
        cls.lista_estado.append(True)
        cls.lista_estado.append(True)
        cls.lista_estado.append(False)

    @classmethod    
    def draw_tile(cls, screen, image, isoX, isoY, screen_width, rombo_height, rombo_width):
        screen.blit(image, (isoX + screen_width // 2 - rombo_width//2, isoY + rombo_height*3))
    
        