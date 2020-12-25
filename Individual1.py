# !/usr/bin/env python3
# -*- coding: utf-8 -*-

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


from datetime import datetime


class Payment:

    def __init__(self, full_name=' ', salary=0, year=0, percent=0, daysworked=0, workingdays=1):
        self.__full_name = str(full_name)
        self.__salary = int(salary)
        self.__year = int(year)
        self.__percent = float(percent)
        self.__daysworked = int(daysworked)
        self.__workingdays = int(workingdays)
        self.amount = 0
        self.heldamount = 0
        self.handamount = 0
        self.exp = 0

        self.accrued_amount()
        self.withheld_amount()
        self.handed_amount()
        self.experience()

    def accrued_amount(self):
        a = self.__salary / self.__workingdays
        b = a * self.__daysworked
        percent = self.__percent / 100 + 1
        self.amount = b * percent

    def withheld_amount(self):
        b = (self.__salary / self.__workingdays) * self.__daysworked
        self.heldamount = b * (0.13 + 0.01)

    def handed_amount(self):
        self.handamount = self.amount - self.heldamount

    def experience(self):
        self.exp = datetime.now().year - self.__year

    def __round__(self, n=0):
        return round(self.handamount)

    def __str__(self):
        return f"Experience: {self.exp} years \nCalculations: {self.amount} - {self.heldamount} = {self.handamount}"

    def __lt__(self, other):
        return self.__salary < other.__salary

    def __eq__(self, other):
        return self.__workingdays == other.__workingdays

    def __ne__(self, other):
        return self.__percent != other.__percent

    def __gt__(self, other):
        return self.__daysworked > other.__daysworked

    def __ge__(self, other):
        return self.exp >= other.exp

    def __le__(self, other):
        return self.handamount <= other.handamount

    def __truediv__(self, other):
        if self.__salary >= other.__salary:
            return self.__salary / other.__salary
        else:
            return other.__salary / self.__salary

    def __mul__(self, other):
        return self.__percent * other.__percent

    def __sub__(self, other):
        if self.__daysworked >= other.__daysworked:
            return self.__daysworked - other.__daysworked
        else:
            return other.__daysworked - self.__daysworked

    def __add__(self, other):
        return self.__workingdays + other.__workingdays


if __name__ == '__main__':
    r1 = Payment(full_name="Zhenya", salary=15000, year=2017, percent=15, daysworked=20, workingdays=24)
    r2 = Payment(full_name="Zhenya", salary=20000, year=2015, percent=10, daysworked=23, workingdays=24)

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
