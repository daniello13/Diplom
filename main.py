import pygame
from pygame.locals import *
import urllib.request
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def Cube_creation(x,y,z,length, level):
    #x,y,z=-0.3 , 
    if level==1 :
        glColor3f(0.0,1.0,0.0)
    if level==2:
        glColor3f(1.0,1.0,0.0)
    if level==3:
        glColor3f(1.0,0.0,0.0)
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
    
mas=[1,2,3,2,2,2,1,1,1,3,3,3,1,1,1,2,3,1,2,3,1,2,2,2,2,3,1]
def Cube():
    edge_length=0.6
    distance_between_small_cubes=0.2

    glColor3f(   1.0,  0.0,  0.0 )
    
    Cube_creation(-1.1,-1.1,-1.1,edge_length, mas[0]) #A
    Cube_creation( -1.1, -0.3, -1.1 , edge_length,mas[1]) #B
    Cube_creation( -1.1, 0.5, -1.1 , edge_length,mas[2]) #C
    Cube_creation(-0.3,-1.1,-1.1, edge_length,mas[3]) #D
    Cube_creation(-0.3,-0.3,-1.1, edge_length,mas[4] )#E
    Cube_creation(-0.3, 0.5, -1.1, edge_length,mas[5])#F
    Cube_creation(0.5,-1.1, -1.1, edge_length,mas[6]) #G
    Cube_creation(0.5,-0.3,-1.1,edge_length,mas[7]) #H
    Cube_creation(0.5, 0.5, -1.1, edge_length,mas[8]) #I

    Cube_creation(-1.1,-1.1,-0.3,edge_length,mas[9]) #A
    Cube_creation( -1.1, -0.3, -0.3 , edge_length,mas[10]) #B
    Cube_creation( -1.1, 0.5, -0.3 , edge_length,mas[11]) #C
    Cube_creation(-0.3,-1.1,-0.3, edge_length,mas[12]) #D
    Cube_creation(-0.3,-0.3,-0.3, edge_length ,mas[13])#E
    Cube_creation(-0.3, 0.5, -0.3, edge_length,mas[14])#F
    Cube_creation(0.5,-1.1, -0.3, edge_length,mas[15]) #G
    Cube_creation(0.5,-0.3,-0.3,edge_length,mas[16]) #H
    Cube_creation(0.5, 0.5, -0.3, edge_length,mas[17]) #I

    Cube_creation(-1.1,-1.1,0.5,edge_length,mas[18]) #A
    Cube_creation( -1.1, -0.3, 0.5 , edge_length,mas[19]) #B
    Cube_creation( -1.1, 0.5, 0.5 , edge_length,mas[20]) #C
    Cube_creation(-0.3,-1.1,0.5, edge_length,mas[21]) #D
    Cube_creation(-0.3,-0.3,0.5, edge_length ,mas[22])#E
    Cube_creation(-0.3, 0.5, 0.5, edge_length,mas[23])#F
    Cube_creation(0.5,-1.1, 0.5, edge_length,mas[24]) #G
    Cube_creation(0.5,-0.3,0.5,edge_length,mas[25]) #H
    Cube_creation(0.5, 0.5, 0.5, edge_length,mas[26]) #I
    
    #`Cube_creation(-0.5, -0.5, -0.5, edge_length)
    #Cube_creation()
def get_data():
    global mas
    f = urllib.request.urlopen('http://diplom.moneto4ka.tk/send_data')
    s=(str)( f.read())
    counter = 0
    counter2=0
    for i in s:
        counter2+=1
        if i ==" ":
            mas[counter]=(int)(s[counter2-2])
            counter+=1
    #print(mas)


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
    glTranslatef(0.0,0.0, -6.0)
    
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
        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        get_data()
        Cube()
        
        pygame.display.flip()
        pygame.time.wait(1)


main()