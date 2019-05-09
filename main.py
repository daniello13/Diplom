import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

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

def Cube_creation(x,y,z,length):
    #x,y,z=-0.3 , 
    glBegin(GL_POLYGON)
    glVertex3f( x, y, z)    # P1
    glVertex3f( x,  y+length, z)     # P2
    glVertex3f(  x+length,  y+length, z)      # P3
    glVertex3f(  x+length, y, z)       # P4
    glEnd()

    glBegin(GL_POLYGON)
    glVertex3f(  x+length, y, z+length )
    glVertex3f(  x+length,  y+length, z+length )
    glVertex3f( x,  y+length, z+length )
    glVertex3f( x, y, z+length )
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex3f( x+length, y, z )
    glVertex3f( x+length,  y+length, z )
    glVertex3f( x+length,  y+length,  z+length )
    glVertex3f( x+length, y,  z+length )
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex3f( x, y,  z+length )
    glVertex3f( x,  y+length,  z+length )
    glVertex3f( x,  y+length, z )
    glVertex3f( x, y, z )
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex3f(  x+length,  y+length,  z+length )
    glVertex3f(  x+length,  y+length, z )
    glVertex3f( x,  y+length, z )
    glVertex3f( x,  y+length,  z+length )
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex3f(  x+length, y, z )
    glVertex3f(  x+length, y,  z+length )
    glVertex3f( x, y,  z+length )
    glVertex3f( x, y, z )
    glEnd()
    
