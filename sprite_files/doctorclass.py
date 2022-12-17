import pygame
import consts
import logfile
import task
import choicesmod

c = consts
l = logfile
t = task
cm = choicesmod

#DOCTOR DIALOG AND SPRITE CLASS GROUP FUNCTIONS
#CHANGE INITS.

class doctor(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.name = 'Doctor'
        self.x = x
        self.y = y
        
        #NPCSCREEN.BLIT
        self.Lstand = c.doctor_standing_left
        self.Rstand = c.doctor_standing_right
        #GIFT LIST
        self.giftlist = c.doctorlist
        #ORIENTATION
        self.orientation = 'bl'
        #DIALOGS
        # < 3 hearts
        self.two0 = ['Do you have an appointment?']
        self.two1 = ['I don\'t engage in useless chatter.']
        self.two2 = ['...What\'s this?', \
                    'Just leave it on the table.']
        # < 6 hearts
        self.five0 = ['Are you okay?']
        self.five1 = ['Make sure to treat your body well.',\
                      'Or don\'t. I get paid if you do haha.']
        self.five2 = ['It\'s alright.', \
                    'Anything else?']
        # < 9 hearts
        self.eight0 = ['Hey.']
        self.eight1 = ['How have you been feeling?',\
                       'Me? Nothing goes on much in my life.',\
                       'Have you talked to [student]? She has a couple of stories.']
        self.eight2 = ['Oh. Thanks.',\
                       'You can keep it.']
        # <= 10 hearts
        self.ten0 = ['How are you?']
        self.ten1 = ['Okay, can you give me a moment?',\
                     'I heard you were planning to stay or not.',\
                     'Have you thought about your decision yet?']
        self.ten2 = ['Thanks.',\
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
