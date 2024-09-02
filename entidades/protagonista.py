class Protagonista:
    def __init__(self, x, y, speed) -> None:
        self.x = x
        self.y = y
        self.speed = speed
        
    def draw(self, pygame, surface, color=(34, 200, 56)):
        pygame.draw.rect(surface, color, (self.x, self.y, 20, 20))
        
    def draw_prota(self, screen, image):
        screen.blit(image, (self.x, self.y))
        #screen.blit(image, (isoX + screen_width // 2 - rombo_width//2, isoY + rombo_height*3))
        
    def move(self, left, right, up, down):
        if left == True:
            self.x -= self.speed
            self.y -= self.speed//2
        if right == True:
            self.x += self.speed
            self.y += self.speed//2
        if up == True:
            self.x += self.speed
            self.y -= self.speed//2
        if down == True:
            self.x -= self.speed
            self.y += self.speed//2
            
    def calculate_coordinates(self, math, p, p2, mouseX, mouseY, deltaX, deltaY, rombo_width, rombo_height, map_origin):
        p[0] = math.floor(mouseX/rombo_width)
        p[1] = math.floor(mouseY/rombo_height)
        p2[0] = (p[1] - map_origin[1]) + (p[0] - map_origin[0])
        p2[1] = (p[1] - map_origin[1]) - (p[0] - map_origin[0])
        
        mouseX += deltaX
        mouseY += deltaY
        
        if self.is_point_in_triangle(p[0]*rombo_width + deltaX, p[1]*rombo_height + deltaY,
                                     p[0]*rombo_width + deltaX + rombo_width//2, p[1]*rombo_height + deltaY,
                                     p[0]*rombo_width + deltaX, p[1]*rombo_height + deltaY + rombo_height//2, mouseX, mouseY):
            p2[0] -= 1
        if self.is_point_in_triangle(p[0]*rombo_width + deltaX + rombo_width//2, p[1]*rombo_height + deltaY,
                                     p[0]*rombo_width + deltaX + rombo_width, p[1]*rombo_height + deltaY,
                                     p[0]*rombo_width + deltaX + rombo_width, p[1]*rombo_height + deltaY + rombo_height//2, mouseX, mouseY):
            p2[1] -= 1
        if self.is_point_in_triangle(p[0]*rombo_width + deltaX + rombo_width, p[1]*rombo_height + deltaY + rombo_height//2,
                                     p[0]*rombo_width + deltaX + rombo_width, p[1]*rombo_height + deltaY + rombo_height,
                                     p[0]*rombo_width + deltaX + rombo_width//2, p[1]*rombo_height + deltaY + rombo_height, mouseX, mouseY):
            p2[0] += 1
        if self.is_point_in_triangle(p[0]*rombo_width + deltaX + rombo_width//2, p[1]*rombo_height + deltaY + rombo_height,
                                     p[0]*rombo_width + deltaX, p[1]*rombo_height + deltaY + rombo_height,
                                     p[0]*rombo_width + deltaX, p[1]*rombo_height + deltaY + rombo_height//2, mouseX, mouseY):
            p2[1] += 1
            
    def areaTriangle(self, x1, y1, x2, y2, x3, y3):
        return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0
    
    def is_point_in_triangle(self, x1, y1, x2, y2, x3, y3, x, y):
        a =  self.areaTriangle(x1, y1, x2, y2, x3, y3)
  
        a1 = self.areaTriangle(x, y, x2, y2, x3, y3)
        a2 = self.areaTriangle(x1, y1, x, y, x3, y3)
        a3 = self.areaTriangle(x1, y1, x2, y2, x, y)

        return abs(a - (a1 + a2 + a3)) < 1e-8
