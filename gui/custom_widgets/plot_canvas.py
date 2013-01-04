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
        self.canvas.mpl_connect('button_release_event', self.zoom_toolbar)
        self.canvas.mpl_connect('key_press_event', self.on_key)

        self.initialize_subplots(subplots)

        #self.toolbar = PlottingToolbar(self, self.canvas).Hide()
        self.toolbar = NavigationToolbar2Wx(self.canvas)
        self.toolbar.Hide()

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        #self.sizer.Add(self.toolbar, 1, wx.GROW | wx.CENTER)
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


    #toolbar crap
    def on_key(self, event):
        if event.key == "p":
            print "this is p"
            self.toolbar.pan()
        elif event.key == "z":
            self.toolbar.zoom()
        else:
            print event.key

    def zoom_toolbar(self, event):
        self.toolbar.pan()

    def zoom_fun(self, event):
        base_scale = 2
        print "scrolling"
        for ax in event.canvas.figure.axes:
            cur_xlim = ax.get_xbound()
            cur_ylim = ax.get_ybound()
            print cur_xlim
            print cur_ylim
            if event.button == 1:
                # deal with zoom in
                scale_factor = 1 / base_scale
            elif event.button == 2:
                # deal with zoom out
                scale_factor = base_scale
            else:
                # deal with something that should never happen
                scale_factor = 1
                print event.button
                # set new limits

            new_half_lenght = (cur_xlim[1] - cur_xlim[0]) * scale_factor * 0.5
            new_half_height = (cur_ylim[1] - cur_ylim[0]) * scale_factor * 0.5

            xdata = event.xdata # get event x location
            ydata = event.ydata # get event y location

            ax.set_xbound(lower=(xdata - new_half_lenght), upper=(xdata + new_half_lenght))
            ax.set_ybound(lower=(ydata - new_half_height), upper=(ydata + new_half_height))

            cur_xlim = ax.get_xbound()
            cur_ylim = ax.get_ybound()
            print cur_xlim
            print cur_ylim

        event.canvas.draw()