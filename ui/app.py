from tkinter.ttk import *
from tkinter import *
from Models.NameSearchers.nameSearcher import NameSearcher
from Models.name import Name
from Models.plot import Plot
from Utils.operations import *
from ui.Widgets.ComboBox.comboBox import ComboBox


class App:

    def __init__(self):
        # Init tkinter
        self.window = Tk()

        # Variables
        self.width = 700
        self.height = 700
        self.isLoadingNames = False
        self.nameGender = []
        self.nameSearcher = None
        self.wantedGender = None
        self.wantedPlotType = 0
        self.wantedSearchType = 0
        self.nameClass = None
        self.plot = None
        self.plotIsBuild = False

        # WIDGET INITIALIZATION
        self.inputFrame = Frame(self.window)
        self.searchInputLbl = Label(self.inputFrame, text="Entrez un nom: ")
        self.searchInputField = Entry(self.inputFrame, textvariable="-SEARCHNAME-", width=21)
        self.searchInputButton = Button(self.inputFrame, text="Chercher", command=self.searchName, padx=15, pady=15,
                                        height=3)

        self.plotTypeValues = {'Histogramme': 0, 'Histogramme V2': 1, 'Diagramme': 2, 'Tige': 3}
        self.plotTypeComboBoxSelector = ComboBox(self.inputFrame, "Type de graphique: ", self.plotTypeValues)

        self.searchTypeValues = {'Recherche par nom': 0, 'Comparer des noms': 1, 'Autres': 2}
        self.searchTypeComboBoxSelector = ComboBox(self.inputFrame, "Type de recherche: ", self.searchTypeValues)

        self.searchProgressBar = Progressbar(self.inputFrame, value=0, orient='horizontal', length=430, mode='determinate')

        self.resultFrame = Frame(self.window)
        self.resultLabel = Label(self.resultFrame, text="", fg="blue")

        self.genderLabel = Label(self.resultFrame, fg="green")
        self.genderSelectorValue = {'Asexuel': "3", 'Masculin': "1", 'Féminin': "2"}
        self.genderComboBoxSelector = Combobox(self.resultFrame, state='readonly', values=list(self.genderSelectorValue.keys()), height=5)

        self.errorLabel = Label(self.inputFrame, fg="red")

    # Define base app options
    def startWindow(self):
        self.window.grid_columnconfigure(0, weight=1)
        self.window.wm_title("Data Python")
        self.window.resizable(False, False)
        self.window.protocol("WM_DELETE_WINDOW", self.closeWindow)
        self.window.bind('<Return>', self.searchName)

        self.setupElements()

        # Start loop for app
        self.window.mainloop()

    # Place elements in window
    def setupElements(self):
        self.searchInputLbl.grid(row=1, column=0)
        self.searchInputField.grid(row=1, column=1, sticky='NW')
        self.searchInputButton.grid(row=1, column=3, rowspan=4)

        self.plotTypeComboBoxSelector.grid(row=2, column=0, func=self.switchPlotType, columnspan=2, stick='NW')
        self.searchTypeComboBoxSelector.grid(row=3, column=0, func=self.switchSearchType, columnspan=2, stick='NW')

        self.inputFrame.grid_columnconfigure(0, weight=1)
        self.inputFrame.grid_rowconfigure(0, weight=1)
        self.inputFrame.grid(row=0, column=0)

        # Set focus on input
        self.searchInputField.focus_set()

    # When main action is trigger
    def searchName(self, event=None):
        name = self.searchInputField.get().upper()
        if not self.appReadyToPerformSearch(name, event):
            return

        self.prepareForLoading()
        self.setupNameSearcher()
        self.finalizeLoading()

        nameClass = self.performSearch(name)

        if not isinstance(nameClass, Name):
            self.displayError(nameClass["errorMessage"])
            return

        if nameClass.isAsexual:
            self.wantedGender = '3'
        else:
            self.wantedGender = nameClass.gender

        self.createPlotCanvas(nameClass.getYearsData())
        self.setupNameInfos()
        self.changeProgressBarValue(100)
        self.resultFrame.grid(row=1, column=0, sticky="NESW")

    # Like name say
    def prepareForLoading(self):
        # Clear window
        self.cleanMainFrame()
        self.searchProgressBar.grid(row=5, column=0, columnspan=5, stick='NW')
        self.isLoadingNames = True
        self.searchInputField['state'] = 'disabled'

    # Function to display error label and set correct text error
    def displayError(self, errorText):
        self.errorLabel['text'] = errorText
        self.errorLabel.grid(row=0, column=0, columnspan=3, sticky='nw')

    # Like name say
    def setupGenderSelector(self):
        self.genderComboBoxSelector.current(0)
        self.genderComboBoxSelector.bind("<<ComboboxSelected>>", self.switchGenderPlot)

    # Permute the wantedPlotType var
    def switchPlotType(self, event=None):
        plotType = self.plotTypeValues[self.plotTypeComboBoxSelector.get()]
        self.wantedPlotType = plotType
        if self.plotIsBuild:
            self.createPlotCanvas(self.nameClass.getYearsData())

    # Permute the wantedSearchType var
    def switchSearchType(self, event=None):
        searchType = self.searchTypeValues[self.searchTypeComboBoxSelector.get()]
        self.wantedSearchType = searchType
        # TODO: define action to draw wanted widget

    # Permute the wantedGender plot var
    def switchGenderPlot(self, event=None):
        gender = self.genderSelectorValue[self.genderComboBoxSelector.get()]
        self.wantedGender = gender
        self.createPlotCanvas(self.nameClass.getYearsData())

    # Like name say
    def finalizeLoading(self):
        self.searchInputField['state'] = 'normal'
        self.isLoadingNames = False
        self.searchProgressBar.grid_forget()

    # Remove and reset all unnecessary elements
    def cleanMainFrame(self):
        self.resultLabel.grid_forget()
        self.errorLabel.grid_forget()
        self.genderLabel.grid_forget()
        self.genderComboBoxSelector.grid_forget()
        self.resultFrame.grid_forget()
        self.searchProgressBar["value"] = 0
        if self.plotIsBuild and self.plot is not None:
            self.plot.destroy()
            self.plotIsBuild = False

    # When close action is send destroy and quit app
    def closeWindow(self):
        self.cleanMainFrame()
        self.window.destroy()
        self.window.quit()

    # Delete the existing plot and create a new one with wanted values
    def createPlotCanvas(self, years):
        # Get data ready for plot implementation
        yearsList, usesList = cleanDataForHistogramWithYears(years[self.wantedGender])
        # Draw plot on a separate frame
        self.plot = Plot(yearsList, usesList, self.wantedPlotType, self.resultFrame).draw()
        self.plotIsBuild = True

    # Setup name infos
    def setupNameInfos(self):
        # Display all info on a separate frame
        self.resultLabel['text'] = 'Le nom ' + self.nameClass.name.upper() + ' a été utilisé ' + str(
            formatHundredNumbers(self.nameClass.totalUses)) + ' fois.'

        self.genderLabel['text'] = 'Genre: ' + defineGenderName(self.wantedGender)
        if self.wantedGender == '3':
            self.setupGenderSelector()

        # Place it
        self.resultLabel.grid(row=0, column=0, columnspan=3, sticky='nw')
        self.genderLabel.grid(row=1, column=0, sticky='nw')
        if self.wantedGender == '3':
            self.genderComboBoxSelector.grid(row=1, column=1, sticky='nw')

    def appReadyToPerformSearch(self, name, event):
        # If app is loading names return
        if self.isLoadingNames:
            return False

        # If name is empty pass
        if not name:
            self.displayError("Veuillez entrer un nom.")
            return False
        if self.nameClass and isinstance(self.nameClass, Name) and self.nameClass.name == name:
            return False
        # If function is call from 'ENTER' and focus is on correct InputField
        if event is not None:
            if self.window.focus_get() != self.searchInputField:
                return False
        return True

    def setupNameSearcher(self):
        if self.nameSearcher is None:
            self.nameSearcher = NameSearcher(self)

    def changeProgressBarValue(self, value):
        self.searchProgressBar['value'] = value
        self.window.update()

    def performSearch(self, name):
        self.prepareForLoading()
        nameClass = self.nameSearcher.find(self.wantedSearchType, name)
        self.changeProgressBarValue(80)
        self.nameClass = nameClass
        self.finalizeLoading()
        return nameClass
