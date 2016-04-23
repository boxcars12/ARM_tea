import pygame
from pygame.locals import *

import math

from OpenGL.GL import *
from OpenGL.GLU import *

lines = (
    (0,1),
    (1,2),
)

def pitch(v1, n, theta):
    theta = math.radians(theta)
    return add_v3v3(mul_v3_fl(v1,math.cos(theta)),cross(n,mul_v3_fl(v1,math.sin(theta))))

def cross(a, b):
    c = [a[1]*b[2] - a[2]*b[1],
         a[2]*b[0] - a[0]*b[2],
         a[0]*b[1] - a[1]*b[0]]

    return c

def add_v3v3(v0, v1):
    return (
        v0[0] + v1[0],
        v0[1] + v1[1],
        v0[2] + v1[2],
        )

def mul_v3_fl(v0, f):
    return (
        v0[0] * f,
        v0[1] * f,
        v0[2] * f,
        )

def arm(vertices):

    glBegin(GL_LINES)

    for line in lines:

        for vertex in line:
            glVertex3fv(vertices[vertex])

    glEnd()


def main():

    pygame.init()
    display = (600,600)
    pygame.display.set_mode(display, pygame.DOUBLEBUF|OPENGL)
    pygame.display.set_caption('This is an Arm')

    gluPerspective(45, (display[0]/display[1]), 0.1, 15.0)

    glTranslatef(0, -1, -5)

    theta1 = 0
    theta2 = 0
    u1 = (0,0,0)
    l1 = 1
    l2 = 1

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F4 and bool(event.mod & pygame.KMOD_ALT):
                    pygame.quit()
                    quit()
                if event.key == pygame.K_UP:
                    theta1 += 5
                if event.key == pygame.K_DOWN:
                    theta1 -= 5
                if event.key == pygame.K_LEFT:
                    theta2 += 5
                if event.key == pygame.K_RIGHT:
                    theta2 -= 5


        u12 = pitch((0,1,0),(0,0,1),theta1)
        u2 = add_v3v3(u1, mul_v3_fl(u12,l1))

        u23 = pitch(u12,(0,0,1),theta2)
        u3 = add_v3v3(u2, mul_v3_fl(u23, l2))

        vertices = (
            u1,
            u2,
            u3,
        )

        glRotatef(1,0,1,0)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        arm(vertices)
        pygame.display.flip()
        pygame.time.wait(10)

main()