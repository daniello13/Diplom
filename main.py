import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

verticies = (
    (0.3, -0.3, -0.3),
    (0.3, 0.3, -0.3),
    (-0.3, 0.3, -0.3),
    (-0.3, -0.3, -0.3),
    (0.3, -0.3, 0.3),
    (0.3, 0.3, 0.3),
    (-0.3, -0.3, 0.3),
    (-0.3, 0.3, 0.3),
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
    (5,7)
    )


def Cube():
    '''
    glBegin(GL_POLYGON|GL_QUADS)
    for edge in edges:
        for vertex in edge:
            glColor3d(1,0,0)
            glVertex3fv(verticies[vertex])
    glEnd()
    '''
    # кубик №1
    glBegin(GL_POLYGON)
    glVertex3f( -0.3, -0.3, -0.3)    # P1
    glVertex3f( -0.3,  0.3, -0.3)     # P2
    glVertex3f(  0.3,  0.3, -0.3)      # P3
    glVertex3f(  0.3, -0.3, -0.3)       # P4
    glEnd()

    glBegin(GL_POLYGON)
    glVertex3f(  0.3, -0.3, 0.3 )
    glVertex3f(  0.3,  0.3, 0.3 )
    glVertex3f( -0.3,  0.3, 0.3 )
    glVertex3f( -0.3, -0.3, 0.3 )
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex3f( 0.3, -0.3, -0.3 )
    glVertex3f( 0.3,  0.3, -0.3 )
    glVertex3f( 0.3,  0.3,  0.3 )
    glVertex3f( 0.3, -0.3,  0.3 )
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex3f( -0.3, -0.3,  0.3 )
    glVertex3f( -0.3,  0.3,  0.3 )
    glVertex3f( -0.3,  0.3, -0.3 )
    glVertex3f( -0.3, -0.3, -0.3 )
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex3f(  0.3,  0.3,  0.3 )
    glVertex3f(  0.3,  0.3, -0.3 )
    glVertex3f( -0.3,  0.3, -0.3 )
    glVertex3f( -0.3,  0.3,  0.3 )
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex3f(  0.3, -0.3, -0.3 )
    glVertex3f(  0.3, -0.3,  0.3 )
    glVertex3f( -0.3, -0.3,  0.3 )
    glVertex3f( -0.3, -0.3, -0.3 )
    glEnd()
    
    #2 кубик
    #
    #glVertex3f( 0.3, -0.3, -0.3 )
    #glVertex3f( 0.3,  0.3, -0.3 )
    #glVertex3f( 0.3,  0.3,  0.3 )
    #glVertex3f( 0.3, -0.3,  0.3 )
    glBegin(GL_POLYGON)
    glColor3f(   1.0,  0.0,  0.0 )
    glVertex3f( -0.3, -0.3, -0.5)    # P1
    glVertex3f( -0.3,  0.3, -0.5)     # P2
    glVertex3f(  0.3,  0.3, -0.5)      # P3
    glVertex3f(  0.3, -0.3, -0.5)       # P4
    glEnd()

    glBegin(GL_POLYGON)
    glVertex3f( -0.3, -0.3, -1.1)    # P1
    glVertex3f( -0.3,  0.3, -1.1)     # P2
    glVertex3f(  0.3,  0.3, -1.1)      # P3
    glVertex3f(  0.3, -0.3, -1.1)       # P4
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex3f( 0.3, -0.3, -0.5)    # P
    glVertex3f(  0.3,  0.3, -0.5)      # P3
    glVertex3f( 0.3,  0.3, -1.1) 
    glVertex3f(  0.3, -0.3, -1.1)       # P4
    glEnd()
    #
    glBegin(GL_POLYGON)
    glVertex3f( -0.3, -0.3, -0.5)    # P
    glVertex3f(  -0.3,  0.3, -0.5)      # P3
    glVertex3f( -0.3,  0.3, -1.1) 
    glVertex3f(  -0.3, -0.3, -1.1)       # P4
    glEnd()
    #
    glBegin(GL_POLYGON)
    glVertex3f( -0.3, 0.3, -0.5)    # P
    glVertex3f(  0.3,  0.3, -0.5)      # P3
    glVertex3f( 0.3,  0.3, -1.1) 
    glVertex3f( -0.3, 0.3, -1.1)       # P4
    glEnd()
    #
    glBegin(GL_POLYGON)
    glVertex3f( -0.3, -0.3, -0.5)    # P
    glVertex3f(  0.3,  -0.3, -0.5)      # P3
    glVertex3f( 0.3,  -0.3, -1.1) 
    glVertex3f( -0.3, -0.3, -1.1)       # P4
    glEnd()
    # 3 кубик
    glBegin(GL_POLYGON)
    glColor3f(   1.0,  0.0,  0.0 )
    glVertex3f( -0.3, -0.3, 0.5)    # P1
    glVertex3f( -0.3,  0.3, 0.5)     # P2
    glVertex3f(  0.3,  0.3, 0.5)      # P3
    glVertex3f(  0.3, -0.3, 0.5)       # P4
    glEnd()

    glBegin(GL_POLYGON)
    glVertex3f( -0.3, -0.3, 1.1)    # P1
    glVertex3f( -0.3,  0.3, 1.1)     # P2
    glVertex3f(  0.3,  0.3, 1.1)      # P3
    glVertex3f(  0.3, -0.3, 1.1)       # P4
    glEnd()

    #
    glBegin(GL_POLYGON)
    glVertex3f( 0.3, -0.3, 0.5)    # P
    glVertex3f(  0.3,  0.3, 0.5)      # P3
    glVertex3f( 0.3,  0.3, 1.1) 
    glVertex3f(  0.3, -0.3, 1.1)       # P4
    glEnd()
    #
    glBegin(GL_POLYGON)
    glVertex3f( -0.3, -0.3, 0.5)    # P
    glVertex3f(  -0.3,  0.3, 0.5)      # P3
    glVertex3f( -0.3,  0.3, 1.1) 
    glVertex3f(  -0.3, -0.3, 1.1)       # P4
    glEnd()
    #
    glBegin(GL_POLYGON)
    glVertex3f( -0.3, 0.3, 0.5)    # P
    glVertex3f(  0.3,  0.3, 0.5)      # P3
    glVertex3f( 0.3,  0.3, 1.1) 
    glVertex3f( -0.3, 0.3, 1.1)       # P4
    glEnd()
    #
    glBegin(GL_POLYGON)
    glVertex3f( -0.3, -0.3, 0.5)    # P
    glVertex3f(  0.3,  -0.3, 0.5)      # P3
    glVertex3f( 0.3,  -0.3, 1.1) 
    glVertex3f( -0.3, -0.3, 1.1)       # P4
    glEnd()

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    #glMatrixMode(GL_MODELVIEW)
    #glLoadIdentity()
    gluPerspective(45, (display[0]/display[1]), 0.3, 50.0)
    #gluLookAt(10, 10, 10, 0, 0, 0, 0, 100, 0)
    glTranslatef(0.0,0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glEnable(GL_DEPTH_TEST)
    # Принимать фрагменты которые ближе к камере

        #light0_diffuse=(0.4, 0.7, 0.2)
        #light0_direction = (4.0, 4.0, 4.0, 0.0)
        glDepthFunc(GL_LESS)
        
        #glEnable(GL_LIGHTING)
        #glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient)
        #glEnable(GL_LIGHT0)
        #GL_POSITION=(3, 0,3,1)
        #glLightfv(GL_LIGHT0, GL_DIFFUSE, light0_diffuse) 
        #glLightfv(GL_LIGHT0, GL_POSITION, light0_direction)
        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)


main()