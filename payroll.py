# payroll program 

class Person(object):

    def __init__(self, name, title, wage):
        self.name = name
        self.title = title
        self.wage = wage

    def getName(self):
        return self.name

    def getTitle(self):
        return self.title

    def getWage(self):
        return self.wage 

annie = Person("annie", "programmer", "40")
david = Person("david", "teacher", "25")
tom = Person("tom", "programmer", "43")
ryan = Person("ryan", "teacher", "55")
deats = Person("deats", "programmer", "40")

print annie.getName()
print david.getTitle()
print ryan.getWage()    
