import wx

class TopFrame(wx.Frame):

    def __init__(self, controller, parent = None, id = -1,title = "", width = 1280, height = 720):
        wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition,(width,height))
        self.controller = controller
        self._createMenu()

    # ------------------ Top Menu

    def _createMenu(self):
        self.menuBar = wx.MenuBar()
        self.menuFile = wx.Menu()

        menuStart = self.menuFile.Append(-1, "&Start Data Acquisition", "Start")
        self.Bind(wx.EVT_MENU, self.controller.on_start_button_click, menuStart)

        menuStopAndSave = self.menuFile.Append(-1, "&Stop and Save to Dropbox", "Stop accelerations aquisition and save")
        self.Bind(wx.EVT_MENU, self.controller.on_stop_and_save_button_click, menuStopAndSave)

        menuStopAndDelete = self.menuFile.Append(-1, "&Stop and Delete Data", "Stop accelerations aquisition and delete")
        self.Bind(wx.EVT_MENU, self.controller.on_stop_and_delete_button_click, menuStopAndDelete)

        self.menuBar.Append(self.menuFile, "&File")
        self.SetMenuBar(self.menuBar)

