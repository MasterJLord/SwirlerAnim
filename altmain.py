import pygame, random, sys, math
from math import sin, cos

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((600, 600))

circle = []
detail = 16

class path:
    def __init__(self):
        self.angle = 360/detail*len(circle)+360/detail
        self.neg = [-1, -1]
#        if self.angle > 90 and self.angle < 270:
#            self.neg[0] = 1
#        if self.angle > 180:
#            self.neg[1] = 1
#        self.angle -= 90*int(self.angle/90)
        self.end1 = [sin(self.angle)*150]
        self.end1.append(cos(self.angle)*150)
#        self.end1[0] *= self.neg[0]
#        self.end1[1] *= self.neg[1]
        self.end2 = [-1*self.end1[0], -1*self.end1[1]]
        self.road = -150 
        self.vel = 1
        
    def drawself(self):
        pygame.draw.line(screen, (180, 180, 180), (300+int(self.end1[0]), 300+int(self.end1[1])), (300+int(self.end2[0]), 300+int(self.end2[1])), 2)
        pygame.draw.circle(screen, (255, 255, 255), (300+int(self.end1[0]), 300+int(self.end1[1])), 2)
        pygame.draw.circle(screen, (255, 255, 255), (300+int(self.end2[0]), 300+int(self.end2[1])), 2)
        pygame.draw.circle(screen, (255, 255, 180), (300+int(self.road/150*self.end2[0]), 300+int(self.road/150*self.end2[1])), 3)
        
        if self.road <= 0:
            self.vel += 1
        else:
            self.vel -= 1
        
        self.road += self.vel


for i in range(detail):
    circle.append(path())

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit() 
        
    screen.fill((0, 0, 0))
    clock.tick(40)

    for i in circle:
        i.drawself()
        
    pygame.display.update()
        
