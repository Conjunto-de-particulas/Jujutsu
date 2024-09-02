class Entity_Images:
    
    DEFAULT_IMAGE_SIZE = (36, 86)
    
    prota = None

    @classmethod
    def load_images(cls, pygame):
        cls.prota = pygame.image.load('images/prota/prota.png')
        cls.prota = pygame.transform.scale(cls.prota,cls.DEFAULT_IMAGE_SIZE)
