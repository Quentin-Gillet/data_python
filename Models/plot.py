import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from Utils.maths import percentage, gradient_image, gradient_bar
from Utils.operations import onKeyPress
from tkinter import Frame


class Plot:

    def __init__(self, years, uses, plotType, window):
        self.years = years
        self.uses = uses
        self.plotType = plotType
        self.window = window

        self.plot = None
        self.axes = None
        self.canvas = None
        self.toolBar = None
        self.toolBarFrame = None

        self.defaultPlotSetup()
        self.drawFigure()

    def defaultPlotSetup(self):
        plt.rcdefaults()

        self.plot, self.axes = plt.subplots()

        maxUses = max(self.uses)

        xlim = min(self.years), 2 + max(self.years)
        ylim = min(self.uses), maxUses + percentage(maxUses, 10)

        self.axes.set(xlim=xlim, ylim=ylim, autoscale_on=False)
        self.axes.set_ylabel('Nombre de fois utilisés')
        self.axes.set_title('Années')

        self.plot.tight_layout()

    def drawFigure(self):
        if self.plotType == 0:
            self.createHistogram()
        elif self.plotType == 1:
            self.createPrettyHistogram()
        elif self.plotType == 2:
            self.createDiagram()
        elif self.plotType == 3:
            self.createStem()
        else:
            self.createHistogram()

    def createHistogram(self):
        self.axes.bar(self.years, self.uses, align='center')

    def createPrettyHistogram(self):
        gradient_image(self.axes, direction=0, extent=(0, 1, 0, 1), transform=self.axes.transAxes,
                       cmap=plt.cm.Oranges, cmap_range=(0.1, 0.6))

        gradient_bar(self.axes, self.years, self.uses, width=0.7)
        self.axes.set_aspect('auto')

    def createDiagram(self):
        self.axes.plot(self.years, self.uses, color='blue', lw=1)

    def createStem(self):
        self.axes.stem(self.years, self.uses)

    def destroy(self):
        self.canvas.get_tk_widget().destroy()
        # TODO: error sometimes when delete toolBar
        # self.toolBar.destroy()
        self.toolBarFrame.destroy()

    def draw(self):
        canvas = FigureCanvasTkAgg(self.plot, master=self.window)
        canvas.draw()
        canvas.get_tk_widget().grid(row=6, column=0, columnspan=10, padx=10, sticky='nw')

        toolbarFrame = Frame(master=self.window)
        toolbarFrame.grid(row=7, column=0, columnspan=10)
        toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)

        canvas.mpl_connect("key_press_event", lambda: onKeyPress(canvas, toolbar))

        plt.close('all')

        self.canvas = canvas
        self.toolBar = toolbar
        self.toolBarFrame = toolbarFrame
