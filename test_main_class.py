import wx
from supermileagebench.testing.test_app_controller import TestAppController


class MainClass(wx.App):
    def OnInit(self):
        self.app_controller = TestAppController()
        return True

app = MainClass(0)
app.MainLoop()