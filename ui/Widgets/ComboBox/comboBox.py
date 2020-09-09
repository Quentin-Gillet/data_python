from tkinter import Label
from tkinter.ttk import Combobox

from ui.Widgets.widget import Widget


class ComboBox(Widget):

    def __init__(self, window, text, values):
        super().__init__(window)
        self.text = text
        self.values = values
        self.comboBoxLabel = Label(window, text=text)
        self.comboBoxSelector = Combobox(window, state='readonly', width=20,
                                         values=list(values.keys()))

    def grid(self, row, column, func, stick=None, columnspan=None, rowspan=None):
        self.comboBoxLabel.grid(row=row, column=column)
        self.comboBoxSelector.grid(row=row, column=(column+1), columnspan=columnspan, stick=stick)
        self.comboBoxSelector.bind("<<ComboboxSelected>>", func)
        self.comboBoxSelector.current(0)

    def get(self):
        return self.comboBoxSelector.get()
