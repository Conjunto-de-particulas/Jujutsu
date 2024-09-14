class Some_Methods:
    
    @staticmethod
    def draw_grid(rect, screen, p, rombo_width, rombo_height,deltaX,deltaY ):
        rect(screen, (255, 255, 255), (p[0]*rombo_width + deltaX, p[1]*rombo_height + deltaY, rombo_width , rombo_height ), 1)
        
    @staticmethod
    def cart_to_iso(x, y, size):
        isoX = (x - y) * size
        isoY = (x + y) * size // 2
        return isoX, isoY
    
    @staticmethod
    def draw_tile(surface, color, color2,isoX, isoY, randint, screen_width, rombo_width, rombo_height, polygon):
        isoX += randint(0, 0)
        isoY += randint(0, 0)
        polygon(surface, color, [(isoX + screen_width // 2, isoY + rombo_height*3), 
                                                            (isoX + screen_width // 2 + rombo_width//2, 
                                                            isoY + rombo_height*3 + rombo_height//2),
                                                            (isoX + screen_width // 2, isoY + rombo_height*3 + rombo_height),
                                                            (isoX + screen_width // 2 - rombo_width//2, 
                                                            isoY + rombo_height*3 + rombo_height//2)])
        polygon(surface, color2, [(isoX + screen_width // 2, isoY + rombo_height*3), 
                                                            (isoX + screen_width // 2 + rombo_width//2, 
                                                            isoY + rombo_height*3 + rombo_height//2),
                                                            (isoX + screen_width // 2, isoY + rombo_height*3 + rombo_height),
                                                            (isoX + screen_width // 2 - rombo_width//2, 
                                                            isoY + rombo_height*3 + rombo_height//2)],1)
        
        polygon(surface, color, [(isoX + screen_width // 2 + rombo_width//2, 
                                                            isoY + rombo_height*3 + rombo_height//2),
                                            (isoX + screen_width // 2 + rombo_width//2, 
                                                            isoY + rombo_height*3 + rombo_height//2 + 44),
                                            (isoX + screen_width // 2, isoY + rombo_height*3 + rombo_height + 44),
                                            (isoX + screen_width // 2, isoY + rombo_height*3 + rombo_height)])
        polygon(surface, color2, [(isoX + screen_width // 2 + rombo_width//2, 
                                                            isoY + rombo_height*3 + rombo_height//2),
                                            (isoX + screen_width // 2 + rombo_width//2, 
                                                            isoY + rombo_height*3 + rombo_height//2 + 44),
                                            (isoX + screen_width // 2, isoY + rombo_height*3 + rombo_height + 44),
                                            (isoX + screen_width // 2, isoY + rombo_height*3 + rombo_height)], 1)
        
        polygon(surface, color, [(isoX + screen_width // 2, isoY + rombo_height*3 + rombo_height),
                                            (isoX + screen_width // 2, isoY + rombo_height*3 + rombo_height + 44),
                                            (isoX + screen_width // 2 - rombo_width//2, 
                                                            isoY + rombo_height*3 + rombo_height//2 + 44),
                                            (isoX + screen_width // 2 - rombo_width//2, 
                                                            isoY + rombo_height*3 + rombo_height//2)])
        polygon(surface, color2, [(isoX + screen_width // 2, isoY + rombo_height*3 + rombo_height),
                                            (isoX + screen_width // 2, isoY + rombo_height*3 + rombo_height + 44),
                                            (isoX + screen_width // 2 - rombo_width//2, 
                                                            isoY + rombo_height*3 + rombo_height//2 + 44),
                                            (isoX + screen_width // 2 - rombo_width//2, 
                                                            isoY + rombo_height*3 + rombo_height//2)], 1)
    @staticmethod
    def generate_map(randint):
        map = []
        for i in range(10):
            r = []
            for j in range(10):
                r.append(randint(6,7))
            map.append(r)
        return map