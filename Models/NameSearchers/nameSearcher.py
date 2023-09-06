from Models.NameSearchers.Searchers.compareNames import CompareNames
from Models.NameSearchers.Searchers.searchWithName import SearchWithName
from Models.Readers.readCSVFile import CSVReader


class NameSearcher:

    def __init__(self, app):
        self.app = app
        self.nameClasses = None

        self.getNamesClassData()

    def find(self, searchType, name=None, names=None, options=None):
        if searchType == 0:
            return self.searchWithName(name, options)
        elif searchType == 1:
            return self.compareNames(names, options)
        elif searchType == 2:
            return self.findMostUseName(options)
        elif searchType == 3:
            return self.findLessUseName(options)
        else:
            return 'Invalid search type'

    def getNamesClassData(self):
        csvReader = CSVReader('../../DataFiles/nat2018.csv', self.app)
        self.nameClasses = csvReader.getNameClassData()

    def searchWithName(self, name, options=None):
        searcher = SearchWithName(self.app, self.nameClasses, name, options)
        self.app.changeProgressBarValue(65)
        return searcher.find()

    def compareNames(self, names, options=None):
        searcher = CompareNames(self.app, self.nameClasses, names, options)
        return searcher.find()

    def findMostUseName(self, options=None):
        pass

    def findLessUseName(self, options=None):
        pass
