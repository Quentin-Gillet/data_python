class SearchWithName:

    def __init__(self, app, nameClasses, name, options):
        self.app = app
        self.nameClasses = nameClasses
        self.name = name
        self.options = options

    def find(self):
        self.app.changeProgressBarValue(20)
        if self.options is None:
            if self.name in self.nameClasses:
                self.app.changeProgressBarValue(50)
                return self.nameClasses[self.name]
            else:
                return {"errorMessage": 'Le nom n\'a pas été trouvé.'}
        pass
