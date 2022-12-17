import pygame
import consts
import enriroments
import tenloop
import logfile
c = consts
e = enriroments
t = tenloop
l = logfile

def redrawGameWindow(gender):
    if c.daily == 0:
        location = 1
        c.screen.blit(c.sky,(0,0))
        e.building(1, 150, c.ground)
        e.cityterrain(1)
        one_y = c.ground - 72
        two_y = c.ground - 82
    elif c.daily == 1:
        if c.location == 1:
            c.screen.blit(c.sky,(0,0))
            e.building(1, 150, c.ground)
            e.cityterrain(1)
            one_y = c.ground - 72
            two_y = c.ground - 82
            c.jelly.stand_left()
            c.rich.stand_right()
        elif c.location == 2:
            c.screen.fill((0,0,0))
            e.cityterrain(2)
            one_y = c.ground - 146
            two_y = c.ground - 160
            c.student.x = c.sx
            c.student.y = c.sy
            if c.dayCount != 2 or c.dayCount != 5 or c.dayCount != 7:
                c.student.stand_left()

        elif c.location == 3:
            c.screen.fill((0,0,0))
            e.cityterrain(3)
            one_y = c.ground - 72 - 43
            two_y = c.ground - 82 - 43
            c.doctor.stand_right()
            if c.dayCount == 2 or c.dayCount == 5 or c.dayCount == 7:
                c.student.x = c.sx - 150
                c.student.y = c.sy + 35
                c.student.stand_right()
        elif c.location == 4:
            c.screen.fill((0,0,0))
            e.cityterrain(4)
            one_y = c.ground - 72 - 70 
            two_y = c.ground - 82 - 70
            c.drev.stand_right()
            c.dark.stand_left()
    if c.gender == 'm':
        c.player_y = one_y
        c.playername = 'One'
        c.one.one_animate()
    elif c.gender == 'f':
        c.player_y = two_y
        c.playername = 'Two'
        c.two.two_animate()
    if c.showcontrols:
        l.controls()

    t.dailytens()
    
    pygame.display.update()
