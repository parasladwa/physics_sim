import pygame
import numpy as np
import time

pygame.init()

HEIGHT, WIDTH = 500, 500
screen = pygame.display.set_mode([WIDTH, HEIGHT])

fps = 60
timer = pygame.time.Clock()




wall_thickness =10
g = 50
spring_constant = 1






def draw_walls():
    left = pygame.draw.line(screen, 'white', (0, 0), (0, HEIGHT), wall_thickness)
    right = pygame.draw.line(screen, 'white', (WIDTH, 0), (WIDTH, HEIGHT), wall_thickness)
    top = pygame.draw.line(screen, 'white', (0, 0), (WIDTH, 0), wall_thickness)
    bottom = pygame.draw.line(screen, 'white', (0, HEIGHT), (WIDTH, HEIGHT), wall_thickness)
    wall_list = [left, right, top, bottom]
    return wall_list





class Node:
    def __init__(self, radius, mass, color, posn, vel, id, nn):
        self.radius = radius
        self.mass = mass
        self.color = color
        self.posn = posn
        self.vel = vel
        self.id = id
        self.nn = nn

    def draw_node(self):
        pygame.draw.circle(screen, self.color, self.posn, self.radius)
        
        
    def force(self, nodes):
        force = [0, 0]
        
        force[1] += self.mass * g
        
        return force
        # for id in self.nn:
        #     other = nodes[id]
        #     force += spring_constant * (other.posn - self.posn)
    
    def update_position(self, force, dt=1):
        self.posn = self.posn + self.vel * dt + force * (dt**2) / (2*self.mass)
        return self.posn

    def update_velocity(self, f1, f2, dt=1):
        self.vel = self.vel + (f1 + f2) * dt / (2*self.mass)
        return self.vel
    
    
        
             
            
            
    

        



def make_grid():
    
    nodes = []
    count =-1
    
    for i in range(200, 301, 50):
        for k in range(200, 301, 50):
            count+=1
            node = Node(10, 1, 'white', np.array([i, k]), np.array([0, 0]), count, [])
            nodes.append(node)

    for node in nodes:
        for other in nodes:
            dist = np.linalg.norm(node.posn - other.posn)
            if dist < 51 and (node.id != other.id):
                node.nn.append(other.id)
        
    return nodes

    
    
    
    
def reset(nodes):
    
    for node in nodes:
        node.color = 'white'
        
    return nodes
    
    
    
    
nodes = make_grid()

run = True    
forces = np.array([[0, 0]]*len(nodes))


while run:
    
    timer.tick(fps)
    screen.fill('black')
    mouse_coords = pygame.mouse.get_pos()

    

    
    walls = draw_walls()
    

    nodes = make_grid()
    
    def draw_all(nodes):
        for i, n in enumerate(nodes):
            n.draw_node()
    draw_all(nodes)
    


    """WORKS"""
    # for i, node in enumerate(nodes):
    #     node.color = 'blue'
    #     for i2, node2 in enumerate(nodes):
    #         if node2.id in node.nn:
    #             node2.color = 'green'
    #             draw_all(nodes)
    #     pygame.display.flip()
    #     time.sleep(1)
    #     reset(nodes)
    def new_forces(nodes):
        forces = [[0, 0]]*len(nodes)
        for i, node in enumerate(nodes):
            forces[node.id] = node.mass*g
        return forces
    
    forces = new_forces(nodes)
    
    
    for node in nodes:
        node.posn = node.update_position(forces[node.id])
        
    draw_all(nodes)
    pygame.display.flip()
    
    old = forces
    forces_new = new_forces(nodes)
    
    for node in nodes:
        node.vel = node.update_velocity(forces[node.id], old[node.id])

    print(nodes[0].posn)
    

    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    
                
    pygame.display.flip()
    
pygame.quit()