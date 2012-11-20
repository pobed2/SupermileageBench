
import wx
import matplotlib       # Provides the graph figures
matplotlib.use('WXAgg') # matplotlib needs a GUI (layout), we use wxPython
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigCanvas

class MainFrame(wx.Frame):

    def __init__(self, parent = None, id = -1,title = ""):

        # Sizing information.  Pixels sizes for the Frame are dpi * length
        self.dpi = 100
        self.height = 7
        self.width = 12
        wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition,((self.width * self.dpi),(self.height * self.dpi)))
        self._createMenu()

    def set_controller(self, controller):
        self.controller = controller

        # ------------------ Event Handler Functions
    def onClose(self, event):
        self.Close()

    def onStartClick(self, event):
        self.controller.start_plotting()

    def onStopAndSaveClick(self, event):
        self.controller.stop_plotting(save = True)

    def onStopAndDeleteClick(self, event):
        self.controller.stop_plotting(save = False)


    # ------------------ Top Menu

    def _createMenu(self):
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

