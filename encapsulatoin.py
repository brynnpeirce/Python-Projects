

## Encapsulation assignment


class Animals:  ##created a class called Animals
    def __init__(self): ## created a function using __init__
        self._animalVar = "Baby Elephant" ## first variable

zoo = Animals() 
zoo._animalVar = "Tiger" ## Setting a new value to the variable animalVar
print(zoo._animalVar)

class Cars: # created a class called cars
    def __init__(self):
        self._carSpeedVar = 50 # setting carespeed to 50

    def getCarSpeed(self): #using get method
        print(self._carSpeedVar)

    def setCarSpeed(self, private): # using set method
        self._carSpeedVar = private


speed = Cars()
speed.getCarSpeed()
speed.setCarSpeed(0) # setting new parameters to change the car speed
speed.getCarSpeed()




