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

from datetime import datetime


class Payment:

    def __init__(self, fullName=' ', salary=0, year=0, percent=0, daysWorked=0, workingDays=1):
        self.__fullName = str(fullName)
        self.__salary = int(salary)
        self.__year = int(year)
        self.__percent = float(percent)
        self.__daysWorked = int(daysWorked)
        self.__workingDays = int(workingDays)
        self.amount = 0
        self.heldAmount = 0
        self.handAmount = 0
        self.exp = 0

        self.accruedAmount()
        self.withheldAmount()
        self.handedAmount()
        self.experience()

    def accruedAmount(self):
        a = self.__salary / self.__workingDays
        b = a * self.__daysWorked
        percent = self.__percent / 100 + 1
        self.amount = b * percent

    def withheldAmount(self):
        b = (self.__salary / self.__workingDays) * self.__daysWorked
        self.heldAmount = b * (0.13 + 0.01)

    def handedAmount(self):
        self.handAmount = self.amount - self.heldAmount

    def experience(self):
        self.exp = datetime.now().year - self.__year

    def __round__(self, n=0):
        return round(self.handAmount)

    def __str__(self):
        return f"Experience: {self.exp} years \nCalculations: {self.amount} - {self.heldAmount} = {self.handAmount}"

    def __lt__(self, other):
        return self.__salary < other.__salary

    def __eq__(self, other):
        return self.__workingDays == other.__workingDays

    def __ne__(self, other):
        return self.__percent != other.__percent

    def __gt__(self, other):
        return self.__daysWorked > other.__daysWorked

    def __ge__(self, other):
        return self.exp >= other.exp

    def __le__(self, other):
        return self.handAmount <= other.handAmount

    def __truediv__(self, other):
        if self.__salary >= other.__salary:
            return self.__salary / other.__salary
        else:
            return other.__salary / self.__salary

    def __mul__(self, other):
        return self.__percent * other.__percent

    def __sub__(self, other):
        if self.__daysWorked >= other.__daysWorked:
            return self.__daysWorked - other.__daysWorked
        else:
            return other.__daysWorked - self.__daysWorked

    def __add__(self, other):
        return self.__workingDays + other.__workingDays


if __name__ == '__main__':
    r1 = Payment(fullName="Zhenya", salary=15000, year=2017, percent=15, daysWorked=20, workingDays=24)
    r2 = Payment(fullName="Zhenya", salary=20000, year=2015, percent=10, daysWorked=23, workingDays=24)

    print(f"{r1}")
    print(f"Сalculated amount handed out: {round(r1)}\n")

    print(f"salary1 < salary2: {r1 < r2}")
    print(f"workingDays1 > workingDays2: {r1 > r2}")
    print(f"percent1 != percent2: {r1 != r2}")
    print(f"daysWorked1 == daysWorked2: {r1 == r2}")
    print(f"Experience1 >= Experience2: {r1 >= r2}")
    print(f"handAmount1 <= handAmount2: {r1 <= r2}\n")

    print(f"Difference in salary(division): {r1 / r2}")
    print(f"multiplication of percent: {r1 * r2}")
    print(f"Addition of working days: {r1 + r2}")
    print(f"Difference in daysWorked(subtraction): {r1 - r2}")
