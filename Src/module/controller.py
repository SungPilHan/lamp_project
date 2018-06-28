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
	 