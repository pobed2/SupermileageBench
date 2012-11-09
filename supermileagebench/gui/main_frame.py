import os
import wx

import matplotlib       # Provides the graph figures
matplotlib.use('WXAgg') # matplotlib needs a GUI (layout), we use wxPython
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigCanvas
from data_plot import DataPlot

import numpy as np  # For efficient data array handling
import pylab

class MainFrame(wx.Frame):

    def __init__(self, parent, id, database, title=None):

        # Sizing information.  Pixels sizes for the Frame are dpi * length
        self.dpi = 100
        self.height = 7
        self.width = 12
        wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition,
            ((self.width * self.dpi), (self.height * self.dpi)))

        # Maximum total time (seconds) to be displayed on x axis
        self.timeToDisplay = 25
        self.timeBeforeEnd = 5


        # --------- GUI and graph initialization
        self.panel = wx.Panel(self, -1)

        self.init_plots()
        self.createMenu()





        # ---------- GUI Variables
        # Graph Arrays

        self.database = database
        self.time = database.time

        self.plotAcceleration()
        self.plotTorque()

        # This times fires every 100 ms to redraw the graphs
        self.redrawPeriod = 100
        self.redrawTimer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.onRedrawTimer, self.redrawTimer)

        # -------- GUI components

        self.graphBox = wx.BoxSizer(wx.VERTICAL)
        self.graphBox.Add(self.canvas, 1, flag=wx.LEFT | wx.TOP | wx.GROW)

        self.panel.SetSizer(self.graphBox)
        self.panel.Show()

    # ------------------ Event Handler Functions


    def startTimer(self):
        self.redrawTimer.Start(self.redrawPeriod)

    def onClose(self, event):
        self.Close()

    def onStartClick(self, event):
        self.database.startDataAquisition()

    def onStopAndSaveClick(self, event):
        self.database.stopDataAquisition(save = True)
        self.resetCanvas()

    def onStopAndDeleteClick(self, event):
        self.database.stopDataAquisition(save = False)
        self.resetCanvas()

    def resetCanvas(self):
        pass

        # ---------- Plot and canvas (graph) functionality

    def init_plots(self):
        self.fig = Figure((self.width, (self.height)), dpi=self.dpi)
        self.canvas = FigCanvas(self.panel, -1, self.fig)
        self.subplots = []

        acceleration_repository = ''
        torque_repository = ''

        #Add subplots here
        accelerationPlot = DataPlot(acceleration_repository, self.fig, subplot_code=(121), title='Acceleration', x_label='Time (s)'
                        , y_label= 'Acceleration (radians / seconds^2)')
        torquePlot = DataPlot(torque_repository, self.fig, subplot_code=(122), title='Torque', x_label='Time (s)'
            , y_label= 'Torque')

        self.subplots.append(accelerationPlot)
        self.subplots.append(torquePlot)

    def drawPlot(self):

        for plot in self.subplots:
            plot.prepare_plot_for_draw()

        self.canvas.draw()

    def onRedrawTimer(self, event):
        try:
            self.drawPlot()
        except RuntimeError as e:
            print e




    # ------------------ Top Menu

    # The top menu under File, including saving as csv, image, or exiting.
    # This also handles the Ctrl-X shortcut for exiting.
    def createMenu(self):
        self.menuBar = wx.MenuBar()

        self.menuFile = wx.Menu()

        menuStart = self.menuFile.Append(-1, "&Start Data Acquisition", "Start")
        self.Bind(wx.EVT_MENU, self.onStartClick, menuStart)

        menuStopAndSave = self.menuFile.Append(-1, "&Stop and Save to Dropbox", "Stop accelerations aquisition and save")
        self.Bind(wx.EVT_MENU, self.onStopAndSaveClick, menuStopAndSave)

        menuStopAndDelete = self.menuFile.Append(-1, "&Stop and Delete Data", "Stop accelerations aquisition and delete")
        self.Bind(wx.EVT_MENU, self.onStopAndDeleteClick, menuStopAndDelete)

        menuSaveCSV = self.menuFile.Append(-1, "&Save plot as CSV", "Save accelerations to csv")
        self.Bind(wx.EVT_MENU, self.onSaveCSV, menuSaveCSV)

        menuSave = self.menuFile.Append(-1, "&Save plot as image", "Save plot to image")
        self.Bind(wx.EVT_MENU, self.onSavePlot, menuSave)

        self.menuFile.AppendSeparator()

        menuExit = self.menuFile.Append(-1, "E&xit\tCtrl-X", "Exit")
        self.Bind(wx.EVT_MENU, self.onClose, menuExit)

        self.menuBar.Append(self.menuFile, "&File")
        self.SetMenuBar(self.menuBar)


    # ----- Save as Image
    def onSavePlot(self, event):
        fileChoices = "PNG (*.png)|*.png"

        dlg = wx.FileDialog(
            self,
            message="Save plot as...",
            defaultDir=os.getcwd(),
            defaultFile="plot.png",
            wildcard=fileChoices,
            style=wx.SAVE)

        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            self.canvas.print_figure(path, dpi=self.dpi)

    # ----- Save as file

    def onSaveCSV(self, event):
        fileChoices = "CSV (*.csv)|*.csv"

        dlg = wx.FileDialog(
            self,
            message="Save data as...",
            defaultDir=os.getcwd(),
            defaultFile="plot.csv",
            wildcard=fileChoices,
            style=wx.SAVE)

        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            outFile = open(path, 'w')

            outFile.write("Time, Positions, Velocities, Accelerations, Torques\n")
            for i in range(len(self.time)):
                outFile.write(str(self.database.file_time[i]) + ",")
                outFile.write(str(self.database.file_positions[i]) + ",")
                outFile.write(str(self.database.file_velocities[i]) + ",")
                outFile.write(str(self.database.file_accelerations[i]) + ",")
                outFile.write(str(self.database.file_torque) + "\n")
            outFile.close()

