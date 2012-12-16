import wx

class StartStopTopbar(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, 0, style=wx.SIMPLE_BORDER)
        self.start_button = wx.Button(self, label="Start")
        self.stop_button = wx.Button(self, label="Stop")

        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(self.start_button, 1, flag=wx.CENTER)
        self.sizer.Add(self.stop_button, 1, flag=wx.CENTER)

        self.SetSizer(self.sizer)


