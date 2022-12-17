import pygame,sys
from pygame import *
from pygame.sprite import *
from pygame import Color, Surface
from tkinter import *


pygame.init()
clock = pygame.time.Clock()
screenx = 720
screeny = 450
font = pygame.font.SysFont('georgia',10)

#distinguish layers
screen = display.set_mode((screenx,screeny))
buildscreen = display.set_mode((screenx,screeny))
characterscreen = display.set_mode((screenx,screeny))
npcscreen = display.set_mode((screenx,screeny))
dialogscreen = display.set_mode((screenx,screeny))

display.set_caption("final project")
skytemp = pygame.image.load('sky.png').convert_alpha()
sky = pygame.transform.scale(skytemp, (720,450))

#DIALOG
pokediaimg = pygame.image.load('dialog.png').convert_alpha()
pokeheight = pygame.Surface.get_height(pokediaimg)/4
pokewidth = pygame.Surface.get_width(pokediaimg)/4
pokedialog = pygame.transform.scale(pokediaimg, (pokewidth,pokeheight))
pokex = 0
pokey = 0

text_box = True
textCount = 0
daily = 0
location = 1
ypressed = False
enddialog = True
log = False #for conversations
distance = False #range
showcontrols = False

#CHOICES
choice = 0
A = ''
B = ''
C = ''

#DAY COUNT starts at day 0 and ends at day 10
dayCount = 0

#PLAYER SETTINGS
#player defaults aka beginning screen
playercharachosen = False
gender = ''

#player's initial animation state
jump = False
walk_left = False
walk_right = False
left = True
right = False
walk = False

jumpCount = 0
walkCount = 0
standCount = 0

#player location
ground = 422
player_x = 600
player_y = 0
xchange = 0
ychange = 0

#PLAYER IMAGES
#one's images
one_standing_left = [pygame.image.load('spritesheet\standingOneHanded-0.png').convert_alpha(), pygame.image.load('spritesheet\standingOneHanded-1.png').convert_alpha(), pygame.image.load('spritesheet\standingOneHanded-2.png').convert_alpha()]
one_standing_right = [pygame.transform.flip(one_standing_left[0], True, False), pygame.transform.flip(one_standing_left[1], True, False), pygame.transform.flip(one_standing_left[2], True, False)]
one_walk_left = [pygame.image.load('spritesheet\walkingOneHanded-0.png').convert_alpha(),pygame.image.load('spritesheet\walkingOneHanded-1.png').convert_alpha(),pygame.image.load('spritesheet\walkingOneHanded-2.png').convert_alpha(),pygame.image.load('spritesheet\walkingOneHanded-3.png').convert_alpha()]
one_walk_right = [pygame.transform.flip(one_walk_left[0],True,False),pygame.transform.flip(one_walk_left[1],True,False),pygame.transform.flip(one_walk_left[2],True,False),pygame.transform.flip(one_walk_left[3],True,False)]
one_jump_left = pygame.image.load('spritesheet\jumping-0.png').convert_alpha()
one_jump_right = pygame.transform.flip(one_jump_left,True,False)
#two's images
two_standing_left = [pygame.image.load('two\standingOneHanded-0.png').convert_alpha(), pygame.image.load('two\standingOneHanded-1.png').convert_alpha(), pygame.image.load('two\standingOneHanded-2.png').convert_alpha()]
two_standing_right = [pygame.transform.flip(two_standing_left[0], True, False), pygame.transform.flip(two_standing_left[1], True, False), pygame.transform.flip(two_standing_left[2], True, False)]
two_walk_left = [pygame.image.load('two\walkingOneHanded-0.png').convert_alpha(),pygame.image.load('two\walkingOneHanded-1.png').convert_alpha(),pygame.image.load('two\walkingOneHanded-2.png').convert_alpha(),pygame.image.load('two\walkingOneHanded-3.png').convert_alpha()]
two_walk_right = [pygame.transform.flip(two_walk_left[0],True,False),pygame.transform.flip(two_walk_left[1],True,False),pygame.transform.flip(two_walk_left[2],True,False),pygame.transform.flip(two_walk_left[3],True,False)]
two_jump_left = pygame.image.load('two\jumping-0.png').convert_alpha()
two_jump_right = pygame.transform.flip(two_jump_left,True,False)

