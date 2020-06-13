# Module 8
#   Programming Assignment 11
#     Prob-1.py

class Car:
    # constructor
    def __init__(self, make, model, year):
        self._make = make
        self._model = model
        self._year = year

    def setMake(self, make):
        self._make = make

    def getMake(self):
        return self._make

    def setModel(self, model):
        self._model = model
    
    def getModel(self):
        return self._model
    
    def setYear(self, year):
        self._year = year

    def getYear(self):
        return self._year

def TestCar():
    carLot = []
    carLot.append(Car("minubishi", "achord", "2003"))
    carLot.append(Car("farfella", "camora", "2017"))
    carLot.append(Car("fiorde", "automoten", "2010"))
    carLot.append(Car("kyota", "samazo", "2013"))
    carLot.append(Car("landza", "arratil", "2006"))
    
    i = 1
    for car in carLot:
        print("car #",i)
        print("Make:", car.getMake())
        print("Model:", car.getModel())
        print("Year:", car.getYear(), "\n")
        i = i + 1
    
    i = 1
    for car in carLot:
        Make = input("Enter a car make: ")
        Model = input("Enter a car model: ")
        Year = input("Enter the year of the car: ")
        car.setMake(Make)
        car.setModel(Model)
        car.setYear(Year)

    i = 1
    for car in carLot:
        print("car #",i)
        print("Make:", car.getMake())
        print("Model:", car.getModel())
        print("Year:", car.getYear(), "\n")
        i = i + 1

if __name__ == "__main__":
    TestCar()
