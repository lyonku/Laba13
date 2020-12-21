#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from dataclasses import dataclass, field
import sys
from typing import List
import xml.etree.ElementTree as ET


#   Выполнить индивидуальное задание 2 лабораторной работы 9, использовав классы данных, а
#   также загрузку и сохранение данных в формат XML.


@dataclass(frozen=True)
class train:
    name: str
    num: int
    time: str


@dataclass
class Staff:
    trains: List[train] = field(default_factory=lambda: [])

    def add(self, name, num, time):
        self.trains.append(
            train(
                name=name,
                num=num,
                time=time
            )
        )
        self.trains.sort(key=lambda train: train.name)

    def __str__(self):
        # Заголовок таблицы.
        table = []
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 17
        )
        table.append(line)
        table.append(
            '| {:^4} | {:^30} | {:^20} | {:^17} |'.format(
                "№",
                "Пункт назначения",
                "Номер поезда",
                "Время отправления"
            )
        )
        table.append(line)

        # Вывести данные о всех сотрудниках.
        for idx, train in enumerate(trains, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:>17} |'.format(
                    idx,
                    train.get('name', ''),
                    train.get('num', ''),
                    train.get('time', 0)
                )
            )
        table.append(line)

        return '\n'.join(table)

    def select(self):
        parts = command.split(' ', maxsplit=2)

        number = int(parts[1])

        count = 0
        for train in trains:
            if train.get('num') == number:
                count += 1
                print('Номер поезда:', train.get('num', ''))
                print('Пункт назначения:', train.get('name', ''))
                print('Время отправления:', train.get('time', ''))

        if count == 0:
            print("Таких поездов нет!")

    def load(self, filename):
        with open(filename, 'r', encoding='utf8') as fin:
            xml = fin.read()
        parser = ET.XMLParser(encoding="utf8")
        tree = ET.fromstring(xml, parser=parser)
        self.trains = []

        for train_element in tree:
            name, num, time = None, None, None

            for element in train_element:
                if element.tag == 'name':
                    name = element.text
                elif element.tag == 'num':
                    num = element.text
                elif element.tag == 'time':
                    time = list(element.text)

                if name is not None and num is not None \
                        and time is not None:
                    self.trains.append(
                        train(
                            name=name,
                            num=time,
                            time=time
                        )
                    )

    def save(self, filename):
        root = ET.Element('trains')
        for train in self.trains:
            train_element = ET.Element('train')

            name_element = ET.SubElement(train_element, 'name')
            name_element.text = train.name

            num_element = ET.SubElement(train_element, 'num')
            num_element.text = train.num

            time_element = ET.SubElement(train_element, 'time')
            time_element.text = str(train.time)

            root.append(train_element)

        tree = ET.ElementTree(root)
        with open(filename, 'wb') as fout:
            tree.write(fout, encoding='utf8', xml_declaration=True)


if __name__ == '__main__':
    trains = ()
    staff = Staff()
    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()
        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break
        elif command == 'add':
            # Запросить данные о работнике.
            name = input("Название пункта назначения: ")
            num = int(input("Номер поезда: "))
            time = input("Время отправления: ")

            train = {
                'name': name,
                'num': num,
                'time': time,
            }

            staff.add(name, num, time)

        elif command == 'list':
            print(staff)

        elif command.startswith('select '):
            parts = command.split(' ', maxsplit=2)

            number = int(parts[1])

            count = 0

            for train in trains:
                if train.get('num') == number:
                    count += 1
                    print('Номер поезда:', train.get('num', ''))
                    print('Пункт назначения:', train.get('name', ''))
                    print('Время отправления:', train.get('time', ''))

            if count == 0:
                print("Таких поездов нет!")

        elif command.startswith('load '):
            # Разбить команду на части для выделения имени файла.
            parts = command.split(' ', maxsplit=1)
            staff.load(parts[1])

        elif command.startswith('save '):
            # Разбить команду на части для выделения имени файла.
            parts = command.split(' ', maxsplit=1)
            staff.save(parts[1])

        elif command == 'help':

            print("Список команд:\n")
            print("add - добавить поезд;")
            print("list - вывести список поездов;")
            print("select <номер поезда> - запросить информацию о выбранном поезде;")
            print("help - отобразить справку;")
            print("load <имя файла> - загрузить данные из файла;")
            print("save <имя файла> - сохранить данные в файл;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
