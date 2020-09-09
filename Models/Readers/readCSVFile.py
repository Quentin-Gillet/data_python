import csv
from Models.Readers.reader import Reader
from Models.name import Name


class CSVReader(Reader):

    def __init__(self, file, app=None):
        super().__init__(file)
        self.app = app
        self.progressBar = None
        self.progressBarPart = 6364
        self.linesCounted = 0
        self.nameClasses = {}

        self.loadNameData()

    # TODO: try have better perf (setup timer for check)
    def loadNameData(self):
        if self.app is not None:
            self.progressBar = self.app.searchProgressBar

        # Load CSV file
        with open(self.file) as csv_file:
            # Read CSV file
            csv_reader = csv.reader(csv_file, delimiter=';')
            lineCount = 0
            # Read each line
            for row in csv_reader:
                # Don't read first line
                if lineCount == 0:
                    lineCount += 1
                    continue
                else:
                    if self.isNameClassesNotEmpty() and self.ifNameAlreadyExist(row[1]):
                        nameClass = self.nameClasses[row[1]]
                        if not nameClass.isAsexual and not nameClass.isGender(row[0]):
                            nameClass.setAsexual(True)
                        nameClass.addYear(row[2], row[3], row[0])
                    else:
                        # First time name is read
                        nameClass = Name(row[1], row[0])
                        nameClass.addYear(row[2], row[3], row[0])

                        self.nameClasses[row[1]] = nameClass

                if self.app is not None:
                    self.incrementProgressBar(lineCount)

                lineCount += 1

    # Check if name already exist in dict
    def ifNameAlreadyExist(self, name):
        return name in self.nameClasses

    # Check if dict in not empty
    def isNameClassesNotEmpty(self):
        return self.nameClasses

    def incrementProgressBar(self, lineCount):
        # Divide by 100 total lines for progressBar part
        if lineCount - self.linesCounted == self.progressBarPart:
            self.linesCounted = lineCount
            self.progressBar["value"] += 1
            # Update self.window UI
            self.app.window.update()

    def getNameClassData(self):
        return self.nameClasses
