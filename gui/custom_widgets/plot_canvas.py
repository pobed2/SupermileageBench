import wx
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigCanvas
from gui.custom_widgets.plotting_toolbar import PlottingToolbar
from gui.mvc_helpers.observable import Observable

class PlotCanvas(wx.Panel, Observable):
    def __init__(self, parent, subplots):
        wx.Panel.__init__(self, parent, -1, style=wx.SIMPLE_BORDER)
        Observable.__init__(self)

        self.fig = Figure()
        self.canvas = FigCanvas(self, -1, self.fig)
        self.sub_data_plots = subplots

        for plot in self.sub_data_plots:
            plot.initialize_figure(self.fig)

        self.toolbar = PlottingToolbar(self, self.canvas)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.toolbar, 1, wx.GROW | wx.CENTER)
        self.sizer.Add(self.canvas, 30, wx.GROW)

        self.SetSizer(self.sizer)

    def draw(self):
        for plot in self.sub_data_plots:
            plot.prepare_plot_for_draw()
        self.canvas.draw()