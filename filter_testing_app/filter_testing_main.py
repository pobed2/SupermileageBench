import wx
from filter_testing.filter_testing_controller import FilterTestingController


class FilterTestingMain(wx.App):
    def OnInit(self):
        self.controller = FilterTestingController()
        return True

app = FilterTestingMain(0)
app.MainLoop()
