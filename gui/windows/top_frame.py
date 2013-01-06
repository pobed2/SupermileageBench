import wx

class TopFrame(wx.Frame):
    def __init__(self, controller, parent=None, id=-1, title=""):
        wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition)
        self.controller = controller
        self._createMenu()
        self.Maximize()

    # ------------------ Top Menu

    def _createMenu(self):
        self.menuBar = wx.MenuBar()
        self.menuFile = wx.Menu()

        menu_properties = self.menuFile.Append(-1, "Properties", "Properties")
        self.Bind(wx.EVT_MENU, self.controller.on_properties_click, menu_properties)

        self.menuBar.Append(self.menuFile, "&File")
        self.SetMenuBar(self.menuBar)

