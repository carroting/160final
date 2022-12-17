import pygame
import consts
import choicesmod

c = consts
cm = choicesmod

def startgame():
    oneNPC = c.screen.blit(c.one_standing_left[0],(3.5 *c.screenx / 5 - 70,200 + 10))
    twoNPC = c.screen.blit(c.two_standing_right[0],(1.5 * c.screenx/5,200))
    pygame.display.update()
    cm.options('start game','male','female')
    if c.choice == 1 or c.choice == 2:
        if c.choice == 1:
            c.gender = 'm'
        elif c.choice == 2:
            c.gender = 'f'
        c.playercharachosen = True
        
