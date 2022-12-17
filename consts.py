import pygame,sys
from pygame import *
from pygame.sprite import *
from pygame import Color, Surface

sys.path.append("./sprite_files")
import playersprite
import jellyclass
import studentclass
import ownerclass
import doctorclass
import richardclass
import drevclass
import darkclass
p = playersprite
jc = jellyclass
sc = studentclass
oc = ownerclass
dc = doctorclass
rc = richardclass
vc = drevclass
kc = darkclass

pygame.init()
clock = pygame.time.Clock()
screenx = 720
screeny = 450
font = pygame.font.SysFont('georgia',10)

#distinguish layers
screen = pygame.display.set_mode((screenx,screeny))
buildscreen = pygame.display.set_mode((screenx,screeny))
characterscreen = pygame.display.set_mode((screenx,screeny))
npcscreen = pygame.display.set_mode((screenx,screeny))
dialogscreen = pygame.display.set_mode((screenx,screeny))

display.set_caption("final project")
skytemp = pygame.image.load('img/sky.png').convert_alpha()
sky = pygame.transform.scale(skytemp, (720,450))

#DAY COUNT starts at day 0 and ends at day 10
dayCount = 0

#DIALOG
pokediaimg = pygame.image.load('img/dialog.png').convert_alpha()
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
wait = False
starttime = 0
endtime = 0
spacepressed = False
#CHOICES
choice = 0
A = ''
B = ''
C = ''

#PLAYER SETTINGS
#player defaults aka beginning screen
playercharachosen = False
gender = ''
playername = ''

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

#player sprites
one = p.Player("one", "m")
two = p.Player("two", "f")

#LOCATION IMAGES
#n = 1
cityunder_list = [pygame.image.load('img/Edelstein\city\city terrain (1).png'),pygame.image.load('img/Edelstein\city\city terrain (2).png'),pygame.image.load('img/Edelstein\city\city terrain (3).png'),pygame.image.load('img/Edelstein\city\city terrain (4).png'),pygame.image.load('img/Edelstein\city\city terrain (5).png'),pygame.image.load('img/Edelstein\city\city terrain (6).png')]
cityunder_rect = [pygame.Surface.get_width(cityunder_list[0]),pygame.Surface.get_width(cityunder_list[1]),pygame.Surface.get_width(cityunder_list[2]),pygame.Surface.get_width(cityunder_list[3]),pygame.Surface.get_width(cityunder_list[4]),pygame.Surface.get_width(cityunder_list[5])]
cityterrain_list = [pygame.image.load('img/Edelstein\city\city terrain (10).png').convert_alpha(), pygame.image.load('img/Edelstein\city\city terrain (11).png').convert_alpha(), pygame.image.load('img/Edelstein\city\city terrain (12).png').convert_alpha(),pygame.image.load('img/Edelstein\city\city terrain (13).png').convert_alpha()]
cityterrain_rect = [pygame.Surface.get_width(cityterrain_list[0]),pygame.Surface.get_width(cityterrain_list[1]),pygame.Surface.get_width(cityterrain_list[2]),pygame.Surface.get_width(cityterrain_list[3])]
house_list = [pygame.image.load('img/Edelstein\city\house (1).png').convert_alpha(),pygame.image.load('img/Edelstein\city\house (2).png').convert_alpha(),pygame.image.load('img/Edelstein\city\house (3).png').convert_alpha(),pygame.image.load('img/Edelstein\city\house (4).png').convert_alpha(),pygame.image.load('img/Edelstein\city\house (5).png').convert_alpha(),pygame.image.load('img/Edelstein\city\house (6).png').convert_alpha(),pygame.image.load('img/Edelstein\city\house (7).png').convert_alpha(),pygame.image.load('img/Edelstein\city\house (8).png').convert_alpha(),pygame.image.load('img/Edelstein\city\house (9).png').convert_alpha(),pygame.image.load('img/Edelstein\city\house (10).png').convert_alpha()]

