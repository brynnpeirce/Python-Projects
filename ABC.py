
## Abstraction assignment 

from abc import ABC, abstractmethod

class car(ABC):
    def driving(self, mph):
        print("Your current speed: ",mph)

#This functin is telling us to pass in an argument
    @abstractmethod
    def speed(self, mph):
        pass

class police(car):
#defined how to implement the payment function from its parent paySlip class
    def speed(self, mph):
         print("You were caught going {} in a 10mph area.\nYou have been pulled over by the police".format(mph))


busted = police()
busted.driving("57")
busted.speed("57")
