import wx
from gui.mvc_helpers.observable import Observable

class StartStopTopbar(wx.Panel, Observable):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, 0, style=wx.SIMPLE_BORDER)
        Observable.__init__(self)

        self.start_button = wx.Button(self, label="Start")
        self.stop_button = wx.Button(self, label="Stop")

        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(self.start_button, 1, flag=wx.CENTER)
        self.sizer.Add(self.stop_button, 1, flag=wx.CENTER)

        self.SetSizer(self.sizer)

        self.start_button.Bind(wx.EVT_BUTTON, self.on_start)
        self.stop_button.Bind(wx.EVT_BUTTON, self.on_stop)

    def on_start(self, event):
        for observer in self.observers:
            observer.update("start")

    def on_stop(self, event):
        for observer in self.observers:
            observer.update("stop")
