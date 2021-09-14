class drone:
    def __init__(self, name, size): 
        self.Name = name
        self.Size = size
    
    def mysize(self):
        print(self.Size, "is my size")
    
    def fly(self):
        print(self.Name, "is flying")

InvisibleDrone = drone("ghonchu", "pico")
BaraDrone = drone("bhudma", "ExtraLarge")

InvisibleDrone.mysize()
InvisibleDrone.fly()


