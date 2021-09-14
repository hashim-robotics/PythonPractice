class robot:
    def __init__(self, NameRobot, NumWheels):
        self.name = NameRobot
        self.wheels = NumWheels

    def TurnLeft(self):
        print(self.name, "is turning left ")

    def TurnRight(self):
        print(self.name, "is turning right ")
    
    def MovingForward(self):
        print(self.name, "is moving Forward ")

    def MovingBackwards(self):
        print(self.name, "is moving Backwards ")
        
    
Robot1 = robot("ET", 4)
Robot2 = robot("Poop", 1)

def Task1():
    Robot1.MovingForward()
    Robot1.TurnRight()
def Task2():
    Robot2.MovingBackwards()
    Robot2.TurnLeft()

Task1()
Task2()
