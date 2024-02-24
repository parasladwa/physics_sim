import pygame

pygame.init()

WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode([WIDTH, HEIGHT])

fps = 60
timer = pygame.time.Clock()



#game vars
wall_thickness =10
gravity = 0.5
bounce_stop = 0.3


def draw_walls():
        left = pygame.draw.line(screen, 'white', (0, 0), (0, HEIGHT), wall_thickness)
        right = pygame.draw.line(screen, 'white', (WIDTH, 0), (WIDTH, HEIGHT), wall_thickness)
        top = pygame.draw.line(screen, 'white', (0, 0), (WIDTH, 0), wall_thickness)
        bottom = pygame.draw.line(screen, 'white', (0, HEIGHT), (WIDTH, HEIGHT), wall_thickness)
        wall_list = [left, right, top, bottom]
        return wall_list


class Ball:
        def __init__(self, position, radius, color, mass, retention, velocity, id):
                self.position = position
                self.radius = radius
                self.color = color
                self.mass = mass
                self.retention = retention
                self.velocity = velocity
                self.id = id
                
                self.circle = ''
                
        def draw(self):
                self.circle = pygame.draw.circle(screen, self.color, self.position, self.radius)
                
        
        
        def check_gravity(self):
                
                if self.position[1] < (HEIGHT - self.radius - wall_thickness/2):
                        self.velocity[1] += gravity
                
                else:
                        if self.velocity[1] > bounce_stop:
                                self.velocity[1] = -self.velocity[1]*self.retention


ball1 = Ball([50, 50], 30, 'blue', 100, 0.9, [1, 1], 1)
ball2 = Ball([200, 200], 30, 'blue', 100, 0.9, [1, 1], 1)


#main game loop
run = True

while run:
        timer.tick(fps)
        screen.fill('black')
        
        ball1.draw()
        ball2.draw()
        
        walls = draw_walls()
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False
                        
                        
        pygame.display.flip()
        
pygame.quit()