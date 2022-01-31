from package import addition
from package import subtraction 
from package import multiplication
from package import division

class Calculator:
    def __init__(self, first_number, second_number, command):
        self.first_number = first_number
        self.second_number = second_number
        self.command = command
    
    def calc(self):
        if self.command == "+":
            return addition()
        elif self.command == "-":
            return subtraction()
        elif self.command == "*":
            return multiplication()
        elif self.command == "/":
            return division
        else:
            return "Not valid operation!"