#NPC IMAGES
#fisherman
fish_standing_left = [pygame.image.load('fisherman\standingOneHanded-0.png').convert_alpha(), pygame.image.load('fisherman\standingOneHanded-1.png').convert_alpha(), pygame.image.load('fisherman\standingOneHanded-2.png').convert_alpha()]
fish_standing_right = [pygame.transform.flip(fish_standing_left[0], True, False), pygame.transform.flip(fish_standing_left[1], True, False), pygame.transform.flip(fish_standing_left[2], True, False)]
#jellylemon
jelly_standing_left = [pygame.image.load('jellylemon\standingOneHanded-0.png').convert_alpha(), pygame.image.load('jellylemon\standingOneHanded-1.png').convert_alpha(), pygame.image.load('jellylemon\standingOneHanded-2.png').convert_alpha()]
jelly_standing_right = [pygame.transform.flip(jelly_standing_left[0], True, False), pygame.transform.flip(jelly_standing_left[1], True, False), pygame.transform.flip(jelly_standing_left[2], True, False)]
#student in 7e
student_standing_left = [pygame.image.load('student\standingOneHanded-0.png').convert_alpha(), pygame.image.load('student\standingOneHanded-1.png').convert_alpha(), pygame.image.load('student\standingOneHanded-2.png').convert_alpha()]
student_standing_right = [pygame.transform.flip(student_standing_left[0], True, False), pygame.transform.flip(student_standing_left[1], True, False), pygame.transform.flip(student_standing_left[2], True, False)]

#DIALOG/MESSAGE BOXES
def dialogFunc(coord = '', character = '', line = '', linetwo = '', linethree = ''):
    log = Dialog(coord, character, line, linetwo, linethree)
    log.box()
    log.display_text()
    
class Dialog(pygame.sprite.Sprite):
    def __init__(self, coord, character, line = '', linetwo = '', linethree = ''):
        global pokewidth, screenx
        
        self.coord = coord
        self.character = character
        self.line = line
        self.linetwo = linetwo
        self.linethree = linethree

        self.rect = pokedialog.get_rect()

        self.x = 0
        self.y = 0

        #for bottom left coord
        self.blx = 10
        self.bly = 320
        #for top right coord
        self.rtx = 340
        self.rty = 5
        #for center
        self.centerx = screenx/2 - pokewidth/2
        self.centery = screeny/2 - pokeheight/2

    def display_text(self):
        #for the lazy me who does not want to code a lot more lines lol
        textbox = font.render(self.character + ':', True, (0,0,0))
        dialogscreen.blit(textbox,(self.x+20,self.y+20))
        textbox = font.render(self.line, True, (0,0,0))
        dialogscreen.blit(textbox,(self.x+20,self.y+35))
        textbox = font.render(self.linetwo, True, (0,0,0))
        dialogscreen.blit(textbox,(self.x+20,self.y+55))
        textbox = font.render(self.linethree, True, (0,0,0))
        dialogscreen.blit(textbox,(self.x+20,self.y+75))
    
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
        pygame.draw.rect(dialogscreen, (237, 240, 250),(self.x + 5,self.y + 5,pokewidth - 10,pokeheight - 10))
        dialogscreen.blit(pokedialog, (self.x,self.y))
        pokex = self.x
        pokey = self.y

#ENVIRONMENTS
#location = 2
seveneimg = pygame.image.load('7-eleven.png').convert_alpha()
sevenex = pygame.Surface.get_width(seveneimg)
seveney = pygame.Surface.get_height(seveneimg)
sevene = pygame.transform.scale(seveneimg, (sevenex * 1, seveney*1))
crimg = pygame.image.load('7eleven_cashregister.png').convert_alpha()
#location = 1
def cityterrain():
    """Edelstein template"""
    global ground
    cityterrain_list = [pygame.image.load('Edelstein\city\city terrain (10).png').convert_alpha(), pygame.image.load('Edelstein\city\city terrain (11).png').convert_alpha(), pygame.image.load('Edelstein\city\city terrain (12).png').convert_alpha(),pygame.image.load('Edelstein\city\city terrain (13).png').convert_alpha()]
    cityterrain_rect = [pygame.Surface.get_width(cityterrain_list[0]),pygame.Surface.get_width(cityterrain_list[1]),pygame.Surface.get_width(cityterrain_list[2]),pygame.Surface.get_width(cityterrain_list[3])]
    totalwidth = 0
    for i in range(len(cityterrain_list)):
        totalwidth += cityterrain_rect[i]
    repetition = int(screenx / totalwidth + 1)

    tempx = 0
    
    for i in range(repetition + 1):
        for j in range(len(cityterrain_list)):
            buildscreen.blit(cityterrain_list[j],(tempx,ground))
            tempx += cityterrain_rect[j]
