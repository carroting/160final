import pygame
import consts
import logfile
import task
import choicesmod

c = consts
l = logfile
t = task
cm = choicesmod

#JELLY DIALOG AND SPRITE CLASS GROUP FUNCTIONS


class jelly(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.name = 'Jelly'
        self.x = x
        self.y = y
        
        #NPCSCREEN.BLIT
        self.Lstand = c.jelly_standing_left
        self.Rstand = c.jelly_standing_right
        #GIFT LIST
        self.giftlist = c.studentlist
        #ORIENTATION
        self.orientation = 'rt'
        #DIALOGS
        # < 3 hearts
        self.two0 = ['Hello!', \
                    'You have an interesting aura around you.']
        self.two1 = ['Today is a nice day, isn\'t it?', \
                     'It\'s a perfect day to not do anything at all.']
        self.two2 = ['Aw, how sweet.', \
                    'That\'s a bit too much.']
        # < 6 hearts
        self.five0 = ['How are you doing today?']
        self.five1 = ['How has Perihelion been treating you?', \
                    'If you go to the grocery, you might run into [Student].']
        self.five2 = ['You\'re so nice!', \
                    'Well, I\'d love to accept that...']
        # < 9 hearts
        self.eight0 = ['!!!! :(']
        self.eight1 = ['I can\'t believe it!',\
                      'I just bombed my finals! My mom\'s going to kill me (╯︵╰,)']
        self.eight2 = ['Thanks for cheering me up!!',\
                       'You don\'t have to give me so many, you know...!']
        # <= 10 hearts
        self.ten0 = ['What\'s up!']
        self.ten1 = ['Richard and I were just eating at the Diner.',\
                     'We saw that guy, Drev, slip up and create a huge mess! It was so funny!',\
                     'You should totally try their Coriander and Pork Jook!']
        self.ten2 = ['I\'m so lucky to be your friend <3',\
                     'A better gift would be staying here in Perihelion with me!']
        
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

