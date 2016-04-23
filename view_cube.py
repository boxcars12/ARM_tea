import pygame
from pygame.locals import *

import math

from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
    )

surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6),
)

colors = (
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (0, 1, 0),
    (1, 1, 1),
    (0, 1, 1),
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 0, 0),
    (1, 1, 1),
    (0, 1, 1),
)

axis_points = (
    (0,0,0),
    (1,0,0),
    (0,1,0),
    (0,0,1),
)

axis_lines = (
    (0,1),
    (0,2),
    (0,3),
)

axis_colors = (
    (1,0,0),
    (0,1,0),
    (0,0,1),
)

def mul_v3_fl(v0, f):
    return (
        v0[0] * f,
        v0[1] * f,
        v0[2] * f,
        )

def euc_distance(iniCoor, endCoor):
    return math.sqrt(math.pow(math.fabs(iniCoor[0] - endCoor[0]), 2) + math.pow(math.fabs(iniCoor[1] - endCoor[1]), 2) + math.pow(math.fabs(iniCoor[2] - endCoor[2]), 2))

def cross(a, b):
    c = [a[1]*b[2] - a[2]*b[1],
         a[2]*b[0] - a[0]*b[2],
         a[0]*b[1] - a[1]*b[0]]

    return c

def dot_v3v3(v0, v1):
    return (
        (v0[0] * v1[0]) +
        (v0[1] * v1[1]) +
        (v0[2] * v1[2])
        )

def sub_v2v2(v0, v1):
    return (
        v0[0] - v1[0],
        v0[1] - v1[1],
        )

def z_assign(x,y):
    r = 300
    return (
        math.sqrt(math.pow(r, 2) - (math.pow(x[0], 2) + math.pow(y[0], 2))) if (math.pow(x[0], 2) + math.pow(y[0], 2) <= math.pow(r, 2) / 2) else (math.pow(r, 2) / 2) / math.sqrt(pow(x[0], 2) + math.pow(y[0], 2)),
        math.sqrt(math.pow(r, 2) - (math.pow(x[1], 2) + math.pow(y[1], 2))) if (math.pow(x[1], 2) + math.pow(y[1], 2) <= math.pow(r, 2) / 2) else (math.pow(r, 2) / 2) / math.sqrt(pow(x[1], 2) + math.pow(y[1], 2)),
        )

def Cube():

    glBegin(GL_QUADS)

    for surface in surfaces:
        x = 0
        for vertex in surface:
            x += 1
            glColor3fv(colors[x])
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in edges:
       for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def Ref_Frame():

    glBegin(GL_LINES)

    x = 0
    for line in axis_lines:
        for point in line:
            glColor3fv(colors[x])
            glVertex3fv(axis_points[point])
        x += 1
    glEnd()


def main():
    pygame.init()
    display = (600,600)
    pygame.display.set_mode(display, pygame.DOUBLEBUF|OPENGL)
    pygame.display.set_caption('This is a cube')

    gluPerspective(45, (display[0]/display[1]), 0.1, 15.0)

    glTranslatef(0,0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F4 and bool(event.mod & pygame.KMOD_ALT):
                    pygame.quit()
                    quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                flag = True
                while flag:
                    for event2 in pygame.event.get():
                        if event2.type == pygame.MOUSEBUTTONUP:
                            flag = False
                    pos_2 = pygame.mouse.get_pos()
                    print pos_2
                    pos_1 = sub_v2v2(pos_2,pygame.mouse.get_rel())
                    print pos_1
                    x = (pos_1[0],pos_2[0])
                    y = (pos_1[1], pos_2[1])
                    z = z_assign(x,y)
                    print z
                    v1 = mul_v3_fl( (x[0],y[0],z[0]), 1 / euc_distance((0,0,0), (x[0],y[0],z[0])) )
                    v2 = mul_v3_fl( (x[1],y[1],z[1]), 1 / euc_distance((0,0,0), (x[1],y[1],z[1])) )
                    N = cross(v1,v2)
                    d = dot_v3v3(v1,v2)
                    print d
                    theta = math.acos(d)
                    print N
                    # print theta
                    # glRotatef(theta, N[0], N[1], N[2])
                    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
                    Cube()
                    Ref_Frame()
                    pygame.display.flip()
                    pygame.time.wait(10)

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        Ref_Frame()
        pygame.display.flip()
        pygame.time.wait(10)


main()