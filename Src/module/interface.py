from Tkinter import *

class Interface():

    def __init__(self):
        self.tk = Tk()
        self.tk.title("lamp_program")
        self.tk.geometry("640x400+100+100")
        self.tk.resizable(False, False)
        self.imgOff = PhotoImage(file='light_bulb_off.gif')
        self.imgOn = PhotoImage(file='light_bulb_on.gif')

        for k in range (0,5):
            self.bind(k+1, self.userInput)



    def getChoice(self):
        return self.choice

    def userInput(self,event):
        self.choice = event.getchar()

    def drawLamp(self, lamps):

        for lamp in lamps:
            # turn on
            if lamp.getState():
                label = Label(image=self.imgOn)
                label.image = self.imgOn
                label.pack(side=LEFT, padx=10, pady=10)

            # turn off
            else:
                label = Label(image=self.imgOff)
                label.image = self.imgOff
                label.pack(side=LEFT, padx=10, pady=10)

        self.tk.update()

