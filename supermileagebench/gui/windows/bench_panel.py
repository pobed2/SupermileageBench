from __future__ import division
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigCanvas

import wx

class BenchPanel(object):
    def __init__(self, sub_data_plots, parent, width=1280, height=720, dpi=100):
        self.panel = wx.Panel(parent, -1)
        self.panel.SetSize((1280, 720))

        self.sub_data_plots = sub_data_plots
        self._init_plots(width, height, dpi)


    def _init_plots(self, width, height, dpi):
        self.fig = Figure((width / dpi, height / dpi), dpi=dpi)
        self.canvas = FigCanvas(self.panel, -1, self.fig)

        for plot in self.sub_data_plots:
            plot.initialize_figure(self.fig)

        self.graphBox = wx.BoxSizer(wx.VERTICAL)
        self.graphBox.Add(self.canvas, 1, flag=wx.LEFT | wx.TOP | wx.GROW)

        self.panel.SetSizer(self.graphBox)
        self.panel.Show()

    def drawPlot(self):
        for plot in self.sub_data_plots:
            plot.prepare_plot_for_draw()
        self.canvas.draw()

    def hide(self):
        self.panel.Hide()

    def show(self):
        self.panel.Show()
