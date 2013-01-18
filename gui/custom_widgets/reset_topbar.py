import wx
from gui.mvc_helpers.observable import Observable
from gui.mvc_helpers.observable_events import ResetAppClickedObservableEvent

class ResetTopbar(wx.Panel, Observable):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, 0, style=wx.SIMPLE_BORDER)
        Observable.__init__(self)

        self.reset_button = wx.Button(self, label="Refaire un autre essai")

        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(self.reset_button, 1, flag=wx.CENTER)

        self.SetSizer(self.sizer)

        self.reset_button.Bind(wx.EVT_BUTTON, self.on_reset)

    def on_reset(self, event):
        for observer in self.observers:
            observer.update(ResetAppClickedObservableEvent())
