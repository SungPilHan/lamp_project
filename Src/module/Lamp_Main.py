from tkinter import *

class Interface():
    def __init__(self):
        self.tk = Tk()
        self.tk.title("lamp_program")
        self.tk.geometry("330x100")
        self.imgOff = PhotoImage(file='light_bulb_off.gif')
        self.imgOn = PhotoImage(file='light_bulb_on.gif')
        self.labels = []
        self.choice=None

        for k in range(0,5):
            label = Label(image=self.imgOff)
            label.pack(side=LEFT)
            self.labels.append(label)

        for k in range (0,5):
            self.tk.bind(str(k+1), self.userInput)

    def getChoice(self):
        return self.choice

    def resetChoice(self):
        self.choice = None

    def userInput(self,event):
        self.choice = event.char
        print(self.choice)

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

class Lamp:
    def __init__(self):
        self.state = False

    def getState(self):
        return self.state

    def turnOn(self):
        self.state = True

    def turnOff(self):
        self.state = False

class controller(object):
	def __init__(self, interface, lamps):
		self.interface = interface
		self.lamps = lamps

	def control(self):
		try:
			choice = self.interface.getChoice()
			self.interface.resetChoice()
			lamp = self.lamps[int(choice) - 1]
		
			if lamp.getState():
				lamp.turnOff()
			else:
				lamp.turnOn()

		except:
			pass

		self.interface.drawLamp(self.lamps)

if __name__=="__main__":
    lamps = []
    for i in range(0,5):
        lamp = Lamp()
        lamps.append(lamp)

    inter = Interface()
    con = controller(inter, lamps)
    while True:
        con.control()
