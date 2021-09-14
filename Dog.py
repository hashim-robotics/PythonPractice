class dog:
    
    def __init__(self, name1, numlegs, breed1, color="black"):
        self.legs = numlegs
        self.name = name1
        self.breed = breed1
        self.tail = True
        self.color = color

    def printBreed(self, x):
        
        print("I am in printbreed func")
        
    def changeColor(self, newColor):
        self.color = newColor

  