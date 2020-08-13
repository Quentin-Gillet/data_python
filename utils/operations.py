from utils.colorama import bcolors
from utils.matplotlib import *


def find_most_use_name(list_where_find):
    temp_list_of_names = []
    for row in list_where_find:
        temp_list_of_names.append([str(row[0]), str(row[1])])
        pass

    list_where_find = temp_list_of_names
    list_where_find.sort(key=lambda x: int(x[1]))
    list_where_find = list_where_find[-10:]
    all_names = []
    all_numbers = []

    for row in list_where_find:
        all_names.append(row[0])
        all_numbers.append(round(int(row[1])))
        pass

    create_diagramme(all_names, all_numbers, 'Diagramme des noms les plus utilisés')


def find_less_use_name(list_where_find):
    temp_list_of_names = []
    for row in list_where_find:
        temp_list_of_names.append([str(row[0]), str(row[1])])
        pass

    list_where_find = temp_list_of_names
    list_where_find.sort(key=lambda x: int(x[1]))
    list_where_find = list_where_find[:10]
    all_names = []
    all_numbers = []

    for row in list_where_find:
        all_names.append(row[0])
        all_numbers.append(row[1])
        pass

    create_diagramme(all_names, all_numbers, 'Diagramme des noms les moins utilisés')


def find_by_name(name, option, list_where_find):
    if option == 'nothing':
        total = 0

        for x in list_where_find:
            find = name in x
            if find:
                total += int(x[1])
                pass
            pass

        if total != 0:
            print(bcolors.BLUE + name + bcolors.END + " has been used " +
                  bcolors.GREEN + str(total) + bcolors.END + " times in 117 years")
        else:
            print(bcolors.RED + name + " is never use in 117 years" + bcolors.END)
        pass

    elif option.isdigit():
        total = 0

        for x in list_where_find:
            find = name in x
            if find:
                if x[2] == option:
                    total += int(x[3])
                    pass
                pass
            pass

        if total != 0:
            print(bcolors.BLUE + name + bcolors.END + " has been used " +
                  bcolors.GREEN + str(total) + bcolors.END + " times in " + option)
        else:
            print(bcolors.RED + name + " is never use in " + option + bcolors.END)
        pass
    elif option == 'graph':

        total_by_years = []
        years = []

        for x in list_where_find:
            find = name in x
            if find and x[2] != 'XXXX':
                years.append(x[2])
                total_by_years.append(int(x[3]))
                pass
            pass

        years.sort()

        create_diagramme(years, total_by_years, "Diagramme de l'historique du prénom " + name)
        pass
    elif option == 'return_name_number':
        total = 0

        for x in list_where_find:
            find = name in x
            if find:
                total += int(x[3])
                pass
            pass

        return total if total != 0 else None
        pass
    pass


def compare_by_name(name1, name2, list_where_find, option):
    if option is None:
        name1_exist = True
        name2_exist = True

        names = [find_by_name(name1, 'return_name_number', list_where_find), find_by_name(
            name2, 'return_name_number', list_where_find)]

        if names[0] is None:
            print(bcolors.RED + 'The name ' + name1 +
                  ' is not exist' + bcolors.END)
            name1_exist = False
            pass
        if names[1] is None:
            print(bcolors.RED + 'The name ' + name2 +
                  ' is not exist' + bcolors.END)
            name2_exist = False
            pass
        if name1_exist and name2_exist:
            print(bcolors.GREEN + str(names[0]) + bcolors.END + ' uses for ' + bcolors.BLUE + name1 + bcolors.END +
                  ' and ' + bcolors.YELLOW + str(
                names[1]) + bcolors.END + ' uses for ' + bcolors.RED + name2 + bcolors.END)
            pass
    elif option == 'graph':

        name1_exist = True
        name2_exist = True

        total_by_years_1 = []
        years_1 = []

        total_by_years_2 = []
        years_2 = []

        for x in list_where_find:
            find = name1 in x
            if find and x[2] != 'XXXX':
                years_1.append(x[2])
                total_by_years_1.append(int(x[3]))
                pass
            pass

        for x in list_where_find:
            find = name2 in x
            if find and x[2] != 'XXXX':
                years_2.append(x[2])
                total_by_years_2.append(int(x[3]))
                pass
            pass

        if total_by_years_1 and years_1 is None:
            print(bcolors.RED + 'The name ' + name1 +
                  ' is not exist' + bcolors.END)
            name1_exist = False
            pass
        if total_by_years_2 and years_2 is None:
            print(bcolors.RED + 'The name ' + name2 +
                  ' is not exist' + bcolors.END)
            name2_exist = False
            pass
        if name1_exist and name2_exist:
            years_1.sort()
            years_2.sort()

            create_double_diagramme(years_1, years_2, total_by_years_1, total_by_years_2, name1, name2,
                                    'Diagramme de comparaison de ' + name1 + ' et ' + name2)
            pass
        pass
    pass
