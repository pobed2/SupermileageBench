from __future__ import division

import wx
from gui.custom_widgets.constants_sidebar import ConstantsSidebar
from gui.custom_widgets.dropbox_files_sidebar import DropboxFilesSidebar
from gui.custom_widgets.plot_canvas import PlotCanvas
from gui.custom_widgets.start_stop_topbar import StartStopTopbar

class BenchPanel(wx.Panel):
    def __init__(self, sub_data_plots, parent):
        wx.Panel.__init__(self, parent, -1)
        self.sub_data_plots = sub_data_plots
        self._init_widgets()


    def _init_widgets(self):
        self.start_stop_buttons = StartStopTopbar(self)
        self.listBox1 = DropboxFilesSidebar(self, ["Allo", "GGG"])
        self.constants_sidebar = ConstantsSidebar(self)
        self.plot_canvas = PlotCanvas(self, self.sub_data_plots)

        self.vertical_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.vertical_sizer.Add(self.listBox1, 1, wx.GROW)
        self.vertical_sizer.Add(self.plot_canvas, 5, wx.GROW)
        self.vertical_sizer.Add(self.constants_sidebar, 1, wx.GROW)

        self.graphBox = wx.BoxSizer(wx.VERTICAL)
        self.graphBox.Add(self.start_stop_buttons, 1, flag=wx.LEFT | wx.TOP | wx.GROW)
        self.graphBox.Add(self.vertical_sizer, 20, wx.GROW)

        self.SetSizer(self.graphBox)
        self.Show()

    def hide_sidebar(self):
        self.vertical_sizer.Layout()

    def draw_plot_canvas(self):
        self.plot_canvas.draw()

    def hide(self):
        self.Hide()

    def show(self):
        self.Show()
