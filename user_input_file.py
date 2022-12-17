import pygame, sys
import consts
import task
import logfile

c = consts
t = task
l = logfile

pygame.init()
def userinput():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #KEY UP
        if event.type == pygame.KEYUP:
            #LEFT AND RIGHT
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                c.walk = False
                c.xchange = 0
                c.walkCount = 0
                c.walk_left = False
                c.walk_right = False
            #Y
            if event.key == pygame.K_y:
                if c.ypressed and c.enddialog:
                    c.textCount = 0
            if event.key == pygame.K_SPACE:
                if c.text_box == False:
                    c.ypressed = False
                elif c.spacepressed:
                     c.textCount +=1
                     c.wait = False
                     c.spacepressed = False
        #KEY DOWN
        if event.type == pygame.KEYDOWN:
            #E END DAY
            if event.key == pygame.K_e:
                if c.daily == 1:
                    c.dayCount += 1
                    c.daily = 0
                    t.endofday(c.dayCount)        
            #ESC SHOW CONTROLS
            if event.key == pygame.K_ESCAPE:
                if not(c.showcontrols):
                    c.showcontrols = True
                elif c.showcontrols:
                    c.showcontrols = False
            #Y INTERACT
            if event.key == pygame.K_y:
                if c.distance:
                    c.ypressed = True
            #SPACE AND TEXT_BOX
            if event.key == pygame.K_SPACE and c.text_box:
                if c.wait:
                    c.spacepressed = True
            #ALT JUMP
            if event.key == pygame.K_RALT or event.key == pygame.K_LALT:
                c.jump = True
            #LEFT MOVE
            if event.key == pygame.K_LEFT:
                c.walk = True
                c.walk_left = True
                c.walk_right = False
                c.left = True
                c.right = False
                c.xchange = -2.5
                if c.jump:
                    c.xchange = -4
            #RIGHT MOVE
            elif event.key == pygame.K_RIGHT:
                c.walk = True
                c.walk_left = False
                c.walk_right = True
                c.left = False
                c.right = True
                c.xchange = 2.5
                if c.jump:
                    c.xchange = 4
            #1 2 3 4 LOCATION CHANGE
            elif event.key == pygame.K_1 or \
               event.key == pygame.K_2 or \
               event.key == pygame.K_3 or \
               event.key == pygame.K_4:
                if c.daily == 1:
                    if c.ypressed:
                        c.ypressed = False
                        textCount = 0
                    if event.key == pygame.K_1 and not(c.location == 1):
                        c.location = 1 #outside
                        c.player_x = 600
                    elif event.key == pygame.K_2 and not(c.location == 2):
                        c.location = 2 #7e
                        c.player_x = c.screenx/2 - c.sevenx/2 + 20 #change y in redraw.py
                    elif event.key == pygame.K_3 and not(c.location == 3):
                        c.location = 3 #doctor
                        c.player_x = 50 #change y in redraw.py
                    elif event.key == pygame.K_4 and not(c.location == 4):
                        c.location = 4
                        c.player_x = 200
