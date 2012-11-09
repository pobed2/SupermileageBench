'''
Created on Sep 23, 2012

@author: MacBook
'''

import os
import wx

import matplotlib       # Provides the graph figures
matplotlib.use('WXAgg') # matplotlib needs a GUI (layout), we use wxPython
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigCanvas

from filters import savitzky_golay

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
        
        self.initPlot()
        self.createMenu()

        self.canvas = FigCanvas(self.panel, -1, self.fig)
        


        # ---------- GUI Variables
        # Graph Arrays
        
        self.database = database
        self.time = database.time

        #self.plotPosition()
        #self.plotVelocity()

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

#    def plotPosition(self):
#        self.positions = self.database.positions
#        self.plotPositions = self.axes.plot(
#            self.positions,
#            linewidth=1,
#            color=(1, 1, 1),
#            )[0]
#
#    def plotVelocity(self):
#        self.velocities = self.database.velocities
#        self.plotVelocities = self.veloPlot.plot(
#            self.velocities,
#            linewidth=1,
#            color=(1, 1, 0),
#            )[0]
    
    def plotAcceleration(self):
        self.accelerations = self.database.accelerations
        self.plotAccelerations = self.accelPlot.plot(
            self.accelerations, 
            linewidth=1,
            color=(1, 0, 0),
            )[0]

    def plotTorque(self):
        self.torques = self.database.torque
        self.plotTorques = self.torquePlot.plot(
            self.torques,
            linewidth=1,
            color=(0,1,0),
        )[0]
    
    # Size, color, etc
    def initPlot(self):
        self.fig = Figure((self.width, (self.height)), dpi=self.dpi)

#        self.axes = self.fig.add_subplot(221)
#        self.axes.set_axis_bgcolor('black')
#        self.axes.set_title('Position', size=12)
#        self.axes.set_xlabel("Time (seconds)", size=10)
#        self.axes.set_ylabel("Position (radians)", size=10)
#
#        pylab.setp(self.axes.get_xticklabels(), fontsize=8)
#        pylab.setp(self.axes.get_yticklabels(), fontsize=8)
#
#        self.veloPlot = self.fig.add_subplot(222)
#        self.veloPlot.set_axis_bgcolor('black')
#        self.veloPlot.set_title('Velocity', size=12)
#        self.veloPlot.set_xlabel("Time (seconds)", size=10)
#        self.veloPlot.set_ylabel("Velocity (radians per seconds)", size=10)
        
        self.accelPlot = self.fig.add_subplot(121)
        self.accelPlot.set_axis_bgcolor('black')
        self.accelPlot.set_title('Acceleration', size=12)
        self.accelPlot.set_xlabel("Time (seconds)", size=10)
        self.accelPlot.set_ylabel("Acceleration (radians per seconds^2)", size=10)

        self.torquePlot = self.fig.add_subplot(122)
        self.torquePlot.set_axis_bgcolor('black')
        self.torquePlot.set_title('Torque', size=12)
        self.torquePlot.set_xlabel("Time (seconds)", size=10)
        self.torquePlot.set_ylabel("Torque", size=10)

    # What gets called each on each redraw timer fire event
    def drawPlot(self):
        if(len(self.database.torque)!=0):

            gap = (self.time[-1] if self.time[-1] > self.timeToDisplay else self.timeToDisplay)
            xmax = gap + self.timeBeforeEnd
            xmin = gap - self.timeToDisplay    
                
#            self.axes.set_xbound(lower=xmin, upper=xmax)
#            self.veloPlot.set_xbound(lower=xmin, upper=xmax)
            self.accelPlot.set_xbound(lower=xmin, upper=xmax)
            self.torquePlot.set_xbound(lower=xmin, upper=xmax)
            
#            yminPos = round(min(self.positions), 0) - (0.1 * abs(round(min(self.positions), 0)))
#            ymaxPos = round(max(self.positions), 0) + (0.1 * round(max(self.positions), 0))
#            self.axes.set_ybound(lower=yminPos, upper=ymaxPos)
#
#            yminVelo = round(min(self.velocities), 0) - (0.1 * abs(round(min(self.velocities), 0)))
#            ymaxVelo = round(max(self.velocities), 0) + (0.1 * round(max(self.velocities), 0))
#            self.veloPlot.set_ybound(lower=yminVelo, upper=ymaxVelo)
            
            yminAccel = round(min(self.accelerations), 0) - (0.1 * abs(round(min(self.accelerations), 0)))
            ymaxAccel = round(max(self.accelerations), 0) + (0.1 * round(max(self.accelerations), 0))  
            self.accelPlot.set_ybound(lower=yminAccel, upper=ymaxAccel)

            yminTorque = round(min(self.database.torque), 0) - (0.1 * abs(round(min(self.database.torque), 0)))
            ymaxTorque = round(max(self.database.torque), 0) + (0.1 * round(max(self.database.torque), 0))
            self.torquePlot.set_ybound(lower=yminTorque, upper=ymaxTorque)

            
#            self.axes.grid(True, color='gray')
#            pylab.setp(self.axes.get_xticklabels(),
#                visible=True)
    
            timeArray = np.array(self.time)            
#            self.plotPositions.set_data(timeArray, np.array(self.positions))
#
#            self.plotVelocities.set_data(timeArray[len(self.velocities)-len(timeArray):], np.array(self.velocities))
            self.plotAccelerations.set_data(timeArray[len(self.accelerations)-len(timeArray):], np.array(self.accelerations))
            self.plotTorques.set_data(timeArray[len(self.database.torque)-len(timeArray):], np.array(self.database.torque))

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

    # Note this saves -all- accelerations from self.fileX variables
    def onSaveCSV(self, event):
        fileChoices = "CSV (*.csv)|*.csv"
        
        dlg = wx.FileDialog(
            self, 
            message="Save accelerations as...",
            defaultDir=os.getcwd(),
            defaultFile="plot.csv",
            wildcard=fileChoices,
            style=wx.SAVE)
        
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            outFile = open(path, 'w')

            outFile.write("Time, Positions, Velocities, Accelerations\n")
            for i in range(len(self.time)):
                outFile.write(str(self.time[i]) + ",")
                outFile.write(str(self.positions[i]) + ",")
                outFile.write(str(self.velocities[i]) + ",")
                outFile.write(str(self.accelerations[i]) + "\n")
            outFile.close()