def Cube():
    '''
    glBegin(GL_POLYGON|GL_QUADS)
    for edge in edges:
        for vertex in edge:
            glColor3d(1,0,0)
            glVertex3fv(verticies[vertex])
    glEnd()
    '''
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

    #4 кубик
    glBegin(GL_POLYGON)
    glVertex3f( 0.5, -0.3, -0.3)    # P1
    glVertex3f( 0.5,  0.3, -0.3)     # P2
    glVertex3f(  1.1,  0.3, -0.3)      # P3
    glVertex3f(  1.1, -0.3, -0.3)       # P4
    glEnd()

    glBegin(GL_POLYGON)
    glVertex3f(  0.5, -0.3, 0.3 )
    glVertex3f(  0.5,  0.3, 0.3 )
    glVertex3f( 1.1,  0.3, 0.3 )
    glVertex3f( 1.1, -0.3, 0.3 )
    glEnd()

    glBegin(GL_POLYGON)
    glVertex3f( 0.5, 0.3, -0.3 )
    glVertex3f( 0.5,  -0.3, -0.3 )
    glVertex3f( 0.5,  -0.3,  0.3 )
    glVertex3f( 0.5, 0.3,  0.3 )
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex3f( 1.1, -0.3,  0.3 )
    glVertex3f( 1.1,  0.3,  0.3 )
    glVertex3f( 1.1,  0.3, -0.3 )
    glVertex3f( 1.1, -0.3, -0.3 )
    glEnd()
    
    
    #5 кубик
    glBegin(GL_POLYGON)
    glVertex3f( 0.5, -0.3, -0.5)    # P1
    glVertex3f( 0.5,  0.3, -0.5)     # P2
    glVertex3f(  1.1,  0.3, -0.5)      # P3
    glVertex3f(  1.1, -0.3, -0.5)       # P4
    glEnd()

    glBegin(GL_POLYGON)
    glVertex3f(  0.5, -0.3, -1.1 )
    glVertex3f(  0.5,  0.3, -1.1 )
    glVertex3f( 1.1,  0.3, -1.1 )
    glVertex3f( 1.1, -0.3, -1.1 )
    glEnd()

    glBegin(GL_POLYGON)
    glVertex3f( 0.5, 0.3, -0.5 )
    glVertex3f( 0.5,  -0.3, -0.5 )
    glVertex3f( 0.5,  -0.3,  -1.1 )
    glVertex3f( 0.5, 0.3,  -1.1 )
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex3f( 1.1, -0.3,  -1.1 )
    glVertex3f( 1.1,  0.3,  -1.1 )
    glVertex3f( 1.1,  0.3, -0.5 )
    glVertex3f( 1.1, -0.3, -0.5 )
    glEnd()
    # 6 кубик 
    glBegin(GL_POLYGON)
    glVertex3f( 0.5, -0.3, 0.5)    # P1
    glVertex3f( 0.5,  0.3, 0.5)     # P2
    glVertex3f(  1.1,  0.3, 0.5)      # P3
    glVertex3f(  1.1, -0.3, 0.5)       # P4
    glEnd()

    glBegin(GL_POLYGON)
    glVertex3f(  0.5, -0.3, 1.1 )
    glVertex3f(  0.5,  0.3, 1.1 )
    glVertex3f( 1.1,  0.3, 1.1 )
    glVertex3f( 1.1, -0.3, 1.1)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex3f( 0.5, 0.3, 0.5 )
    glVertex3f( 0.5,  -0.3, 0.5 )
    glVertex3f( 0.5,  -0.3,  1.1 )
    glVertex3f( 0.5, 0.3,  1.1 )
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex3f( 1.1, -0.3,  1.1 )
    glVertex3f( 1.1,  0.3,  1.1 )
    glVertex3f( 1.1,  0.3, 0.5 )
    glVertex3f( 1.1, -0.3, 0.5 )
    glEnd()
    # 7 кубик
    glBegin(GL_POLYGON)
    glVertex3f( -0.5, -0.3, -0.3)    # P1
    glVertex3f( -0.5,  0.3, -0.3)     # P2
    glVertex3f(  -1.1,  0.3, -0.3)      # P3
    glVertex3f(  -1.1, -0.3, -0.3)       # P4
    glEnd()

    glBegin(GL_POLYGON)
    glVertex3f(  -0.5, -0.3, 0.3 )
    glVertex3f(  -0.5,  0.3, 0.3 )
    glVertex3f( -1.1,  0.3, 0.3 )
    glVertex3f( -1.1, -0.3, 0.3 )
    glEnd()

    glBegin(GL_POLYGON)
    glVertex3f( -0.5, 0.3, -0.3 )
    glVertex3f( -0.5,  -0.3, -0.3 )
    glVertex3f( -0.5,  -0.3,  0.3 )
    glVertex3f( -0.5, 0.3,  0.3 )
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex3f( -1.1, -0.3,  0.3 )
    glVertex3f( -1.1,  0.3,  0.3 )
    glVertex3f( -1.1,  0.3, -0.3 )
    glVertex3f( -1.1, -0.3, -0.3 )
    glEnd()

    # 8 кубик
    glBegin(GL_POLYGON)
    glVertex3f( -0.5, -0.3, -0.5)    # P1
    glVertex3f( -0.5,  0.3, -0.5)     # P2
    glVertex3f(  -1.1,  0.3, -0.5)      # P3
    glVertex3f(  -1.1, -0.3, -0.5)       # P4
    glEnd()

    glBegin(GL_POLYGON)
    glVertex3f(  -0.5, -0.3, -1.1 )
    glVertex3f(  -0.5,  0.3, -1.1 )
    glVertex3f( -1.1,  0.3, -1.1 )
    glVertex3f( -1.1, -0.3, -1.1 )
    glEnd()

    glBegin(GL_POLYGON)
    glVertex3f( -0.5, 0.3, -0.5 )
    glVertex3f( -0.5,  -0.3, -0.5 )
    glVertex3f( -0.5,  -0.3,  -1.1 )
    glVertex3f( -0.5, 0.3,  -1.1 )
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex3f( -1.1, -0.3,  -1.1 )
    glVertex3f( -1.1,  0.3,  -1.1 )
    glVertex3f( -1.1,  0.3, -0.5 )
    glVertex3f( -1.1, -0.3, -0.5 )
    glEnd()
    # 9 кубик
    glBegin(GL_POLYGON)
    glVertex3f( -0.5, -0.3, 0.5)    # P1
    glVertex3f( -0.5,  0.3, 0.5)     # P2
    glVertex3f(  -1.1,  0.3, 0.5)      # P3
    glVertex3f(  -1.1, -0.3, 0.5)       # P4
    glEnd()

    glBegin(GL_POLYGON)
    glVertex3f(  -0.5, -0.3, 1.1 )
    glVertex3f(  -0.5,  0.3, 1.1 )
    glVertex3f( -1.1,  0.3, 1.1 )
    glVertex3f( -1.1, -0.3, 1.1 )
    glEnd()

    glBegin(GL_POLYGON)
    glVertex3f( -0.5, 0.3, 0.5 )
    glVertex3f( -0.5,  -0.3, 0.5 )
    glVertex3f( -0.5,  -0.3,  1.1 )
    glVertex3f( -0.5, 0.3,  1.1 )
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex3f( -1.1, -0.3,  1.1 )
    glVertex3f( -1.1,  0.3,  1.1 )
    glVertex3f( -1.1,  0.3, 0.5 )
    glVertex3f( -1.1, -0.3, 0.5 )
    glEnd()

    #10 КУБИК
    glBegin(GL_POLYGON)
    glVertex3f( -0.3, 0.5, -0.3)    # P1
    glVertex3f( 0.3,  0.5, -0.3)     # P2
    glVertex3f(  0.3,  1.1, -0.3)      # P3
    glVertex3f(  -0.3, 1.1, -0.3)       # P4
    glEnd()

    glBegin(GL_POLYGON)
    glVertex3f(  -0.3, 0.5, 0.3 )
    glVertex3f(  0.3,  0.5, 0.3 )
    glVertex3f( 0.3, 1.1, 0.3 )
    glVertex3f( -0.3, 1.1, 0.3 )
    glEnd()

    glBegin(GL_POLYGON)
    glVertex3f( -0.3, -0.5, -0.3 )
    glVertex3f( -0.3,  -1.1, -0.3 )
    glVertex3f( -0.3,  -1.1,  0.3 )
    glVertex3f( -0.3, -0.5,  0.3 )
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex3f( 0.3, -0.5,  -0.3 )
    glVertex3f( 0.3,  -1.1,  -0.3 )
    glVertex3f( 0.3,  -1.1, 0.3 )
    glVertex3f( 0.3, -0.5, 0.3 )
    glEnd()

    #11 cube
    glBegin(GL_POLYGON)
    glVertex3f( -0.3, 0.5, -0.5)    # P1
    glVertex3f( 0.3,  0.5, -0.5)     # P2
    glVertex3f(  0.3,  1.1, -0.5)      # P3
    glVertex3f(  -0.3, 1.1, -0.5)       # P4
    glEnd()

    glBegin(GL_POLYGON)
    glVertex3f(  -0.3, 0.5, -1.1 )
    glVertex3f(  0.3,  0.5, -1.1 )
    glVertex3f( 0.3, 1.1, -1.1 )
    glVertex3f( -0.3, 1.1, -1.1 )
    glEnd()

    glBegin(GL_POLYGON)
    glVertex3f( -0.3, -0.5, -0.5 )
    glVertex3f( -0.3,  -1.1, -0.5 )
    glVertex3f( -0.3,  -1.1,  -1.1 )
    glVertex3f( -0.3, -0.5,  -1.1 )
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex3f( 0.3, -0.5,  -0.5 )
    glVertex3f( 0.3,  -1.1,  -0.5 )
    glVertex3f( 0.3,  -1.1, -1.1 )
    glVertex3f( 0.3, -0.5, -1.1 )
    glEnd()
    #12 cube
    glBegin(GL_POLYGON)
    glVertex3f( -0.3, 0.5, 0.5)    # P1
    glVertex3f( 0.3,  0.5, 0.5)     # P2
    glVertex3f(  0.3,  1.1, 0.5)      # P3
    glVertex3f(  -0.3, 1.1, 0.5)       # P4
    glEnd()

    glBegin(GL_POLYGON)
    glVertex3f(  -0.3, 0.5, 1.1 )
    glVertex3f(  0.3,  0.5, 1.1 )
    glVertex3f( 0.3, 1.1, 1.1 )
    glVertex3f( -0.3, 1.1, 1.1 )
    glEnd()

    glBegin(GL_POLYGON)
    glVertex3f( -0.3, -0.5, 0.5 )
    glVertex3f( -0.3,  -1.1, 0.5 )
    glVertex3f( -0.3,  -1.1,  1.1 )
    glVertex3f( -0.3, -0.5,  1.1 )
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex3f( 0.3, -0.5,  0.5 )
    glVertex3f( 0.3,  -1.1, 0.5 )
    glVertex3f( 0.3,  -1.1, 1.1 )
    glVertex3f( 0.3, -0.5, 1.1 )
    glEnd()
    #13 cube -0.3
    glBegin(GL_POLYGON)
    glVertex3f( -0.3, -0.5, -0.3)    # P1
    glVertex3f( 0.3,  -0.5, -0.3)     # P2
    glVertex3f(  0.3,  -1.1, -0.3)      # P3
    glVertex3f(  -0.3, -1.1, -0.3)       # P4
    glEnd()

    glBegin(GL_POLYGON)
    glVertex3f(  -0.3, -0.5, 0.3 )
    glVertex3f(  0.3,  -0.5, 0.3 )
    glVertex3f( 0.3, -1.1, 0.3 )
    glVertex3f( -0.3, -1.1, 0.3 )
    glEnd()

    glBegin(GL_POLYGON)
    glVertex3f( -0.3, 0.5,  -0.3 )
    glVertex3f( -0.3,  1.1,  -0.3 )
    glVertex3f( -0.3,  1.1, 0.3 )
    glVertex3f( -0.3, 0.5, 0.3 )
    glEnd()

    glBegin(GL_POLYGON)
    glVertex3f( 0.3, 0.5,  -0.3 )
    glVertex3f( 0.3,  1.1,  -0.3 )
    glVertex3f( 0.3,  1.1, 0.3 )
    glVertex3f( 0.3, 0.5, 0.3 )
    glEnd()
    #14 cube
    glBegin(GL_POLYGON)
    glVertex3f( -0.3, -0.5, -0.5)    # P1
    glVertex3f( 0.3,  -0.5, -0.5)     # P2
    glVertex3f(  0.3,  -1.1, -0.5)      # P3
    glVertex3f(  -0.3, -1.1, -0.5)       # P4
    glEnd()

    glBegin(GL_POLYGON)
    glVertex3f(  -0.3, -0.5, -1.1 )
    glVertex3f(  0.3,  -0.5, -1.1 )
    glVertex3f( 0.3, -1.1, -1.1 )
    glVertex3f( -0.3, -1.1, -1.1 )
    glEnd()

    glBegin(GL_POLYGON)
    glVertex3f( -0.3, 0.5,  -0.5 )
    glVertex3f( -0.3,  1.1,  -0.5 )
    glVertex3f( -0.3,  1.1, -1.1 )
    glVertex3f( -0.3, 0.5, -1.1 )
    glEnd()

    glBegin(GL_POLYGON)
    glVertex3f( 0.3, 0.5,  -0.5 )
    glVertex3f( 0.3,  1.1,  -0.5 )
    glVertex3f( 0.3,  1.1, -1.1 )
    glVertex3f( 0.3, 0.5, -1.1 )
    glEnd()
    #15 cube
    glBegin(GL_POLYGON)
    glVertex3f( -0.3, -0.5, 0.5)    # P1
    glVertex3f( 0.3,  -0.5, 0.5)     # P2
    glVertex3f(  0.3,  -1.1,0.5)      # P3
    glVertex3f(  -0.3, -1.1,0.5)       # P4
    glEnd()

    glBegin(GL_POLYGON)
    glVertex3f(  -0.3, -0.5, 1.1 )
    glVertex3f(  0.3,  -0.5, 1.1 )
    glVertex3f( 0.3, -1.1, 1.1 )
    glVertex3f( -0.3, -1.1, 1.1 )
    glEnd()

    glBegin(GL_POLYGON)
    glVertex3f( -0.3, 0.5,  0.5 )
    glVertex3f( -0.3,  1.1,  0.5 )
    glVertex3f( -0.3,  1.1, 1.1 )
    glVertex3f( -0.3, 0.5, 1.1 )
    glEnd()

    glBegin(GL_POLYGON)
    glVertex3f( 0.3, 0.5,  0.5 )
    glVertex3f( 0.3,  1.1,  0.5 )
    glVertex3f( 0.3,  1.1, 1.1 )
    glVertex3f( 0.3, 0.5, 1.1 )
    glEnd()
    '''
    edge_length=0.6
    distance_between_small_cubes=0.2
    z = -1.1
    glColor3f(   1.0,  0.0,  0.0 )
    coord = [-1.1,z+edge_length+distance_between_small_cubes,0.5]
    for z in coord:
        Cube_creation(-0.3,-0.3,z,edge_length) #A
        Cube_creation( 0.5, -0.3, z , edge_length) #B
        Cube_creation( -0.3, 0.5, z , edge_length) #C
        Cube_creation(0.5,0.5,z, edge_length) #D
        Cube_creation(-0.3,-1.1,z, edge_length )#E
        Cube_creation(0.5, -1.1, z, edge_length)#F
        Cube_creation(-1.1,0.5, z, edge_length) #G
        Cube_creation(-1.1,-0.3,z,edge_length) #H
        Cube_creation(-1.1, -1.1, z, edge_length) #I
    
    #`Cube_creation(-0.5, -0.5, -0.5, edge_length)
    #Cube_creation()


def keyboard (Key, x, y):
    if(Key==GLUT_KEY_RIGHT):
        glRotatef(2, 0, 0, 1)
    

def main():
    motion = "stop"
    pygame.init()
    display = (800,600)
    
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    #glutSpecialFunc(keyboard)
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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    motion = "right"
                if event.key == pygame.K_UP:
                    motion = "up"
            elif event.type == pygame.KEYUP:
                if event.key in [pygame.K_UP, pygame.K_RIGHT]:
                    motion = "stop"
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
        if motion == "right":
            glRotatef(1, 0, 0, 1)
        if motion == "up":
            glRotatef(1,1,0,0)
        #glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        Cube()
        
        pygame.display.flip()
        pygame.time.wait(10)


main()