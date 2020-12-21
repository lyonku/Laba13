# Создать класс Payment (зарплата). В классе должны быть представлены поля: фамилия-
# имя-отчество, оклад, год поступления на работу, процент надбавки, подоходный налог,
# количество отработанных дней в месяце, количество рабочих дней в месяце, начисленная и
# удержанная суммы. Реализовать методы:
# вычисления начисленной суммы,
# вычисления удержанной суммы,
# вычисления суммы, выдаваемой на руки,
# вычисления стажа. Стаж вычисляется как полное количество лет, прошедших от года
# поступления на работу, до текущего года.
# Начисления представляют собой сумму, начисленную за отработанные дни, и
# надбавки, то есть доли от первой суммы. Удержания представляют собой отчисления в
# пенсионный фонд (1% от начисленной суммы) и подоходный налог. Подоходный налог
# составляет 13% от начисленной суммы без отчислений в пенсионный фонд.

# !/usr/bin/env python3
# -*- coding: utf-8 -*-

class Payment:

    def __init__(self, fullName=' ', salary=0, year=0, percent=0, daysWorked=0,
                 workingDays=1):
        self.fullName = str(fullName)
        self.salary = int(salary)
        self.year = int(year)
        self.percent = float(percent)
        self.daysWorked = int(daysWorked)
        self.workingDays = int(workingDays)
        self.amount = 0
        self.heldAmount = 0
        self.handAmount = 0
        self.exp = 0

        self.accruedAmount()
        self.withheldAmount()
        self.handedAmount()
        self.experience()

    def read(self):
        fullName = input('Enter your full name: ')
        salary = input('Enter salary: ')
        year = input('Enter year of joining: ')
        percent = input('Enter percentage of premium: ')
        daysWorked = input('Enter number of days worked in a month: ')
        workingDays = input('Enter number of working days in a month: ')

        self.fullName = fullName
        self.salary = int(salary)
        self.year = int(year)
        self.percent = float(percent)
        self.daysWorked = int(daysWorked)
        self.workingDays = int(workingDays)

        self.accruedAmount()
        self.withheldAmount()
        self.handedAmount()
        self.experience()

    def display(self):
        print(f"Accrued amount: {round(self.amount)}")
        print(f"Withholding amount: {round(self.heldAmount)}")
        print(f"Сalculated amount handed out: {round(self.handAmount)}")
        print(f"Experience: {self.exp} year(s)")

    def __str__(self):
        return "Amount:{}".format(self.amount)

    def accruedAmount(self):
        a = self.salary / self.workingDays
        b = a * self.daysWorked
        percent = self.percent / 100 + 1
        self.amount = b * percent

    def withheldAmount(self):
        b = (self.salary / self.workingDays) * self.daysWorked
        self.heldAmount = b * (0.13 + 0.01)

    def handedAmount(self):
        self.handAmount = self.amount - self.heldAmount

    def experience(self):
        self.exp = 2020 - self.year

    def __add__(self, other):
        return Payment(self.fullName, self.salary + other.salary, self.year,
                       self.percent + other.percent, self.daysWorked + other.daysWorked,
                       self.workingDays)

    def __lt__(self, other):
        return self.handAmount < other.handAmount


if __name__ == '__main__':
    r1 = Payment()
    r1.read()
    r1.display()
    print(r1)

    r2 = Payment()
    r2.read()
    r2.display()

    print(r1 < r2)

    r3 = r1 + r2
    r3.display()
