import pygame
import consts
import logfile
import task
import choicesmod

c = consts
l = logfile
t = task
cm = choicesmod

#RICHARD DIALOG AND SPRITE CLASS GROUP FUNCTIONS
#CHANGE INITS.

class richard(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.name = 'Richard'
        self.x = x
        self.y = y
        
        #NPCSCREEN.BLIT
        self.Lstand = c.rich_standing_left
        self.Rstand = c.rich_standing_right
        #GIFT LIST
        self.giftlist = c.richlist
        #ORIENTATION
        self.orientation = 'rt'
        #DIALOGS
        # < 3 hearts
        self.two0 = ['Yo.']
        self.two1 = ['You\'re new here.',\
                     'Who are you?',\
                     'Oh shoot, for real? Damn. That\'s crazy.']
        self.two2 = ['Awesome. I\'ll get you something for sure.', \
                    'Yea, next time.']
        # < 6 hearts
        self.five0 = ['What\'s up?']
        self.five1 = ['Oh, you know. Just been here and there.',\
                      'Night time is when it\'s at.',\
                      'Can\'t do nothing at all during the day.']
        self.five2 = ['Damn.', \
                      'Yea, thanks man.']
        # < 9 hearts
        self.eight0 = ['Hey!']
        self.eight1 = ['Have you met Jelly and her friend?',\
                       'I forgot her name.',\
                       'She said it once, but I couldn\'t care more.']
        self.eight2 = ['Wowwww. You\'re the best.',\
                       'If you plan on staying here, let me know. I\'ll treat you.']
        # <= 10 hearts
        self.ten0 = ['Yeahhhh.']
        self.ten1 = ['Nah, my mom\'s going to kill me.',\
                     'Just failed the exam I took last week.',\
                     'I don\'t really care about school.']
        self.ten2 = ['I owe you IF you stay.',\
                     'Thanks, man.']
        
    def stand_left(self):
        c.npcscreen.blit(self.Lstand[c.standCount//20], (self.x,self.y))
    def stand_right(self):
        c.npcscreen.blit(self.Rstand[c.standCount//20], (self.x,self.y))
    def location(self):
        if c.player_x >= self.x - 100 and c.player_x <= self.x + 100:
            return True
        else:
            return False
    def conversation(self):
        if c.ypressed:
            if c.findheartCount(self.name) < 3:
                self.twoheartlog()
            elif c.findheartCount(self.name) < 6:
                self.fiveheartlog()
            elif c.findheartCount(self.name) < 9:
                self.eightheartlog()
            else:
                self.tenheartlog()
    def twoheartlog(self):
        #sections
        section0 = len(self.two0)
        section1 = len(self.two1)
        section2 = len(self.two2)
        list0 = self.two0
        list1 = self.two1
        list2 = self.two2
        #startdialog
        if c.textCount == 0:
            c.choice = 0
        if c.textCount <= section0 and c.choice == 0:
            for i in range(section0):
                if c.textCount == i:
                    l.dialogFunc(self.orientation, self.name, list0[i])
            if c.textCount == section0:
                cm.short(self.name)
        elif c.choice == 1 and c.textCount <= section0 + section1:
            for i in range(section1):
                if c.textCount == i + section0:
                    l.dialogFunc(self.orientation, self.name, list1[i])
        elif c.choice == 2:
            if self.giftlist[c.dayCount]:
                l.dialogFunc(self.orientation, self.name, list2[1])
            else:
                l.dialogFunc(self.orientation, self.name, list2[0])
        if (c.choice == 1 and c.textCount == section0 + section1) \
           or (c.choice == 2 and c.textCount == section0 + 1):
            if c.choice == 2:
                t.tasks(self.name, c.dayCount)
            l.endlog()
    def fiveheartlog(self):
        section0 = len(self.five0)
        section1 = len(self.five1)
        section2 = len(self.five2)
        list0 = self.five0
        list1 = self.five1
        list2 = self.five2
        #startdialog
        if c.textCount == 0:
            c.choice = 0
        if c.textCount <= section0 and c.choice == 0:
            for i in range(section0):
                if c.textCount == i:
                    l.dialogFunc(self.orientation, self.name, list0[i])
            if c.textCount == section0:
                cm.short(self.name)
        elif c.choice == 1 and c.textCount <= section0 + section1:
            for i in range(section1):
                if c.textCount == i + section0:
                    l.dialogFunc(self.orientation, self.name, list1[i])
        elif c.choice == 2:
            if self.giftlist[c.dayCount]:
                l.dialogFunc(self.orientation, self.name, list2[1])
            else:
                l.dialogFunc(self.orientation, self.name, list2[0])
        if (c.choice == 1 and c.textCount == section0 + section1) \
           or (c.choice == 2 and c.textCount == section0 + 1):
            if c.choice == 2:
                t.tasks(self.name, c.dayCount)
            l.endlog()
    def eightheartlog(self):
        #sections
        section0 = len(self.eight0)
        section1 = len(self.eight1)
        section2 = len(self.eight2)
        list0 = self.eight0
        list1 = self.eight1
        list2 = self.eight2
        #startdialog
        if c.textCount == 0:
            c.choice = 0
        if c.textCount <= section0 and c.choice == 0:
            for i in range(section0):
                if c.textCount == i:
                    l.dialogFunc(self.orientation, self.name, list0[i])
            if c.textCount == section0:
                cm.short(self.name)
        elif c.choice == 1 and c.textCount <= section0 + section1:
            for i in range(section1):
                if c.textCount == i + section0:
                    l.dialogFunc(self.orientation, self.name, list1[i])
        elif c.choice == 2:
            if self.giftlist[c.dayCount]:
                l.dialogFunc(self.orientation, self.name, list2[1])
            else:
                l.dialogFunc(self.orientation, self.name, list2[0])
        if (c.choice == 1 and c.textCount == section0 + section1) \
           or (c.choice == 2 and c.textCount == section0 + 1):
            if c.choice == 2:
                t.tasks(self.name, c.dayCount)
            l.endlog()
    def tenheartlog(self):
        #sections
        section0 = len(self.eight0)
        section1 = len(self.eight1)
        section2 = len(self.eight2)
        list0 = self.eight0
        list1 = self.eight1
        list2 = self.eight2
        #startdialog
        if c.textCount == 0:
            c.choice = 0
        if c.textCount <= section0 and c.choice == 0:
            for i in range(section0):
                if c.textCount == i:
                    l.dialogFunc(self.orientation, self.name, list0[i])
            if c.textCount == section0:
                cm.short(self.name)
        elif c.choice == 1 and c.textCount <= section0 + section1:
            for i in range(section1):
                if c.textCount == i + section0:
                    l.dialogFunc(self.orientation, self.name, list1[i])
        elif c.choice == 2:
            if self.giftlist[c.dayCount]:
                l.dialogFunc(self.orientation, self.name, list2[1])
            else:
                l.dialogFunc(self.orientation, self.name, list2[0])
        if (c.choice == 1 and c.textCount == section0 + section1) \
           or (c.choice == 2 and c.textCount == section0 + 1):
            if c.choice == 2:
                t.tasks(self.name, c.dayCount)
            l.endlog()