#n = 2
sevene = pygame.image.load('img/7-eleven.png').convert_alpha()
sevenx = pygame.Surface.get_width(sevene)
seveny = pygame.Surface.get_height(sevene)
cashr = pygame.image.load('img/7eleven_cashregister.png').convert_alpha()
#n = 3
hostemp = pygame.image.load('img/hospital.png').convert_alpha()
hospital = pygame.transform.scale(hostemp, (1366/5 * 3,618/5 * 3))
#n = 4
diner = pygame.image.load('img/diner.png').convert_alpha()
dinerx = pygame.Surface.get_width(diner)
dinery = pygame.Surface.get_height(diner)
#IMAGE LOAD
#PLAYER IMAGES
#one's images
one_standing_left = [pygame.image.load('img/spritesheet\standingOneHanded-0.png').convert_alpha(), pygame.image.load('img/spritesheet\standingOneHanded-1.png').convert_alpha(), pygame.image.load('img/spritesheet\standingOneHanded-2.png').convert_alpha()]
one_standing_right = [pygame.transform.flip(one_standing_left[0], True, False), pygame.transform.flip(one_standing_left[1], True, False), pygame.transform.flip(one_standing_left[2], True, False)]
one_walk_left = [pygame.image.load('img/spritesheet\walkingOneHanded-0.png').convert_alpha(),pygame.image.load('img/spritesheet\walkingOneHanded-1.png').convert_alpha(),pygame.image.load('img/spritesheet\walkingOneHanded-2.png').convert_alpha(),pygame.image.load('img/spritesheet\walkingOneHanded-3.png').convert_alpha()]
one_walk_right = [pygame.transform.flip(one_walk_left[0],True,False),pygame.transform.flip(one_walk_left[1],True,False),pygame.transform.flip(one_walk_left[2],True,False),pygame.transform.flip(one_walk_left[3],True,False)]
one_jump_left = pygame.image.load('img/spritesheet\jumping-0.png').convert_alpha()
one_jump_right = pygame.transform.flip(one_jump_left,True,False)
#two's images
two_standing_left = [pygame.image.load('img/two\standingOneHanded-0.png').convert_alpha(), pygame.image.load('img/two\standingOneHanded-1.png').convert_alpha(), pygame.image.load('img/two\standingOneHanded-2.png').convert_alpha()]
two_standing_right = [pygame.transform.flip(two_standing_left[0], True, False), pygame.transform.flip(two_standing_left[1], True, False), pygame.transform.flip(two_standing_left[2], True, False)]
two_walk_left = [pygame.image.load('img/two\walkingOneHanded-0.png').convert_alpha(),pygame.image.load('img/two\walkingOneHanded-1.png').convert_alpha(),pygame.image.load('img/two\walkingOneHanded-2.png').convert_alpha(),pygame.image.load('img/two\walkingOneHanded-3.png').convert_alpha()]
two_walk_right = [pygame.transform.flip(two_walk_left[0],True,False),pygame.transform.flip(two_walk_left[1],True,False),pygame.transform.flip(two_walk_left[2],True,False),pygame.transform.flip(two_walk_left[3],True,False)]
two_jump_left = pygame.image.load('img/two\jumping-0.png').convert_alpha()
two_jump_right = pygame.transform.flip(two_jump_left,True,False)

