import progressbar
import sys
import re
from utils.operations import *

path = "nat2017.txt"

list_of_names_and_years = []
list_of_names = []

list_of_actual_reading_name = []


def checkInput(inputValues, arguments):
    if inputValues == '-h':
        print('This is the commands you can perform: ')
        print('— most_use_name: show graph of most use names between 1900 and 2017')
        print('— less_use_name: show graph of less use names between 1900 and 2017')
        print('— find_by_name <name> <empty|graph|year>: show usage of name (with in a graph or per years) between '
              '1900 and 2017')
        print('— compare_by_name <name1> <name2> <empty|graph>: compare two usages of names')
    elif inputValues == 'most_use_name':
        find_most_use_name(list_of_names)
    elif inputValues == 'less_use_name':
        find_less_use_name(list_of_names)
    elif inputValues == 'compare_by_name':
        if len(arguments) == 0:
            print('usage: compare_by_name <name1> <name2> <empty|graph>')
        elif len(arguments) == 1:
            print('usage: compare_by_name <name1> <name2> <empty|graph>')
        elif len(arguments) == 2:
            compare_by_name(arguments[0].upper(), arguments[1].upper(),
                            list_of_names_and_years, None)
        elif len(arguments) == 3:
            compare_by_name(arguments[0].upper(), arguments[1].upper(),
                            list_of_names_and_years, 'graph')
            pass
    elif inputValues == 'find_by_name':
        if len(arguments) == 0:
            print('usage: find_by_name <name> <empty|graph|year>')
        elif len(arguments) == 1:
            find_by_name(arguments[0].upper(), 'nothing', list_of_names)
        elif len(arguments) == 2:
            if arguments[1] == 'graph':
                find_by_name(arguments[0].upper(), 'graph', list_of_names_and_years)
            elif arguments[1].isdigit():
                find_by_name(arguments[0].upper(), arguments[1], list_of_names_and_years)
            else:
                print('usage: find_by_name <name> <empty|graph|year>')
                pass
            pass
    elif inputValues == 'exit':
        sys.exit()
    else:
        print('This is the commands you can do: ')
        print('— most_use_name: show graph of most use names between 1900 and 2017')
        print('— less_use_name: show graph of less use names between 1900 and 2017')
        print(
            '— find_by_name <name> <empty|graph|year>: show usage of name (with in a graph or per years) between 1900 '
            'and 2017')
        print(
            '— compare_by_name <name1> <name2> <empty|graph>: compare two usages of names')
        pass
    pass


def read_file():
    num_lines = sum(1 for line in open('nat2017.txt', 'r', errors='ignore'))
    actual_line = 1

    with open(path, 'r', encoding='utf8', errors='ignore') as f:
        bar = progressbar.ProgressBar(
            maxval=num_lines + 1, widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
        bar.start()

        for line in f:
            if actual_line != 1:

                split_line = line
                pattern = re.compile(r'\s+')
                split_line = re.sub(pattern, ';', split_line)

                split_line = split_line.split(';', 3)
                split_line[3] = split_line[3].replace(';', '')

                list_of_names_and_years.append(split_line)

                if len(list_of_actual_reading_name) == 0:
                    list_of_actual_reading_name.append(split_line[1])
                    list_of_actual_reading_name.append(split_line[3])
                    pass

                if split_line[1] != '_PRENOMS_RARES':

                    if split_line[1] == list_of_actual_reading_name[0]:

                        value_to_add = split_line[3]
                        value_actual = list_of_actual_reading_name[1]

                        value_total = int(value_to_add) + int(value_actual)

                        list_of_actual_reading_name[1] = value_total
                    else:
                        list_of_names.append([list_of_actual_reading_name[0],
                                              list_of_actual_reading_name[1]])

                        list_of_actual_reading_name[:] = []
                        list_of_actual_reading_name.append(split_line[1])
                        list_of_actual_reading_name.append(split_line[3])
                        pass
                    pass
                pass
            actual_line += 1
            bar.update(actual_line)
            pass
        bar.finish()
        pass


if __name__ == '__main__':
    read_file()
    while True:
        inputValue = input('Chose an action (-h for help)\n')
        inputValue = inputValue.split(' ')

        inputValue = list(filter(None, inputValue))
        inputValue = list(filter(bool, inputValue))

        args = inputValue[1:]

        checkInput(inputValue[0], args)
        pass
