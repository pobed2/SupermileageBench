import wx

from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigCanvas


class BenchPanel(object):

    def __init__(self, sub_data_plots, parent):

        self.dpi = 100
        self.height = 7
        self.width = 12

        self.panel = wx.Panel(parent, -1)

        self.sub_data_plots = sub_data_plots
        self.init_plots()


    def init_plots(self):
        self.fig = Figure((self.width, self.height), dpi=self.dpi)
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
