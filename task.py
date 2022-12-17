import pygame

import consts

c = consts

#n for day #

def endofday(x):
    n = x - 1
    if n < 10:
        if c.jellylist[n] == None:
            c.jellylist[n] = False
            
        if c.richlist[n] == None:
            c.richlist[n] = False
        
        if c.studentlist[n] == None:
            c.studentlist[n] = False
            
        if c.doctorlist[n] == None:
            c.doctorlist[n] = False
            
        if c.ownerlist[n] == None:
            c.ownerlist[n] = False

        if c.darklist[n] == None:
            c.darklist[n] = False

        if c.drevlist[n] == None:
            c.drevlist[n] = False

def tasks(name, n):
    if name == 'Jelly' and c.jellylist[n] == None:
        c.jellylist[n] = True
        c.jheart += 1
            
    if name == 'Richard' and c.richlist[n] == None:
        c.richlist[n] = True
        c.rheart += 1
            
    if name == 'Student' and c.studentlist[n] == None:
        c.studentlist[n] = True
        c.sheart += 1
            
    if name == 'Doctor' and c.doctorlist[n] == None:
        c.doctorlist[n] = True
        c.dheart += 1
            
    if name == 'Owner' and c.ownerlist[n] == None:
        c.ownerlist[n] = True
        c.oheart += 1
        
    if name == 'Drev' and c.drevlist[n] == None:
        c.drevlist[n] = True
        c.vheart += 1

    if name == 'Dark' and c.darklist[n] == None:
        c.darklist[n] = True
        c.kheart += 1
