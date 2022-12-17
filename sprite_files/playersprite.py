import pygame
import consts
import enriroments

c = consts
e = enriroments

#PLAYER SPRITE
class Player(pygame.sprite.Sprite):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    
    def one_animate(self):
        c.player_x += c.xchange
        c.player_y += c.ychange

        #boundary
        if c.location == 1:
            if c.player_x <= 0:
                c.player_x = 0
            elif c.player_x >= 700:
                c.player_x = 700
        elif c.location == 2:
            if c.player_x <= c.screenx/2 - c.sevenx/2:
                c.player_x = c.screenx/2 - c.sevenx/2
            elif c.player_x >= c.screenx/2 + c.sevenx/2 - 60:
                c.player_x = c.screenx/2 + c.sevenx/2 - 60
        elif c.location == 3:
            if c.player_x <= 0:
                c.player_x = 0
            elif c.player_x >= 700:
                c.player_x = 700
        elif c.location == 4:
            if c.player_x <= c.screenx/2 - c.dinerx/2:
                c.player_x = c.screenx/2 - c.dinerx/2
            elif c.player_x >= c.screenx/2 + c.dinerx/2 - 60:
                c.player_x = c.screenx/2 + c.dinerx/2 - 60
            
        #counters for frame by frame
        if c.walkCount + 1 >= 60:
            c.walkCount = 0
        if c.jumpCount + 1 >= 20:
            c.ychange = 0
            c.jumpCount = 0
            c.jump = False
        if c.standCount + 1 >= 60:
            c.standCount = 0

        #animations
        if c.walk and c.jump:
            c.jumpCount += 1
            if c.jumpCount < 20/2:
                c.player_y -= pow(c.jumpCount,1/2)*1.5
            elif c.jumpCount > 20/2:
                c.player_y += pow(c.jumpCount - 20/2,1/2)*1.5
                
            if c.left:
                if c.walk_left:
                    c.player_x -= 1
                c.characterscreen.blit(c.one_jump_left, (c.player_x,c.player_y))
            if c.right:
                if c.walk_right:
                    c.player_x += 1
                c.characterscreen.blit(c.one_jump_right, (c.player_x,c.player_y))
        elif c.walk:
            if c.walk_left:
                c.characterscreen.blit(c.one_walk_left[c.walkCount//15], (c.player_x,c.player_y))
                c.walkCount += 1
            elif c.walk_right:
                c.characterscreen.blit(c.one_walk_right[c.walkCount//15], (c.player_x,c.player_y))
                c.walkCount += 1
        elif c.jump:
            c.jumpCount += 1
            if c.jumpCount < 20/2:
                c.player_y -= pow(c.jumpCount,1/2)*1.5
            elif c.jumpCount > 20/2:
                c.player_y += pow(c.jumpCount - 20/2,1/2)*1.5
                
            if c.left:
                c.characterscreen.blit(c.one_jump_left, (c.player_x,c.player_y))
            if c.right:
                c.characterscreen.blit(c.one_jump_right, (c.player_x,c.player_y))
        elif not(c.jump) and not(c.walk):
            c.walkCount = 0
            c.jumpCount = 0
            if c.left:
                c.characterscreen.blit(c.one_standing_left[c.standCount//20],(c.player_x,c.player_y))
                c.standCount += 1
            elif c.right:
                c.characterscreen.blit(c.one_standing_right[c.standCount//20],(c.player_x,c.player_y))
                c.standCount += 1
    def two_animate(self):
        c.player_x += c.xchange
        c.player_y += c.ychange

        #boundary
        if c.location == 1:
            if c.player_x <= 0:
                c.player_x = 0
            elif c.player_x >= 700:
                c.player_x = 700
        elif c.location == 2:
            if c.player_x <= c.screenx/2 - c.sevenx/2:
                c.player_x = c.screenx/2 - c.sevenx/2
            elif c.player_x >= c.screenx/2 + c.sevenx/2 - 60:
                c.player_x = c.screenx/2 + c.sevenx/2 - 60
        elif c.location == 3:
            if c.player_x <= 0:
                c.player_x = 0
            elif c.player_x >= 700:
                c.player_x = 700
        elif c.location == 4:
            if c.player_x <= c.screenx/2 - c.dinerx/2:
                c.player_x = c.screenx/2 - c.dinerx/2
            elif c.player_x >= c.screenx/2 + c.dinerx/2 - 60:
                c.player_x = c.screenx/2 + c.dinerx/2 - 60
            
        #counters for frame by frame
        if c.walkCount + 1 >= 60:
            c.walkCount = 0
        if c.jumpCount + 1 >= 20:
            c.ychange = 0
            c.jumpCount = 0
            c.jump = False
        if c.standCount + 1 >= 60:
            c.standCount = 0

        #animations
        if c.walk and c.jump:
            c.jumpCount += 1
            if c.jumpCount < 20/2:
                c.player_y -= pow(c.jumpCount,1/2)*1.5
            elif c.jumpCount > 20/2:
                c.player_y += pow(c.jumpCount - 20/2,1/2)*1.5
                
            if c.left:
                if c.walk_left:
                    c.player_x -= 1
                c.characterscreen.blit(c.two_jump_left, (c.player_x,c.player_y))
            if c.right:
                if c.walk_right:
                    c.player_x += 1
                c.characterscreen.blit(c.two_jump_right, (c.player_x,c.player_y))
        elif c.walk:
            if c.walk_left:
                c.characterscreen.blit(c.two_walk_left[c.walkCount//15], (c.player_x,c.player_y))
                c.walkCount += 1
            elif c.walk_right:
                c.characterscreen.blit(c.two_walk_right[c.walkCount//15], (c.player_x,c.player_y))
                c.walkCount += 1
        elif c.jump:
            c.jumpCount += 1
            if c.jumpCount < 20/2:
                c.player_y -= pow(c.jumpCount,1/2)*1.5
            elif c.jumpCount > 20/2:
                c.player_y += pow(c.jumpCount - 20/2,1/2)*1.5
                
            if c.left:
                c.characterscreen.blit(c.two_jump_left, (c.player_x,c.player_y))
            if c.right:
                c.characterscreen.blit(c.two_jump_right, (c.player_x,c.player_y))
        elif not(c.jump) and not(c.walk):
            c.walkCount = 0
            c.jumpCount = 0
            if c.left:
                c.characterscreen.blit(c.two_standing_left[c.standCount//20],(c.player_x,c.player_y))
                c.standCount += 1
            elif c.right:
                c.characterscreen.blit(c.two_standing_right[c.standCount//20],(c.player_x,c.player_y))
                c.standCount += 1
