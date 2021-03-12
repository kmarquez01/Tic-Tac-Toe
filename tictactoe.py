import pygame
import sys
import os
import random
import math
import numpy

pygame.init()

WIDTH = 750
HEIGHT = 750

COLOR = (26, 37, 54)

LINE_WIDTH = 15

LINE_COLOR = (0, 0, 0)

BROWS = 3

BCOLS = 3

CRADIUS = 60

CWIDTH = 15

CCWIDTH = 25

GAP = 55

screen = pygame.display.set_mode( (WIDTH, HEIGHT) )

pygame.display.set_caption( "Tic Tac Toe")

font = pygame.font.SysFont('arial', 14)

text = font.render('Game has ended! Press "R" to restart', True, (255,255,255), LINE_COLOR)

text1 = font.render('A tie! Restart by pressing "R"!', True, (255, 255, 255), LINE_COLOR)

text2 = font.render('Choose another square!', True, (255, 255, 255), LINE_COLOR)

border = text.get_rect()

border.center = (375, 10)

screen.fill(COLOR)

def lines():
    
    pygame.draw.line(screen, LINE_COLOR, (0,250), (750, 250), LINE_WIDTH)

    pygame.draw.line(screen, LINE_COLOR, (0,500), (750, 500), LINE_WIDTH)

    pygame.draw.line(screen, LINE_COLOR, (250,0), (250, 800), LINE_WIDTH)

    pygame.draw.line(screen, LINE_COLOR, (500,0), (500, 800), LINE_WIDTH)
   
lines()

board = numpy.zeros( (BROWS, BCOLS) )


def chosensquare(player, row, col):
    board[row][col] = player


def vacantsquare(row, col):
    if board[row][col] == 0:
        return True

    elif board[0][0] != 0:
        screen.blit(text2, border)
        return False
    

    elif board[0][1] != 0:
        screen.blit(text2, border)
        return False

 

    elif board[0][2] != 0:
        screen.blit(text2, border)
        return False


    elif board[1][0] != 0:
        screen.blit(text2, border)
        return False
 

    elif board[1][1] != 0:
        screen.blit(text2, border)
        return False
 

    elif board[1][2] != 0:
        screen.blit(text2, border)
        return False
        
    else:
        screen.blit(text1, border)

    return False


def fullboard():
    for row in range(BROWS):
        for col in range(BCOLS):
            if board[row][col] != 0:
                return True
            else:       
                return False

print(fullboard())

                
def shapes():
    for row in range(BROWS):
        for col in range(BCOLS):
            if board[row][col] == 1:
                centerx = int(col * 250 + 750 / 6)
                centery = int(row * 250 + 750 / 6)
                pygame.draw.circle(screen, LINE_COLOR, (centerx, centery), CRADIUS, CWIDTH)
            elif board[row][col] == 2:
                linestart = int(col * 250)
                linestart1 = int(row * 250 + 250)
                linend = int(row * 250)
                linend1 = int(col * 250 + 250)
                pygame.draw.line(screen, LINE_COLOR, (linestart + GAP, linestart1 - GAP), (linend1 - GAP, linend + GAP), CCWIDTH)
                pygame.draw.line(screen, LINE_COLOR, (linestart + GAP, linend + GAP), (linend1 - GAP, linestart1 - GAP), CCWIDTH)

print(board)

#    elif board[0][col] != player and board[1][col] != player and board[2][col] != player and board[row][0] != player and board[row][1] != player and board[row][2] != player and board[0][0] != player and board[1][1] != player and board[2][2] != player and board[0][2] != player and board[1][1] != player and board[2][0] != player: 
#    screen.blit(text1, border)

player = 1

end = True

def computermoves(comp, row, col):
    board[row][col] = comp


def verticalwin(col, player):

    x = col * 250 + 125

    color = (255, 255, 255)
 

    pygame.draw.line(screen, color, (x, 15), (x, HEIGHT - 30), 15)
    screen.blit(text, border)


def horizontalwin(row, player):
    
    y = row * 250 + 125

    color = (255, 255, 255)

    
    pygame.draw.line(screen, color, (15, y), (WIDTH - 30, y), 15)
    screen.blit(text, border)

def diagonalup(player):

    color = (255, 255, 255)


    pygame.draw.line(screen, color, (15, 15), (WIDTH - 30, HEIGHT - 30), 15)
    screen.blit(text, border)

def diagonaldown(player):
    
    color = (255, 255, 255)
    
    pygame.draw.line(screen, color, (15, HEIGHT - 30), (WIDTH - 30, 30), 15)
    screen.blit(text, border)

def restart():
    screen.fill(COLOR)
    lines()
    player = 1
    for row in range(BROWS):
        for col in range(BCOLS):
            board[row][col] = 0

def win(player):
    
    for col in range(BCOLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            verticalwin(col, player)
            print("player wins!")
            
            return True

    for row in range(BROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            horizontalwin(row, player)
            
            print("player wins!")
            return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        diagonalup(player)
        
        print("player wins!")
        
        return True

    if(board[0][2] == player and board[1][1] == player and board[2][0] == player):
        diagonaldown(player)
        
        return True
      
    
    return False

while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.MOUSEBUTTONDOWN and end:

            x = event.pos[0]
            y = event.pos[1]

            chosenrow = int(y // 250)
            chosencol = int(x // 250)

            print("\nx co-ordinate is", chosenrow)
            print("y co-ordinate is", chosencol, "\n")

            if(vacantsquare(chosenrow, chosencol)):
                if player == 1:
                    chosensquare(1, chosenrow, chosencol)
                    if win(player):
                        end = False
                    player = 2
                elif player == 2:
                    chosensquare(2, chosenrow, chosencol)
                    if win(player):
                        end = False
                    player = 1
                
                shapes()
            

                print(board)
            elif(vacantsquare(chosenrow, chosencol) == False):
                print(text)
                
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                end = True
                restart()
        else:
            continue

    pygame.display.update()