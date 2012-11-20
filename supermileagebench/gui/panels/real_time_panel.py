import wx

from supermileagebench.gui.panels.bench_panel import BenchPanel

class RealTimePanel(BenchPanel):

    def __init__(self, sub_data_plots, parent):
        super(RealTimePanel, self).__init__(sub_data_plots, parent)
        self.parent = parent
        self._init_timer()

    def _init_timer(self):
        self.redrawPeriod = 100
        self.redrawTimer = wx.Timer(self.parent)
        self.parent.Bind(wx.EVT_TIMER, self._onRedrawTimer, self.redrawTimer)

    def startTimer(self):
        self.redrawTimer.Start(self.redrawPeriod)

    def stop_timer(self):
        self.redrawTimer.Stop()

    def _onRedrawTimer(self, event):
        try:
            self.drawPlot()
        except RuntimeError as e:
            print e


