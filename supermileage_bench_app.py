import wx
from app_initialization.app_controller import AppController


class SupermileageBenchApp(wx.App):
    def OnInit(self):
        self.app_controller = AppController()
        return True

app = SupermileageBenchApp(0)
app.MainLoop()