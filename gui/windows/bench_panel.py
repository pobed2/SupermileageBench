from __future__ import division

import wx
from gui.custom_widgets.constants_sidebar import ConstantsSidebar
from gui.custom_widgets.dropbox_files_sidebar import DropboxFilesSidebar
from gui.custom_widgets.plot_canvas import PlotCanvas
from gui.custom_widgets.start_stop_topbar import StartStopTopbar

class BenchPanel(wx.Panel):
    def __init__(self, parent, sub_data_plots, filenames_to_compare_to):
        wx.Panel.__init__(self, parent, -1)
        self.widgets = self._init_widgets(sub_data_plots, filenames_to_compare_to)

    def _init_widgets(self, sub_data_plots, filenames_to_compare_to):
        self.start_stop_buttons = StartStopTopbar(self)
        self.listBox1 = DropboxFilesSidebar(self, filenames_to_compare_to)
        self.constants_sidebar = ConstantsSidebar(self)
        self.plot_canvas = PlotCanvas(self, sub_data_plots)

        self.vertical_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.vertical_sizer.Add(self.listBox1, 1, wx.GROW)
        self.vertical_sizer.Add(self.plot_canvas, 5, wx.GROW)
        self.vertical_sizer.Add(self.constants_sidebar, 1, wx.GROW)

        self.graphBox = wx.BoxSizer(wx.VERTICAL)
        self.graphBox.Add(self.start_stop_buttons, 1, flag=wx.LEFT | wx.TOP | wx.GROW)
        self.graphBox.Add(self.vertical_sizer, 20, wx.GROW)

        self.SetSizer(self.graphBox)
        self.Show()

        return [self.start_stop_buttons, self.listBox1, self.constants_sidebar, self.plot_canvas]

    def add_panel_observers(self, observer):
        for widget in self.widgets:
            widget.add_observer(observer)

    def hide_sidebar(self):
        self.vertical_sizer.Layout()

    def draw_plot_canvas(self):
        self.plot_canvas.draw()

    def hide(self):
        self.Hide()

    def show(self):
        self.Show()
