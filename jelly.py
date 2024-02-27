import pygame



pygame.init()

HEIGHT, WIDTH = 500, 500
screen = pygame.display.set_mode([WIDTH, HEIGHT])

fps = 60
timer = pygame.time.Clock()




wall_thickness =10
gravity = 0.5
bounce_stop = 1

#track position of mouse to get movement vector
mouse_trajectory = []





def draw_walls():
    left = pygame.draw.line(screen, 'white', (0, 0), (0, HEIGHT), wall_thickness)
    right = pygame.draw.line(screen, 'white', (WIDTH, 0), (WIDTH, HEIGHT), wall_thickness)
    top = pygame.draw.line(screen, 'white', (0, 0), (WIDTH, 0), wall_thickness)
    bottom = pygame.draw.line(screen, 'white', (0, HEIGHT), (WIDTH, HEIGHT), wall_thickness)
    wall_list = [left, right, top, bottom]
    return wall_list





class Node:
    def __init__(self, radius, mass, color, posn, vel):
        
        self.radius = radius
        self.mass = mass
        self.color = color
        self.posn = posn
        self.vel = vel
    
     
    def draw_node(self):
        pygame.draw.circle(screen, self.color, self.posn, self.radius)
        
        
    def position_update(self, force, dt):
        self.posn = self.posn + self.vel + force * (dt**2) / (2 * self.mass)
        return self.posn
    
    def velocity_update(self, f1, f2, dt):
        self.vel = self.vel + (f1 + f2) * dt / (2*self.mass)
    
    def forces(self, other):
        f = [ 0, self.mass * gravity ]
        return f 
    
    def acceleration(self, force):
        acc = force / self.mass
        return acc
    

        



def make_grid():
    nodes = []
    for i in range(200, 301, 50):
        for k in range(200, 301, 50):
            node = Node(10, 1, 'white', [i, k], [0, 0])
            nodes.append(node)
    return nodes
    
    
nodes = make_grid()


run = True
while run:
    timer.tick(fps)
    screen.fill('black')
    mouse_coords = pygame.mouse.get_pos()
    mouse_trajectory.append(mouse_coords)
    

    
    walls = draw_walls()
    
    
    
    
    
    
    
    for node in nodes:
        node.draw_node()
        
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    
                
    pygame.display.flip()
    
pygame.quit()