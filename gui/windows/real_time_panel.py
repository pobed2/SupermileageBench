import wx

from gui.windows.bench_panel import BenchPanel

class RealTimePanel(BenchPanel):
    def __init__(self, parent, sub_data_plots, filenames_to_compare_to):
        super(RealTimePanel, self).__init__(parent, sub_data_plots, filenames_to_compare_to)
        self._init_timer(parent)

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


