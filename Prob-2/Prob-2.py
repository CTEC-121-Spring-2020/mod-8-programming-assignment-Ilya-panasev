# Module 8
#   Programming Assignment 11
#     Prob-2.py

class Student:
    # constructor
    # Whenever I go up to Gaiser hall to register for classes or go to an advisor
    # they usually ask me what my name is first, then ask me for my student ID
    # in order to pull up the rest of my information. Major and GPA are usually 
    # listed under the information they pull up.
    def __init__(self, name, IDnumber):
        self._name = name
        self._IDnumber = IDnumber
        self._major = ""
        self._GPA = 0.0

    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name

    def setIDnumber(self, IDnumber):
        self._IDnumber = IDnumber

    def getIDnumber(self):
        return self._IDnumber
    
    def setMajor(self, major):
        self._major = major

    def getMajor(self):
        return self._major

    def setGPA(self, GPA):
        self._GPA = GPA
    
    def getGPA(self):
        return self._GPA

def TestStudent():
    stuList = []
    stuList.append(Student("Joe Bella", "9933"))
    stuList.append(Student("Tucker Blank", "3399"))
    stuList.append(Student("Gayle Ujifusa", "1011"))
    stuList.append(Student("Edna Anker", "9875"))
    
    stuList[0].setMajor("Web Development")
    stuList[1].setMajor("Nursing")
    stuList[2].setMajor("Baking")
    stuList[3].setMajor("Medical Office")

    stuList[0].setGPA(3.8)
    stuList[1].setGPA(3.0)
    stuList[2].setGPA(2.8)
    stuList[3].setGPA(3.0)

    for element in stuList:
        print("Name:", element.getName())
        print("ID Number:", element.getIDnumber())
        print("Major:", element.getMajor())
        print("GPA:", element.getGPA())
        print()
        

if __name__ == "__main__":
    TestStudent()