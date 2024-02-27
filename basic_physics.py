import pygame
import time

pygame.init()

WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode([WIDTH, HEIGHT])

fps = 60
timer = pygame.time.Clock()



#game vars    
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



def calc_motion_vector():
    x_speed, y_speed = 0, 0
    
    if len(mouse_trajectory) > 19:
        x_speed = (mouse_trajectory[-1][0] - mouse_trajectory[0][0])/len(mouse_trajectory)
        y_speed = (mouse_trajectory[-1][1] - mouse_trajectory[0][1])/len(mouse_trajectory)
    
    return x_speed, y_speed





class Ball:
    def __init__(self, position, radius, color, mass, retention, velocity, id, friction):
        self.position = position
        self.radius = radius
        self.color = color
        self.mass = mass
        self.retention = retention
        self.velocity = velocity
        self.id = id
        self.selected = False
        self.friction = friction
        
        self.circle = ''
                
    def draw(self):
        self.circle = pygame.draw.circle(screen, self.color, self.position, self.radius)
        
        
    
    def check_gravity(self):
        if not self.selected:
                
            if self.position[1] < (HEIGHT - self.radius - wall_thickness/2):
                self.velocity[1] += gravity
            
            else:
                if self.velocity[1] > bounce_stop:
                    self.velocity[1] = -self.velocity[1]*self.retention
                        
                else:
                    if abs(self.velocity[1]) <= bounce_stop:
                        self.velocity[1] = 0
            
            if (self.position[0] < self.radius + (wall_thickness/2) and self.velocity[0] < 0) or \
                (self.position[0] > WIDTH - self.radius - (wall_thickness/2) and self.velocity[0] > 0):
                self.velocity[0] *= -1 * self.retention
                    
                if abs(self.velocity[0]) < bounce_stop:
                        self.x_xpeed = 0
                        
            if self.velocity[1] == 0 and self.velocity[0] !=0 :
                if self.velocity[0] > 0:
                    self.velocity[0] -= self.friction
                    
            
        else:
            self.velocity = [x_push, y_push]
        return self.velocity[1]
    
    
    def update_position(self, mouse):
        if not self.selected:
        
            self.position[1] += self.velocity[1]
            self.position[0] += self.velocity[0]
        else:
            self.position[0] = mouse[0]
            self.position[1] = mouse[1]
    
    
    
    
    def check_select(self, pos):
        self.selected = False
        
        if self.circle.collidepoint(pos):
            self.selected = True
        return self.selected
        
                
                
                
                
                
                
                
                
                
                
                
                
                


ball1 = Ball([50, 50], 30, 'blue', 100, 0.5, [1, 1], 1, 0.02)
ball2 = Ball([200, 200], 30, 'blue', 100, 0.9, [1, 1], 1, 0.03)

balls = [ball1, ball2]
#main game loop
run = True



while run:
    timer.tick(fps)
    screen.fill('black')
    mouse_coords = pygame.mouse.get_pos()
    mouse_trajectory.append(mouse_coords)
    
    if len(mouse_trajectory) > 20:
        mouse_trajectory.pop(0)
    x_push, y_push = calc_motion_vector()
    
    ball1.draw()
    ball2.draw()
    ball1.update_position(mouse_coords)
    ball2.update_position(mouse_coords)
    ball1.velocity[1] = ball1.check_gravity()
    ball2.velocity[1] = ball2.check_gravity()

    
    walls = draw_walls()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button ==1:
                
                if ball1.check_select(event.pos) or ball2.check_select(event.pos):
                    active_select = True
                    
                    
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                active_select = False
                for i in range(len(balls)):
                    balls[i].check_select((-10000, -10000))
                
                
    pygame.display.flip()
    
pygame.quit()