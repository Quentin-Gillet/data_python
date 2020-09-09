from matplotlib.backend_bases import key_press_handler


def cleanDataForHistogramWithYears(data):
    yearsList = []
    usesList = []
    # Each row are being scan
    for yearId in data:
        # Remove useless row
        if data[yearId]['year'] == 'XXXX':
            continue
        # Append data into list
        yearsList.append(int(data[yearId]['year']))
        usesList.append(int(data[yearId]['uses']))

    # Return them
    return yearsList, usesList


def defineGenderName(gender):
    if gender == '1':
        return 'Masculin'
    elif gender == '2':
        return 'Féminin'
    elif gender == '3':
        return ''
    else:
        return 'ERROR'


def defineNameGender(genderName):
    if genderName == 'Masculin':
        return '1'
    elif genderName == 'Féminin':
        return '2'
    elif genderName == 'Asexuel':
        return '3'
    else:
        return 'ERROR'


def find_most_use_name():
    # TODO: remade all
    pass


def find_less_use_name():
    # TODO: remade all
    pass


# Format number if has more than 3 numbers
def formatHundredNumbers(number):
    return f"{number:,}"


# EventHandler for plot toolbar TODO: move into proper file
def onKeyPress(canvas, toolbar, event=None):
    key_press_handler(event, canvas, toolbar)


def compare_by_name():
    # TODO: remade all
    pass
