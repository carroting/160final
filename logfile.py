import pygame,sys
from pygame import *
from pygame.sprite import *
from pygame import Color, Surface
import consts

c = consts

#DIALOG/MESSAGE BOXES
def dialogFunc(coord = '', character = '', line = '', linetwo = '', linethree = ''):
    log = Dialog(coord, character, line, linetwo, linethree)
    log.box()
    c.wait = True
    c.text_box = True
    log.display_text()

def endlog():
    c.enddialog = True
    c.text_box = False
    c.choice = 0

def controls():
    c.text_box = True
    dialogFunc('center','CONTROLS','use ARROW keys to move, ALT to jump', 'Y to talk to characters, SPACE when going through messages','ESC to escape this dialog')

class Dialog(pygame.sprite.Sprite):
    def __init__(self, coord, character, line = '', linetwo = '', linethree = ''):        
        self.coord = coord
        self.character = character
        self.line = line
        self.linetwo = linetwo
        self.linethree = linethree

        self.rect = c.pokedialog.get_rect()

        self.x = 0
        self.y = 0

        #for bottom left coord
        self.blx = 10
        self.bly = 350
        #for top right coord
        self.rtx = 340
        self.rty = 5
        #for center
        self.centerx = c.screenx/2 - c.pokewidth/2
        self.centery = c.screeny/2 - c.pokeheight/2

    def display_text(self):
        """1 - 3 lines of dialog in one box"""
        #for the lazy me who does not want to code a lot more lines lol
        tb = c.font.render(self.character + ':', True, (0,0,0))
        c.dialogscreen.blit(tb,(self.x+20,self.y+20))
        tb = c.font.render(self.line, True, (0,0,0))
        c.dialogscreen.blit(tb,(self.x+20,self.y+35))
        tb = c.font.render(self.linetwo, True, (0,0,0))
        c.dialogscreen.blit(tb,(self.x+20,self.y+55))
        tb = c.font.render(self.linethree, True, (0,0,0))
        c.dialogscreen.blit(tb,(self.x+20,self.y+75))
    
    def box(self):
        if self.coord == 'bl':
            self.x = self.blx
            self.y = self.bly
        elif self.coord == 'rt':
            self.x = self.rtx
            self.y = self.rty
        elif self.coord == 'center':
            self.x = self.centerx
            self.y = self.centery
        pygame.draw.rect(c.dialogscreen, (237, 240, 250),(self.x + 5,self.y + 5,c.pokewidth - 10,c.pokeheight - 10))
        c.dialogscreen.blit(c.pokedialog, (self.x,self.y))
        c.pokex = self.x
        c.pokey = self.y
