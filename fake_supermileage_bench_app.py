import wx
from app_initialization.faked.fake_app_controller import FakeAppController


class FakeSupermileageBenchApp(wx.App):
    def OnInit(self):
        self.app_controller = FakeAppController()
        return True

app = FakeSupermileageBenchApp(0)
app.MainLoop()