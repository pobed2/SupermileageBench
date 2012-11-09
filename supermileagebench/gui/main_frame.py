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

    def __init__(self, subplots, periodic = True, parent = None, id = -1,title = ""):

        # Sizing information.  Pixels sizes for the Frame are dpi * length
        self.dpi = 100
        self.height = 7
        self.width = 12
        wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition,((self.width * self.dpi),(self.height * self.dpi)))

        self.panel = wx.Panel(self, -1)

        self.subplots = subplots
        self.init_plots()
        self.createMenu()

        if periodic:
            self.init_timer()

        self.graphBox = wx.BoxSizer(wx.VERTICAL)
        self.graphBox.Add(self.canvas, 1, flag=wx.LEFT | wx.TOP | wx.GROW)

        self.panel.SetSizer(self.graphBox)
        self.panel.Show()

    def set_controller(self, controller):
        self.controller = controller

    def init_plots(self):
        self.fig = Figure((self.width, (self.height)), dpi=self.dpi)
        self.canvas = FigCanvas(self.panel, -1, self.fig)

        for plot in self.subplots:
            plot.initialize_figure(self.fig)

    def init_timer(self):
        self.redrawPeriod = 100
        self.redrawTimer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.onRedrawTimer, self.redrawTimer)

    def drawPlot(self):
        for plot in self.subplots:
            plot.prepare_plot_for_draw()

        self.canvas.draw()

    def startTimer(self):
        self.redrawTimer.Start(self.redrawPeriod)

    def stop_timer(self):
        self.redrawTimer.Stop()

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

        self.menuFile.AppendSeparator()

        menuExit = self.menuFile.Append(-1, "E&xit\tCtrl-X", "Exit")
        self.Bind(wx.EVT_MENU, self.onClose, menuExit)

        self.menuBar.Append(self.menuFile, "&File")
        self.SetMenuBar(self.menuBar)

    # ------------------ Event Handler Functions




    def onClose(self, event):
        self.Close()

    def onStartClick(self, event):
        self.controller.start_plotting()

    def onStopAndSaveClick(self, event):
        self.controller.stop_plotting(save = True)

    def onStopAndDeleteClick(self, event):
        self.controller.stop_plotting(save = False)