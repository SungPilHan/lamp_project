class Lamp:
    def __init__(self):
        self.state = False

    def getState(self):
        return self.state

    def turnOn(self):
        self.state = True

    def turnOff(self):
        self.state = False
