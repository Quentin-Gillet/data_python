# import cProfile
# cProfile.run('getNamesData()')

# yearsList, usesList = cleanDataForHistogramWithYears(nameData.getYearsData()["1"])
#
# Plot(yearsList, usesList, 'Tige', None).draw()
from Models.NameSearchers.nameSearcher import NameSearcher

nameSearcher = NameSearcher(None)
nameClass = nameSearcher.find(1, None, ['QUENTIN', 'ARTHUR'])
