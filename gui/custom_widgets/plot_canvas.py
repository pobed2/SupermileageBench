import wx
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigCanvas

class PlotCanvas(wx.Panel):
    def __init__(self, parent, subplots):
        wx.Panel.__init__(self, parent, -1, style=wx.SIMPLE_BORDER)

        self.fig = Figure()
        self.canvas = FigCanvas(self, -1, self.fig)
        self.sub_data_plots = subplots

        for plot in self.sub_data_plots:
            plot.initialize_figure(self.fig)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.GROW)

        self.SetSizer(self.sizer)

    def draw(self):
        for plot in self.sub_data_plots:
            plot.prepare_plot_for_draw()
        self.canvas.draw()