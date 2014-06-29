import sys
import os.path

script, filename = sys.argv
f = open(filename, 'r')

class Person(object):

    def __init__(self, name, title, wage, weekday_hours, weekend_hours):
        self.name = name
        self.title = title
        self.wage = wage
        self.weekday_hours = weekday_hours
        self.weekend_hours = weekend_hours

    def getName(self):
        return self.name

    def getTitle(self):
        return self.title

    def getWage(self):
        return self.wage

    def getWeekdayHours(self):
        return self.weekday_hours

    def getWeekendHours(self):
        return self.weekend_hours

employees = []

for line in f.readlines():
    emp_info = line.split()
    # print emp_info
    # line.split() is returning arrays for each line
    # add hours in each array for each employee
    name = emp_info[0]
    title = emp_info[1]
    wage = emp_info[2]

    weekday_hours = [float(h) for h in emp_info[4:9]]
    print weekday_hours
    weekend_hours = [float(h) for h in emp_info[9:]]
    print weekend_hours
    hours_total = sum(weekday_hours) + sum(weekend_hours)
    print hours_total

    new_employee = Person(name, title, float(wage), sum(weekday_hours), sum(weekend_hours))
    employees.append(new_employee)

f.close()

for employee in employees:
    print employee.getName(),':'
    print '\tTitle:', employee.getTitle()
    print '\tWage:', employee.getWage()
    print '\tWeekday Hours:', employee.getWeekdayHours()
    print '\tWeekend Hours:', employee.getWeekendHours()

expenses_by_profession = {'Programmer': 0, 'Teacher': 0}

def indiv_payroll():
    print "===Payroll==="
    for employee in employees:
        weekday_reghours = employee.getWeekdayHours()
        weekday_ovthours = 0
        if weekday_reghours > 40:
            weekday_ovthours = (weekday_reghours - 40)
            weekday_reghours = 40
        weekday_pay = weekday_reghours * employee.getWage()
        weekend_pay = employee.getWeekendHours() * (employee.getWage() * 1.5)
        ovt_pay = weekday_ovthours * (employee.getWage() * 1.5)
        total_pay = weekday_pay + weekend_pay + ovt_pay
        print employee.getName(), ": $", total_pay

        expenses_by_profession[employee.getTitle()] += total_pay

def expense_breakdown():
    print "===Expense Breakdown==="
    total_emp_pay = sum(expenses_by_profession.values())
    for emp in expenses_by_profession:
        print emp, ": $", expenses_by_profession[emp], ",", (expenses_by_profession[emp] / total_emp_pay * 100), "%"
    print "Total: $", total_emp_pay

def slackers():
    print "==Slacker Warning!==="
    for employee in employees:
        total_hours = employee.getWeekdayHours() + employee.getWeekendHours()
        if total_hours < 20:
            print employee.getName(), "only worked for", total_hours, "hours!"

if __name__ == '__main__':
    indiv_payroll()
    expense_breakdown()
    slackers()