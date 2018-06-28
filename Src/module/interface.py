from tkinter import *

class Interface():
    def __init__(self):
        self.tk = Tk()
        self.tk.title("lamp_program")
        self.tk.geometry("320x100")
        self.imgOff = PhotoImage(file='light_bulb_off.gif')
        self.imgOn = PhotoImage(file='light_bulb_on.gif')
        self.labels = []

        for k in range(0,5):
            label = Label(image=self.imgOff)
            label.pack(side=LEFT)
            self.labels.append(label)

        for k in range (0,5):
            self.bind(str(k+1), self.userInput)

        self.tk.mainloop()

    def getChoice(self):
        return self.choice

    def userInput(self,event):
        self.choice = event.char()

    def drawLamp(self, lamps):
        for label in self.labels:
            label.pack_forget()
            del label

        for lamp in lamps:
            # turn on
            if lamp.getState():
                label = Label(image=self.imgOn)
                label.pack(side=LEFT)
                self.labels.append(label)

            # turn off
            else:
                label = Label(image=self.imgOff)
                label.pack(side=LEFT)
                self.labels.append(label)

        self.tk.update()

Interface()
