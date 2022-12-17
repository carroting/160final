import pygame
import consts
import logfile
import task
import choicesmod

c = consts
l = logfile
t = task
cm = choicesmod

#STUDENT DIALOG AND SPRITE CLASS GROUP FUNCTIONS
#CHANGE INITS.

class student(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.name = 'Student'
        self.x = x
        self.y = y
        
        #NPCSCREEN.BLIT
        self.Lstand = c.student_standing_left
        self.Rstand = c.student_standing_right
        #GIFT LIST
        self.giftlist = c.studentlist
        #ORIENTATION
        self.orientation = 'bl'
        #DIALOGS
        # < 3 hearts
        self.two0 = ['Buzz off!']
        self.two1 = ['Go away!']
        self.two2 = ['...', \
                    '...What???']
        # < 6 hearts
        self.five0 = ['...']
        self.five1 = ['Leave me alone.']
        self.five2 = ['I don\'t get you.', \
                    '...']
        # < 9 hearts
        self.eight0 = ['What?']
        self.eight1 = ['I fed the cat at the restaurant.',\
                       'I have a photo. Look.']
        self.eight2 = ['Um, cool, I guess.',\
                       'I\'m okay.']
        # <= 10 hearts
        self.ten0 = ['Oh, hi.']
        self.ten1 = ['The [doctor] told me I\'m clear for now.',\
                     'Will you be staying in Perihelion?',\
                     'Hang out with me and the others if you\'re planning to stay.']
        self.ten2 = ['Thanks, mate.',\
                     'I said, thank you.']
        
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