#NPC IMAGES
#reminder: update class NPC()
#jellylemon
jelly_standing_left = [pygame.image.load('img/jellylemon\standingOneHanded-0.png').convert_alpha(), pygame.image.load('img/jellylemon\standingOneHanded-1.png').convert_alpha(), pygame.image.load('img/jellylemon\standingOneHanded-2.png').convert_alpha()]
jelly_standing_right = [pygame.transform.flip(jelly_standing_left[0], True, False), pygame.transform.flip(jelly_standing_left[1], True, False), pygame.transform.flip(jelly_standing_left[2], True, False)]
#student in 7e
student_standing_left = [pygame.image.load('img/student\standingOneHanded-0.png').convert_alpha(), pygame.image.load('img/student\standingOneHanded-1.png').convert_alpha(), pygame.image.load('img/student\standingOneHanded-2.png').convert_alpha()]
student_standing_right = [pygame.transform.flip(student_standing_left[0], True, False), pygame.transform.flip(student_standing_left[1], True, False), pygame.transform.flip(student_standing_left[2], True, False)]
#doctor
doctor_standing_left = [pygame.image.load('img/doctor\standingOneHanded-0.png').convert_alpha(), pygame.image.load('img/doctor\standingOneHanded-1.png').convert_alpha(), pygame.image.load('img/doctor\standingOneHanded-2.png').convert_alpha()]
doctor_standing_right = [pygame.transform.flip(doctor_standing_left[0], True, False), pygame.transform.flip(doctor_standing_left[1], True, False), pygame.transform.flip(doctor_standing_left[2], True, False)]
#owner
owner_standing_left = [pygame.image.load('img/owner\standingOneHanded-0.png').convert_alpha(), pygame.image.load('img/owner\standingOneHanded-1.png').convert_alpha(), pygame.image.load('img/owner\standingOneHanded-2.png').convert_alpha()]
#drev in restaurant
drev_standing_left = [pygame.image.load('img/drev\standingOneHanded-0.png').convert_alpha(), pygame.image.load('img/drev\standingOneHanded-1.png').convert_alpha(), pygame.image.load('img/drev\standingOneHanded-2.png').convert_alpha()]
drev_standing_right = [pygame.transform.flip(drev_standing_left[0], True, False), pygame.transform.flip(drev_standing_left[1], True, False), pygame.transform.flip(drev_standing_left[2], True, False)]
#dark in restaurant
dark_standing_left = [pygame.image.load('img/dark\standingOneHanded-0.png').convert_alpha(), pygame.image.load('img/dark\standingOneHanded-1.png').convert_alpha(), pygame.image.load('img/dark\standingOneHanded-2.png').convert_alpha()]
dark_standing_right = [pygame.transform.flip(dark_standing_left[0], True, False), pygame.transform.flip(dark_standing_left[1], True, False), pygame.transform.flip(dark_standing_left[2], True, False)]
#richard
rich_standing_left = [pygame.image.load('img/richard\standingOneHanded-0.png').convert_alpha(), pygame.image.load('img/richard\standingOneHanded-1.png').convert_alpha(), pygame.image.load('img/richard\standingOneHanded-2.png').convert_alpha()]
rich_standing_right = [pygame.transform.flip(rich_standing_left[0], True, False), pygame.transform.flip(rich_standing_left[1], True, False), pygame.transform.flip(rich_standing_left[2], True, False)]

#NPC INIT
#GIFT LIST for TEN
#later add all together == total
jellylist = [None] * 10
studentlist = [None] * 10
doctorlist = [None] * 10
ownerlist = [None] * 10
drevlist = [None] * 10
darklist = [None] * 10
richlist = [None] * 10

#npc locations
#jelly
jx = 500
jy = ground - 105
jelly = jc.jelly(jx,jy)
jheart = 0

#student
sx = 300
sy = ground - 145
student = sc.student(sx,sy)
sheart = 0

#doctor
dx = 600
dy = ground - 125
doctor = dc.doctor(dx,dy)
dheart = 0

#owner
ox = screenx/2 + sevenx/2 - 35
oy = screeny/2 +34
owner = oc.owner(ox,oy)
oheart = 0

#drev
vx = screenx/2 + sevenx/2 - 35
vy = ground - 82 - 70
drev = vc.drev(vx, vy)
vheart = 0

#dark
kx = screenx/2 - sevenx/2 + 100
ky = ground - 82 - 77
dark = kc.dark(kx, ky)
kheart = 0

#richard
rx = 300
ry = ground - 82
rich = rc.richard(rx,ry)
rheart = 0


def findheartCount(name):
    if name == 'Jelly':
        return jheart
    if name == 'Student':
        return sheart
    if name == 'Doctor':
        return dheart
    if name == 'Owner':
        return oheart
    if name == 'Drev':
        return vheart
    if name == 'Dark':
        return kheart
    if name == 'Richard':
        return rheart
    if name == 'Owner':
        return oheart
