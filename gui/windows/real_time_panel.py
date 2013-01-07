#coding: utf-8

import wx
from gui.custom_widgets.plot_selection.plot_selector import PlotSelector

from gui.windows.bench_panel import BenchPanel
from gui.custom_widgets.plot_canvas import PlotCanvas
from gui.custom_widgets.start_stop_topbar import StartStopTopbar
from configuration.app_settings import real_time_plot_types

class RealTimePanel(BenchPanel):
    def __init__(self, parent, sub_data_plots, subplots_names):
        super(RealTimePanel, self).__init__(parent)
        self.widgets = self._init_widgets(sub_data_plots, subplots_names)
        self._init_timer(parent)

    def _init_widgets(self, sub_data_plots, subplots_names):
        self.start_stop_buttons = StartStopTopbar(self)
        self.plot_canvas = PlotCanvas(self, sub_data_plots)
        self.plot_selector = PlotSelector(self, real_time_plot_types, subplots_names)

        self.topbar_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.topbar_sizer.Add(self.start_stop_buttons, 2, wx.GROW)
        self.topbar_sizer.Add(self.plot_selector, 1, wx.GROW)

        self.vertical_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.vertical_sizer.Add(self.plot_canvas, 5, wx.GROW)

        self.parent_sizer = wx.BoxSizer(wx.VERTICAL)
        self.parent_sizer.Add(self.topbar_sizer, 1, wx.GROW)
        self.parent_sizer.Add(self.vertical_sizer, 20, wx.GROW)

        self.SetSizer(self.parent_sizer)
        self.Show()

        return [self.start_stop_buttons, self.plot_canvas, self.plot_selector]

    def update_subplots(self, subplots):
        self.plot_canvas.update_subplots(subplots)

    def _init_timer(self, parent):
        self.redrawPeriod = 100
        self.redrawTimer = wx.Timer(parent)
        parent.Bind(wx.EVT_TIMER, self._onRedrawTimer, self.redrawTimer)

    def startTimer(self):
        self.redrawTimer.Start(self.redrawPeriod)

    def stop_timer(self):
        self.redrawTimer.Stop()

    def _onRedrawTimer(self, event):
        try:
            self.draw_plot_canvas()
        except RuntimeError as e:
            print e