def building(n, x, y):
    """ to print a singular building """
    global ground
    house_list = [pygame.image.load('Edelstein\city\house (1).png').convert_alpha(),pygame.image.load('Edelstein\city\house (2).png').convert_alpha(),pygame.image.load('Edelstein\city\house (3).png').convert_alpha(),pygame.image.load('Edelstein\city\house (4).png').convert_alpha(),pygame.image.load('Edelstein\city\house (5).png').convert_alpha(),pygame.image.load('Edelstein\city\house (6).png').convert_alpha(),pygame.image.load('Edelstein\city\house (7).png').convert_alpha(),pygame.image.load('Edelstein\city\house (8).png').convert_alpha(),pygame.image.load('Edelstein\city\house (9).png').convert_alpha(),pygame.image.load('Edelstein\city\house (10).png').convert_alpha()]
    house_height = []
    house_width = []
    for i in range(len(house_list)):
        house_height.append(pygame.Surface.get_height(house_list[i]))
        house_width.append(pygame.Surface.get_width(house_list[i]))
    #house1:
    if n == 1:
        buildscreen.blit(house_list[4],(-house_width[4] + x,ground - house_height[4]))
        buildscreen.blit(house_list[5],(-house_width[5] + x, ground - house_height[4] - house_height[5]))
        for i in range(4):
            y -= house_height[i]
            buildscreen.blit(house_list[i],(x,y))
            
