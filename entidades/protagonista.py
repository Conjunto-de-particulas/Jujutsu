class Protagonista:
    def __init__(self, x, y, speed) -> None:
        self.x = x
        self.y = y
        self.cW = None
        self.rW = None
        self.deltaX = None
        self.deltaY = None
        self.speed = speed
        self.wait_to_move = False
        self.path_move = []
        self.count_FPS_to_move = 0
        self.get_path = True
          
    def draw_prota(self, screen, image, isoX, isoY, screen_width, rombo_height, rombo_width, deltaX, deltaY):
        screen.blit(image, (isoX + screen_width // 2 - deltaX, isoY + rombo_height*3 - deltaY))
        
    def set_delta_position(self, DEFAULT_IMAGE_SIZE):
        self.deltaX, self.deltaY = DEFAULT_IMAGE_SIZE[0]//2, DEFAULT_IMAGE_SIZE[1]*(65/100)
        
    def move(self):
        self.count_FPS_to_move += 1

        if self.count_FPS_to_move == 15 and len(self.path_move) >= 1:
            i = self.path_move.pop(0)
            self.x = i[0]
            self.y = i[1]
            self.count_FPS_to_move = 0
        elif len(self.path_move) == 0:
            self.wait_to_move = False
            self.get_path = True
                        
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
    
    def bfs(self, map, map_esta):
        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        queue = [[self.x, self.y]]
        visited = set()
        paths = {}
        
        visited.add(f'{self.x} {self.y}')
        paths[f'{self.x} {self.y}'] = []
        
        while len(queue) > 0:
            x, y = queue.pop(0)
            
            for i in direction:
                nx = x + i[0]
                ny = y + i[1]
                
                if (nx >= 0 and nx < len(map[0])) and (ny >= 0 and ny < len(map)) and (f'{nx} {ny}' not in visited) and(map_esta[map[ny][nx]]):
                    queue.append([nx, ny])
                    visited.add(f'{nx} {ny}')
                    paths[f'{nx} {ny}'] = [paths[f'{x} {y}'], [nx, ny]]
        
        return paths
    
    def set_path(self, path):
        if len(path) > 0:
            self.path_move.insert(0, path[-1])
        else:
            return
        self.set_path(path[0])
        
        
