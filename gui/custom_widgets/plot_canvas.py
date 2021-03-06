from __future__ import division
from matplotlib.backends.backend_wx import NavigationToolbar2Wx

import wx
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigCanvas
from gui.mvc_helpers.observable import Observable

class PlotCanvas(wx.Panel, Observable):
    def __init__(self, parent, subplots):
        wx.Panel.__init__(self, parent, -1, style=wx.SIMPLE_BORDER)
        Observable.__init__(self)

        self.fig = Figure()
        self.canvas = FigCanvas(self, -1, self.fig)
        self.toolbar = NavigationToolbar2Wx(self.canvas)
        self.toolbar.Realize()

        self.initialize_subplots(subplots)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.toolbar, 1, wx.GROW | wx.CENTER)
        self.sizer.Add(self.canvas, 30, wx.GROW)

        self.SetSizer(self.sizer)

    def initialize_subplots(self, subplots):
        self.sub_data_plots = subplots

        for plot in self.sub_data_plots:
            plot.initialize_figure(self.fig)

    def draw(self):
        for plot in self.sub_data_plots:
            plot.prepare_plot_for_draw()
        self.canvas.draw()

    def update_subplots(self, subplots):
        self.fig.clf()
        self.initialize_subplots(subplots)
        self.canvas.draw()