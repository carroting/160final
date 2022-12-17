import pygame
import consts

c = consts

pygame.init()
#ENVIRONMENTS
#location = 1
def buildground(y):
    cityunder_list = c.cityunder_list
    cityunder_rect = c.cityunder_rect
    cityterrain_list = c.cityterrain_list
    cityterrain_rect = c.cityterrain_rect
    cttotalwidth = 0
    for i in range(len(cityterrain_list)):
        cttotalwidth += cityterrain_rect[i]
    ctrepetition = int(c.screenx / cttotalwidth + 1)
    
    tempx = 0        
    for i in range(ctrepetition + 1):
        for j in range(len(cityterrain_list)):
            c.buildscreen.blit(cityterrain_list[j],(tempx,y))
            tempx += cityterrain_rect[j]
                
def cityterrain(n):
    cityunder_list = c.cityunder_list
    cityunder_rect = c.cityunder_rect
    cityterrain_list = c.cityterrain_list
    cityterrain_rect = c.cityterrain_rect
    
    if n == 1:
        """Edelstein template"""
        cutotalwidth = 0
        for i in range(len(cityunder_list)):
            cutotalwidth += cityunder_rect[i]
        curepetition = int(c.screenx / cutotalwidth + 1)

        tempx = 0
        
        for i in range(curepetition + 1):
            for j in range(len(cityunder_list)):
                c.buildscreen.blit(cityunder_list[j],(tempx,c.ground))
                tempx += cityunder_rect[j]
        buildground(c.ground)
                
    elif n == 2:
        """grocery or 7e lol"""
        c.buildscreen.blit(c.sevene, (c.screenx/2 - c.sevenx/2,c.screeny/2 - c.seveny/2))
        c.owner.stand()
        c.buildscreen.blit(c.cashr, (c.screenx/2 + c.sevenx/2 - 68, c.screeny/2 + 55))
    elif n == 3:
        """doctor's"""
        c.buildscreen.blit(c.hospital, (0,c.screenx/2 - 618/2 - 20))
        buildground(c.ground - 43)
    elif n == 4:
        """diner"""
        c.buildscreen.blit(c.diner, (c.screenx/2 - c.dinerx/2,c.screeny/2 - c.dinery/2))
        
def building(n, x, y):
    """ to print a singular building """
    house_list = c.house_list
    house_height = []
    house_width = []
    for i in range(len(house_list)):
        house_height.append(pygame.Surface.get_height(house_list[i]))
        house_width.append(pygame.Surface.get_width(house_list[i]))
    #i hope that if you are reading this that you realize that i got lazy and didn't want to load in anymore houses.
    #house1:
    if n == 1:
        c.buildscreen.blit(house_list[4],(-house_width[4] + x,c.ground - house_height[4]))
        c.buildscreen.blit(house_list[5],(-house_width[5] + x, c.ground - house_height[4] - house_height[5]))
        for i in range(4):
            y -= house_height[i]
            c.buildscreen.blit(house_list[i],(x,y))
