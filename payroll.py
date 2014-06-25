import sys
import os.path

script, filename = sys.argv
f = open(filename, 'r')

class Person(object):

    def __init__(self, name, title, wage, hours_worked):
        self.name = name
        self.title = title
        self.wage = wage
        self.hours_worked = hours_worked

    def getName(self):
        return self.name

    def getTitle(self):
        return self.title

    def getWage(self):
        return self.wage

    def getHours(self):
        return self.hours_worked



employees = []

for line in f.readlines():
    emp_info = line.split()
    # print emp_info
    # line.split() is returning arrays for each line
    # add hours in each array for each employee
    name = emp_info[0]
    title = emp_info[1]
    wage = emp_info[2]

    hours_per_day = [float(h) for h in emp_info[4:10]]
    print hours_per_day
    hours_total = sum(hours_per_day)
    print hours_total

    new_employee = Person(name, title, wage, hours_total)
    employees.append(new_employee)

f.close()

for employee in employees:
    print employee.getName(),':'
    print '\tTitle:', employee.getTitle()
    print '\tWage:', employee.getWage()
    print '\tHours Worked:', employee.getHours()


# hw = reg_hours + ovt_hours

# def classify_hours():
#     if hw <= 40:
#         reg_hours = 40 and ovt_hours = 0
#     else:
#         ovt_hours = reg_hours - 40




# def calculate_payroll()
# for David, 40 * 25, 10 * 35 = total hours for David
# total expenses = all hours * rates for all employees