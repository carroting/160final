import pygame,sys
import consts
import logfile

c = consts
l = logfile


def shortendaily():
    c.location = 1
    c.text_box = True
    if c.textCount == 0:
        l.dialogFunc('center', 'Start of ', 'Day ' + str(c.dayCount + 1))
    elif c.textCount == 1:
        l.dialogFunc('rt',c.playername,'A shining day indeed. Whatever will I do.')
    elif c.textCount == 2:
        l.dialogFunc('rt',c.playername,'How are my relationships with others?')
    elif c.textCount == 3:
        l.dialogFunc('rt',c.playername,'Is Perihelion a great place for me to live in?')
    else:
        c.textCount = 0
        c.daily = 1
        c.text_box = False

def dailytens():
    """for the tens of the game"""
    if c.dayCount < 10:
        if c.daily == 0:
            shortendaily()
            if c.ypressed:
                c.ypressed = False
        if c.daily == 1:
            if c.location == 1:
                if c.jelly.location() or c.rich.location():
                    c.distance = True
                    if c.jelly.location():
                        c.jelly.conversation()
                    elif c.rich.location():
                        c.rich.conversation()
                else:
                    c.distance = False
                    
            if c.location == 2:
                if c.owner.location() or (c.student.location() and (c.dayCount != 2 or c.dayCount != 5 or c.dayCount != 7)):
                    c.distance = True
                    if c.owner.location():
                        c.owner.conversation()
                else:
                    c.distance = False

                if c.dayCount != 2 or c.dayCount != 5 or c.dayCount != 7:
                    if c.student.location():
                        c.student.conversation()
                
            if c.location == 3:
                if c.doctor.location() or (c.student.location() and (c.dayCount == 2 or c.dayCount == 5 or c.dayCount == 7)):
                    c.distance = True
                    if c.student.location():
                        c.student.conversation()
                    if c.doctor.location():
                        c.doctor.conversation()
                else:
                    c.distance = False

            if c.location == 4:
                if c.drev.location() or c.dark.location():
                    c.distance = True
                    if c.drev.location():
                        c.drev.conversation()
                    elif c.dark.location():
                        c.dark.conversation()
                else:
                    c.distance = False
                
    else:
        c.text_box = True
        if c.textCount == 0:
            l.dialogFunc('center', '', 'TEN DAYS HAVE PASSED.')
        elif c.textCount == 1:
            if c.sheart + c.jheart + c.dheart + c.oheart >= 45:
                l.dialogFunc('center', '','I made a couple friends here and there and I definitely want to learn more about them.', 'I want to stay here.')
            elif c.sheart >= 8 and c.jheart >= 8 and c.dheart >= 8 and c.oheart >= 8:
                l.dialogFunc('center', '','Perihelion seems to be a great place to stay in.', 'Everyone here is great, and I made a feel friends.')
            else:
                l.dialogFunc('center', '','I\'m going back home.', 'What a bore.')
        else:
            pygame.quit()
            sys.exit()
