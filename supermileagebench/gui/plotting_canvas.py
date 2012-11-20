from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigCanvas


class Plotting_Canvas(object):

    def __init__(self, subplots, periodic = True, parent = None, id = -1,title = ""):
        self.subplots = subplots
        self.init_plots()
        self.createMenu()

    def init_plots(self):
        self.fig = Figure((self.width, (self.height)), dpi=self.dpi)
        self.canvas = FigCanvas(self.panel, -1, self.fig)

        for plot in self.subplots:
            plot.initialize_figure(self.fig)

        self.graphBox = wx.BoxSizer(wx.VERTICAL)
        self.graphBox.Add(self.canvas, 1, flag=wx.LEFT | wx.TOP | wx.GROW)

        self.panel.SetSizer(self.graphBox)
        self.panel.Show()
