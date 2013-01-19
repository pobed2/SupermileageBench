from __future__ import division
import wx

class BenchPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1)

        self.parent_sizer = wx.BoxSizer(wx.VERTICAL)
        self.parent_sizer.Add(self, 1, flag=wx.GROW)
        parent.SetSizer(self.parent_sizer)

    def add_panel_observers(self, observer):
        for widget in self.widgets:
            widget.add_observer(observer)

    def update_subplots(self, subplots):
        self.plot_canvas.update_subplots(subplots)
        self.refresh_canvas()

    def refresh_canvas(self):
        self.plot_canvas.draw()
