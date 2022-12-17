import pygame,sys
import user_input_file
import startgame
import consts
import redraw

u = user_input_file
s = startgame
clock = pygame.time.Clock()
c = consts
r = redraw


pygame.init()
# main
while True:
    
    u.userinput()
    if c.playercharachosen:
        r.redrawGameWindow(c.gender)
    else:
        s.startgame()
    clock.tick(60)
