class Name:

    def __init__(self, name, gender):
        self.years = {'1': {}, '2': {}, '3': {}}
        self.yearId = {'1': 0, '2': 0, '3': 0}
        self.isAsexual = False
        self.gender = gender
        self.name = name
        self.totalUses = 0

    def addYear(self, year, uses, gender):
        self.years[gender][self.yearId[gender]] = {'year': year, 'uses': uses}
        self.yearId[gender] += 1

        if self.isAsexual:
            self.addAsexualYear(year, uses)

        self.totalUses += int(uses)

    def setAsexual(self, isAsexual):
        if self.isAsexual:
            return
        self.isAsexual = isAsexual
        self.setYearDataIntoCorrectGender()
        self.gender = '3'

    def yearExistInYears(self, year, gender):
        for yearId in self.years[gender]:
            if self.years[gender][yearId]['year'] == year:
                return yearId
        else:
            return None

    def addAsexualYear(self, year, uses):
        yearId = self.yearExistInYears(year, '3')
        if yearId is not None:
            actualUses = self.years['3'][yearId]['uses']
            self.years['3'][yearId]['uses'] = int(uses) + int(actualUses)
        else:
            self.yearId['3'] += 1
            self.years['3'][self.yearId['3']] = {'year': year, 'uses': uses}

    def getYearsData(self):
        return self.years

    def setYearDataIntoCorrectGender(self):
        for i in range(0, self.yearId[self.gender]):
            self.years['3'].update({i: self.years[self.gender][i].copy()})
        self.yearId['3'] = self.yearId[self.gender] + 1

    def isGender(self, gender):
        return gender == self.gender
