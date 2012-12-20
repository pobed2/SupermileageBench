import wx
from gui.custom_widgets.custom_navigation_toolbar import CustomNavigationToolbar

class PlottingToolbar(wx.Panel):
    def __init__(self, parent, canvas):
        wx.Panel.__init__(self, parent, -1)

        self.toolbar = CustomNavigationToolbar(canvas)
        self.toolbar.Realize()

        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(self.toolbar, 1, flag=wx.LEFT | wx.TOP | wx.GROW)

        self.SetSizer(self.sizer)

