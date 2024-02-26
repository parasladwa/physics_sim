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

    def forces(main_node, other):
        



node1 = Node(10, 10, 'white', [250, 250], [0, 0])
node2 = Node(10, 10, 'white', [200, 250], [0, 0])
nodes = [node1, node2]


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