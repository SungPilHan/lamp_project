class controller(object):
	def __init__(self):
		self.interface = Interface()
	
	def control(self, lamps):
		choice = interface.getChoice()
		lamp = lamps[int(choice) - 1]
		
		if lamp.getState():
			lamp.turnOff()
		else:
			lamp.turnOn()

		interface.drawLamp(lamp)