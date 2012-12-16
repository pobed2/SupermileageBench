from __future__ import division
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigCanvas

import wx
from gui.custom_widgets.constants_sidebar import ConstantsSidebar
from gui.custom_widgets.dropbox_files_sidebar import DropboxFilesSidebar
from gui.custom_widgets.start_stop_topbar import StartStopTopbar

class BenchPanel(object):
    def __init__(self, sub_data_plots, parent, width=1280, height=520, dpi=100):
        self.panel = wx.Panel(parent, -1)
        self.panel.SetSize((width, height))

        self.sub_data_plots = sub_data_plots
        self._init_plots(width, height, dpi)


    def _init_plots(self, width, height, dpi):
        self.fig = Figure()
        self.canvas = FigCanvas(self.panel, -1, self.fig)

        #        self.btn = wx.Button(self.panel, label="help?")

        self.start_stop_buttons = StartStopTopbar(self.panel)
        self.listBox1 = DropboxFilesSidebar(self.panel, ["Allo", "GGG"])
        self.constants_sidebar = ConstantsSidebar(self.panel)

        for plot in self.sub_data_plots:
            plot.initialize_figure(self.fig)

        self.vertical_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.vertical_sizer.Add(self.listBox1, 1, wx.GROW)
        self.vertical_sizer.Add(self.canvas, 5, wx.GROW)
        self.vertical_sizer.Add(self.constants_sidebar, 1, wx.GROW)

        self.graphBox = wx.BoxSizer(wx.VERTICAL)
        self.graphBox.Add(self.start_stop_buttons, 1, flag=wx.LEFT | wx.TOP | wx.GROW)
        self.graphBox.Add(self.vertical_sizer, 20, wx.GROW)

        self.panel.SetSizer(self.graphBox)
        self.panel.Show()

    def hide_sidebar(self):
        self.vertical_sizer.Layout()

    def drawPlot(self):
        for plot in self.sub_data_plots:
            plot.prepare_plot_for_draw()
        self.canvas.draw()

    def hide(self):
        self.panel.Hide()

    def show(self):
        self.panel.Show()
