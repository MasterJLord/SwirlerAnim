detail = int(input("""How many dots would you like? Pro tip: higher numbers, around 30 or above, generally look better. (press up and down to change patterns.)
"""))


import pygame, random, sys, math
from math import sin, cos
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((600, 600))
picture = pygame.Surface((500, 500), pygame.SRCALPHA)

circle = []
rad = 270
ite = 1
countdown = 0
upping = 0
downing = 0
visible = 0
toggle = 0

class path:
    def __init__(self):
        self.angle = 360/detail*len(circle)+360/detail
        self.neg = [-1, -1]
#        if self.angle > 90 and self.angle < 270:
#            self.neg[0] = 1
#        if self.angle > 180:
#            self.neg[1] = 1
#        self.angle -= 90*int(self.angle/90)
        self.end1 = [sin(self.angle)*rad]
        self.end1.append(cos(self.angle)*rad)
#        self.end1[0] *= self.neg[0]
#        self.end1[1] *= self.neg[1]
        self.end2 = [-1*self.end1[0], -1*self.end1[1]]
        self.road = -1*rad 
        self.vel = 1
        
    def blitable(self):
        pygame.draw.line(picture, (180, 180, 180), (300+int(self.end1[0]), 300+int(self.end1[1])), (300+int(self.end2[0]), 300+int(self.end2[1])), 1)
        pygame.draw.circle(picture, (255, 255, 255), (300+int(self.end1[0]), 300+int(self.end1[1])), 1)
        pygame.draw.circle(picture, (255, 255, 255), (300+int(self.end2[0]), 300+int(self.end2[1])), 1)

    def drawself(self):
        pygame.draw.circle(screen, (255, 255, 180), (300+int(self.road/rad*self.end2[0]), 300+int(self.road/rad*self.end2[1])), 4)
        
    def tick(self, reps):
        for i in range(reps):
            if self.road <= 0:
                self.vel += 1
            else:
                self.vel -= 1

            self.road += self.vel

def reset(ite):
    for i in range(detail):
        circle.append(path())
        for l in circle:
            l.tick(ite)

reset(ite)

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit() 
        
    screen.fill((0, 0, 0))
    clock.tick(30)
    if visible == 255:
        for i in circle:
            i.blitable()
        screen.blit(picture, (0, 0))

    
#    if visible > 0:
#        visible -= 2
#        if visible < 0:
#            visible = 0
#        for i in circle:
#            i.blitable()
#        screen.blit(picture, (0, 0))
        
    for i in circle:
        i.tick(1)
        i.drawself()
        
    pygame.display.update()
    
    key = pygame.key.get_pressed()
    if key[K_UP]:
        if not upping:
            circle = []
            ite += 1
            reset(ite)
            upping = 1
    else:
        upping = 0
    if key[K_DOWN]:
        if not downing:
            circle = []
            ite -= 1
            reset(ite)
            downing = 1
    else:
        downing = 0

    if key[K_1]:
        if not toggle:
            toggle = 1
            if visible == 255:
                visible = 0
            else:
                visible = 255
    else:
        toggle = 0
        
        
    