#NPC CLASS is just for organization
#fisherman = NPC('standing_left',0,0)
#fisherman.fisherman()
class NPC(pygame.sprite.Sprite):
    def __init__(self,name,action,x,y):
        self.name = name
        self.action = action
        self.x = x
        self.y = y
        self.hearts = 0
    def interaction(self):
        global log, text_box, enddialog
        self.hearts += .5
        if ypressed:
            if self.hearts < 2:
                if self.name == 'Student':
                    if textCount < 1:
                        log = True
                        text_box = True
                    else:
                        log = False
                        enddialog = True
                        text_box = False
                    if textCount == 0:
                        dialogFunc('bl', 'Student','Buzz off!')
            if self.hearts < 4:
                if self.name == 'Student':
                    if textCount < 1:
                        log = True
                        text_box = True
                    else:
                        log = False
                        enddialog = True
                        text_box = False
                    if textCount == 0:
                        dialogFunc('bl', 'Student','Buzz off!')
                        
                            
    def one(self):
        global standCount
        if self.action == 'standing_left':
            npcscreen.blit(one_standing_left[standCount//20], (self.x,self.y))
        if self.action == 'standing_right':
            npcscreen.blit(one_standing_right[standCount//20], (self.x,self.y))
    def two(self):
        global standCount
        if self.action == 'standing_left':
            npcscreen.blit(two_standing_left[standCount//20], (self.x,self.y))
        if self.action == 'standing_right':
            npcscreen.blit(two_standing_right[standCount//20], (self.x,self.y))
    def fisherman(self):
        global standCount
        if self.action == 'standing_left':
            npcscreen.blit(fish_standing_left[standCount//20], (self.x,self.y))
        if self.action == 'standing_right':
            npcscreen.blit(fish_standing_right[standCount//20], (self.x,self.y))
    def jelly(self):
        global standCount
        if self.action == 'standing_left':
            npcscreen.blit(jelly_standing_left[standCount//20], (self.x,self.y))
        if self.action == 'standing_right':
            npcscreen.blit(jelly_standing_right[standCount//20], (self.x,self.y))
    def student(self):
        global standCount
        if self.action == 'standing_left':
            npcscreen.blit(student_standing_left[standCount//20], (self.x,self.y))
        if self.action == 'standing_right':
            npcscreen.blit(student_standing_right[standCount//20], (self.x,self.y))

#PLAYER SPRITE
class Player(pygame.sprite.Sprite):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    
    def one_animate(self):
        global jump, walk, walk_left, walk_right, left, right, jumpCount, walkCount, standCount, player_x, player_y, xchange, ychange
        player_x += xchange
        player_y += ychange

        #boundary
        if location == 1 or daily == 0:
            if player_x <= 0:
                player_x = 0
            elif player_x >= 700:
                player_x = 700
        elif location == 2:
            if player_x <= screenx/2 - sevenex/2:
                player_x = screenx/2 - sevenex/2
            elif player_x >= screenx/2 + sevenex/2 - 60:
                player_x = screenx/2 + sevenex/2 - 60
            
        #counters for frame by frame
        if walkCount + 1 >= 60:
            walkCount = 0
        if jumpCount + 1 >= 20:
            ychange = 0
            jumpCount = 0
            jump = False
        if standCount + 1 >= 60:
            standCount = 0

        #animations
        if walk and jump:
            jumpCount += 1
            if jumpCount < 20/2:
                player_y -= pow(jumpCount,1/2)*1.5
            elif jumpCount > 20/2:
                player_y += pow(jumpCount - 20/2,1/2)*1.5
                
            if left:
                if walk_left:
                    player_x -= 1
                characterscreen.blit(one_jump_left, (player_x,player_y))
            if right:
                if walk_right:
                    player_x += 1
                characterscreen.blit(one_jump_right, (player_x,player_y))
        elif walk:
            if walk_left:
                characterscreen.blit(one_walk_left[walkCount//15], (player_x,player_y))
                walkCount += 1
            elif walk_right:
                characterscreen.blit(one_walk_right[walkCount//15], (player_x,player_y))
                walkCount += 1
        elif jump:
            jumpCount += 1
            if jumpCount < 20/2:
                player_y -= pow(jumpCount,1/2)*1.5
            elif jumpCount > 20/2:
                player_y += pow(jumpCount - 20/2,1/2)*1.5
                
            if left:
                characterscreen.blit(one_jump_left, (player_x,player_y))
            if right:
                characterscreen.blit(one_jump_right, (player_x,player_y))
        elif not(jump) and not(walk):
            walkCount = 0
            jumpCount = 0
            if left:
                characterscreen.blit(one_standing_left[standCount//20],(player_x,player_y))
                standCount += 1
            elif right:
                characterscreen.blit(one_standing_right[standCount//20],(player_x,player_y))
                standCount += 1
    def two_animate(self):
        global jump, walk, walk_left, walk_right, left, right, jumpCount, walkCount, standCount, player_x, player_y, xchange, ychange
        player_x += xchange
        player_y += ychange

        #boundary
        if location == 1 or daily == 0:
            if player_x <= 0:
                player_x = 0
            elif player_x >= 700:
                player_x = 700
        elif location == 2:
            if player_x <= screenx/2 - sevenex/2:
                player_x = screenx/2 - sevenex/2
            elif player_x >= screenx/2 + sevenex/2 - 70:
                player_x = screenx/2 + sevenex/2 - 70
            
        #counters for frame by frame
        if walkCount + 1 >= 60:
            walkCount = 0
        if jumpCount + 1 >= 20:
            ychange = 0
            jumpCount = 0
            jump = False
        if standCount + 1 >= 60:
            standCount = 0

        #animations
        if walk and jump:
            jumpCount += 1
            if jumpCount < 20/2:
                player_y -= pow(jumpCount,1/2)*1.1
            elif jumpCount > 20/2:
                player_y += pow(jumpCount - 20/2,1/2)*1.1
                
            if left:
                if walk_left:
                    player_x -= 1
                characterscreen.blit(two_jump_left, (player_x,player_y))
            if right:
                if walk_right:
                    player_x += 1
                characterscreen.blit(two_jump_right, (player_x,player_y))
        elif walk:
            if walk_left:
                characterscreen.blit(two_walk_left[walkCount//15], (player_x,player_y))
                walkCount += 1
            elif walk_right:
                characterscreen.blit(two_walk_right[walkCount//15], (player_x,player_y))
                walkCount += 1
        elif jump:
            jumpCount += 1
            if jumpCount < 20/2:
                player_y -= pow(jumpCount,1/2)*1.1
            elif jumpCount > 20/2:
                player_y += pow(jumpCount - 20/2,1/2)*1.1
                
            if left:
                characterscreen.blit(two_jump_left, (player_x,player_y))
            if right:
                characterscreen.blit(two_jump_right, (player_x,player_y))
        elif not(jump) and not(walk):
            walkCount = 0
            jumpCount = 0
            if left:
                characterscreen.blit(two_standing_left[standCount//20],(player_x,player_y))
                standCount += 1
            elif right:
                characterscreen.blit(two_standing_right[standCount//20],(player_x,player_y))
                standCount += 1

def controls():
    text_box = True
    dialogFunc('center','CONTROLS','use ARROW keys to move, ALT to jump', 'Y to talk to characters, SPACE when going through messages','ESC to escape this dialog')

def dailytens(gender = ''):
    """for the tens of the game"""
    global textCount, text_box, daily,ypressed,enddialog,log,distance
    #name of our main character
    if gender == 'm':
        name = 'One'
    if gender == 'f':
        name = 'Two'
        
    #npc locations
    #fisherman
    fx = 50
    fy = ground - 68
    fisherman = NPC('Fisherman','standing_right',fx,fy)
    #jelly
    jx = 500
    jy = ground - 105
    jelly = NPC('Jelly','standing_left',jx,jy)

    #student
    sx = 300
    sy = ground - 145
    student = NPC('Student','standing_right',sx,sy)

    
    if text_box and daily == 0:
        fisherman.fisherman()
        jelly.jelly()
        if textCount == 0:
            dialogFunc('rt',name,'A shining day indeed. Whatever will I do.')
        elif textCount == 1:
            dialogFunc('rt',name,'How are my relationships with others?')
        elif textCount == 2:
            dialogFunc('rt',name,'Is Perihelion a great place for me to live in?')
        elif textCount > 1:
            textCount = 0
            daily = 1
            text_box = False
    if daily == 1:
        if location == 1:
            fisherman.fisherman()
            jelly.jelly()
            #npc interactions
            if (player_x >= fx - 75 and player_x <= fx + 100) or (player_x >= jx - 75 and player_x <= jx + 100):
                #interact with jelly
                if player_x >= jx - 75 and player_x <= jx + 100:
                    distance = True
                    if ypressed:
                        if textCount < 2:
                            log = True
                            text_box = True
                            if textCount == 0:
                                dialogFunc('rt', 'Jelly','Hello, ' + name)
                            elif textCount == 1:
                                dialogFunc('rt', 'Jelly','You have an interesting aura around you.')
                        else:
                            log = False
                            enddialog = True
                            text_box = False

                #interact with fisherman
                if player_x >= fx - 75 and player_x <= fx + 100:
                    distance = True
                    if ypressed:
                        if textCount < 1:
                            log = True
                            text_box = True
                            if textCount == 0:
                                dialogFunc('rt', 'Fisherman', 'What\'s up, kid? You got something to say??')
                        else:
                            log = False
                            enddialog = True
                            text_box = False
            else:
                if ypressed:
                    ypressed = False
                if distance:
                    distance = False
        elif location == 2:
            student.student()
            if (player_x >= sx - 200 and player_x <= sx + 200):
                #interact with student
                if player_x >= sx - 200 and player_x <= sx + 200:
                    distance = True
                    student.interaction()
        elif location == 3:
            #spawn npcs
            pass
        
def userinput():
    global daily, dayCount,location,showcontrols,distance,log, enddialog, ypressed, textCount,text_box,jump, walk_left, walk_right, left, right, jumpCount, walkCount, standCount, player_x, player_y, xchange, ychange, walk
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                walk = False
                xchange = 0
                walkCount = 0
                walk_left = False
                walk_right = False
            if event.key == pygame.K_y:
                if ypressed and enddialog:
                    textCount = 0
                    distance = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                if daily == 1:
                    dayCount += 1
                    daily = 0
            if event.key == pygame.K_ESCAPE:
                if not(showcontrols):
                    showcontrols = True
                elif showcontrols:
                    showcontrols = False
            if event.key == pygame.K_y:
                if distance:
                    ypressed = True
            if event.key == pygame.K_SPACE and text_box:
                textCount +=1
            if event.key == pygame.K_RALT or event.key == pygame.K_LALT:
                jump = True
            if event.key == pygame.K_LEFT:
                walk = True
                walk_left = True
                walk_right = False
                left = True
                right = False
                xchange = -2.5
                if jump:
                    xchange = -4
            elif event.key == pygame.K_RIGHT:
                walk = True
                walk_left = False
                walk_right = True
                left = False
                right = True
                xchange = 2.5
                if jump:
                    xchange = 4
            if daily == 1:
                if event.key == pygame.K_1:
                    if not(location == 1):
                        location = 1 #outside
                elif event.key == pygame.K_2:
                    if not(location == 2):
                        location = 2 #market
                elif event.key == pygame.K_3:
                    if not(location == 3):
                        location = 3 #doctor
                elif event.key == pygame.K_4:
                    if not(location == 4):
                        location = 4

one = Player("one", "m")
two = Player("two", "f")

def redrawGameWindow(gender):
    global player_y, location, screenx, sevenex, ground
    if daily == 0:
        screen.blit(sky,(0,0))
        building(1, 150, ground)
        cityterrain()
        one_y = ground - 72
        two_y = ground - 82
    elif daily == 1:
        if location == 1:
            screen.blit(sky,(0,0))
            building(1, 150, ground)
            cityterrain()
            one_y = ground - 72
            two_y = ground - 82
        elif location == 2:
            screen.fill((0,0,0))
            buildscreen.blit(sevene, (screenx/2 - sevenex/2,screeny/2 - seveney/2))
            one_y = ground - 146
            two_y = ground - 160
            one_x = 20
            two_x = 20
        elif location == 3:
            pass
        elif location == 4:
            pass
    dailytens(gender)
    if gender == 'm':
        player_y = one_y
        one.one_animate()
    elif gender == 'f':
        player_y = two_y
        two.two_animate()
    if showcontrols:
        controls()
    pygame.display.update()

class Application(Frame):
    def __init__(self, master, option1 = ''):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widget()
        self.option1 = option1

    def create_widget(self):
        global A, B, C
        self.bttn1 = Button(self, text = A, font = ('Georgia',10), command = self.update1)
        self.bttn1.grid()
        if not(B == ''):
            self.bttn2 = Button(self, text = B, font = ('Georgia',10), command = self.update2)
            self.bttn2.grid()
        if not(C == ''):
            self.bttn3 = Button(self, text = C, font = ('Georgia',10), command = self.update3)
            self.bttn3.grid()

    def update1(self):
        global choice
        choice = 1
        self.quit()
        self.destroy()
    def update2(self):
        global choice
        choice = 2
        self.quit()
        self.destroy()
    def update3(self):
        global choice
        choice = 3
        self.quit()
        self.destroy()


def options(title = '',option1 = '', option2 = '', option3 = ''):
    global A,B,C
    win = Tk()
    win.title(title)
    win.geometry("300x300")
    A = option1
    B = option2
    C = option3
    app = Application(win)
    win.mainloop()
    return choice

def startgame():
    global choice,gender, playercharachosen
    oneNPC = NPC('One','standing_left',3.5 *screenx / 5 - 70,200 + 10)
    twoNPC = NPC('Two','standing_right',1.5 * screenx/5,200)
    oneNPC.one()
    twoNPC.two()
    pygame.display.update()
    choice = options('start game','male','female')
    if choice == 1 or choice == 2:
        if choice == 1:
            gender = 'm'
        elif choice == 2:
            gender = 'f'
        playercharachosen = True
            
# main
while True:
    userinput()
    if playercharachosen:
        redrawGameWindow(gender)
    else:
        startgame()
        
    clock.tick(60)
