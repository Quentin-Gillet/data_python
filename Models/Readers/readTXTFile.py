import progressbar
import sys
import re
from Utils.operations import *
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from xml.etree import ElementTree
from xml.dom import minidom

path = "/Volumes/DISQUE2/quentindev/data_python/nat2017.txt"

list_of_names_and_years = []
list_of_names = []

list_of_actual_reading_name = []

better_name_list = []

def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

def read_file():
    num_lines = sum(1 for line in open('nat2017.txt', 'r', errors='ignore'))
    actual_line = 1

    with open(path, 'r', encoding='utf8', errors='ignore') as f:
        temp_years = []

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
                        temp_years.append([split_line[2], split_line[3]])
                        #print(split_line)

                        value_to_add = split_line[3]
                        value_actual = list_of_actual_reading_name[1]

                        value_total = int(value_to_add) + int(value_actual)

                        list_of_actual_reading_name[1] = value_total
                    else:
                        better_name_list.append([split_line[0], split_line[1], temp_years])

                        temp_years[:] = []
                        list_of_names.append([list_of_actual_reading_name[0],
                                              list_of_actual_reading_name[1]])

                        list_of_actual_reading_name[:] = []
                        list_of_actual_reading_name.append(split_line[1])
                        list_of_actual_reading_name.append(split_line[3])
                        pass
                    pass
                pass
            actual_line += 1
            pass
        pass


def buildXMl():
    index = 0

    data = Element('data')
    comment = Comment('All french names usage between ???? - 2017')
    data.append(comment)

    names = SubElement(data, 'names')

    for nameList in better_name_list:
        name = SubElement(names, 'name', {'id': str(index), 'name': nameList[1]})
        gender = SubElement(name, 'gender', {'gender':  'male' if nameList[0] == '1' else 'female'})

        usages = SubElement(name, 'usages')
        for yearList in nameList[2]:
            year = SubElement(usages, 'year', {'year': yearList[0], 'uses': yearList[1]})

        index += 1
    myfile = open("test.xml", "w")
    myfile.write(str(prettify(data)))

if __name__ == '__main__':
    read_file()
    #buildXMl()
    
