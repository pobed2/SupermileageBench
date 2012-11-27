import wx
from supermileagebench.gui.controllers.app_controller import AppController


class MainClass(wx.App):
    def OnInit(self):
        self.app_controller = AppController()
        return True

app = MainClass(0)
app.MainLoop()