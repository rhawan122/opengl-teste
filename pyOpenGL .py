import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random


vertices = [
    [1, 1, -1],
    [1, -1, -1],
    [-1, -1, -1],
    [-1, 1, -1],
    [1, 1, 1],
    [1, -1, 1],
    [-1, -1, 1],
    [-1, 1, 1]
]

faces = [
    [0, 1, 2, 3],
    [3, 2, 6, 7],
    [7, 6, 5, 4],
    [4, 5, 1, 0],
    [1, 5, 6, 2],
    [4, 0, 3, 7]
]

def gerar_cor_aleatoria():
    
    return (random.random(), random.random(), random.random())

cores = [gerar_cor_aleatoria() for _ in faces]

def desenhar_cubo():
    
    glBegin(GL_QUADS)  
    for i in range(len(faces)):
        glColor3fv(cores[i])  
        for j in faces[i]:
            glVertex3fv(vertices[j])  
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5) 

    glEnable(GL_DEPTH_TEST) 

    rotacao_x, rotacao_y = 0, 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    rotacao_y -= 5
                elif event.key == K_RIGHT:
                    rotacao_y += 5
                elif event.key == K_UP:
                    rotacao_x -= 5
                elif event.key == K_DOWN:
                    rotacao_x += 5

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        glPushMatrix()  
        glRotatef(rotacao_x, 1, 0, 0)  
        glRotatef(rotacao_y, 0, 1, 0)  
        desenhar_cubo()  
        glPopMatrix()  
        
        pygame.display.flip()  
        pygame.time.wait(10)  
if __name__ == "__main__":
    main()
