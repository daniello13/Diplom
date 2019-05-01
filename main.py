import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1),
    #начало решетки, номера - номера точек
    (0.33, -1, -1), #8
    (0.33, 1, -1), #9
    (-0.33, -1, -1), #10
    (-0.33, 1, -1), #11
    (-1, 0.33, -1), #12
    (1, 0.33, -1), #13
    (-1, -0.33, -1), #14
    (1, -0.33, -1), #15
    (0.33, -1, 1), #16
    (0.33, 1, 1), #17
    (-0.33, -1, 1), #18
    (-0.33, 1, 1), #19
    (-1, 0.33, 1), #20
    (1, 0.33, 1), #21
    (-1, -0.33, 1),#22
    (1, -0.33, 1), #23

    (1, -1, 0.33),#24
    (1, 1, 0.33), #25
    (1, -1, -0.33), #26
    (1,1,-0.33), #27

    (-1, -1, 0.33), #28
    (-1, 1, 0.33), #29
    (-1, -1, -0.33), #30
    (-1, 1, -0.33) #31
    
    )

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7),
    (8, 9),
    (10, 11),
    (12,13),
    (14,15),
    (16,17),
    (18,19),
    (20, 21),
    (22,23),
    (8,16),
    (9,17),
    (10,18),
    (11,19),
    (12,20),
    (13,21),
    (14, 22),
    (15, 23),
    
    (24, 25),
    (26,27),
    (28, 29),
    (30, 31),
    (24,28),
    (25,29),
    (26,30),
    (27,31)
    )


def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()


def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    #glMatrixMode(GL_MODELVIEW)
    #glLoadIdentity()
    gluPerspective(45, (display[0]/display[1]), 0.5, 50.0)
    #gluLookAt(10, 10, 10, 0, 0, 0, 0, 100, 0)
    glTranslatef(0.0,0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)


main()