class controller(object):
	def __init__(self, lamps):
		self.lamps = lamps
		self.interface = Interface()
	def control(self):
		while(True):
			choice = interface.getChoice()
			lamp = lamps[int(choice) - 1]
			
			if lamp.getState():
				lamp.turnOff()
			else:
				lamp.turnOn()

			interface.drawLamp()