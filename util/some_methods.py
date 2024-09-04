class Some_Methods:
    
    @staticmethod
    def draw_grid(rect, screen, p, rombo_width, rombo_height,deltaX,deltaY ):
        rect(screen, (255, 255, 255), (p[0]*rombo_width + deltaX, p[1]*rombo_height + deltaY, rombo_width , rombo_height ), 1)