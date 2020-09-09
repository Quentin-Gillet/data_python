class CompareNames:

    def __init__(self, app, nameClasses, names, options):
        self.app = app
        self.nameClasses = nameClasses
        self.names = names
        self.options = options
        self.namesData = []

    def find(self):
        if self.options is None:
            for name in self.names:
                if name in self.nameClasses:
                    self.namesData.append(self.nameClasses[name])
                else:
                    return {"errorMessage": 'Le nom ' + name + ' n\'a pas été trouvé.'}

            return self.namesData
