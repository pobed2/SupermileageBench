from gui.windows.bench_panel import *

class FilterTestingPanel(BenchPanel):
    def __init__(self, controller, sub_data_plots, parent, width=1280, height=520, dpi=100):
        self.controller = controller
        super(FilterTestingPanel, self).__init__(sub_data_plots, parent, width, height, dpi)

    def _init_plots(self, width, height, dpi):
        self.fig = Figure((width / dpi, height / dpi), dpi=dpi)
        self.canvas = FigCanvas(self.panel, -1, self.fig)

        self.slider_panel = wx.Panel(self.panel, -1)

        wx.StaticText(self.slider_panel, label='Derivative Interval', pos=(40, 5))
        self.spin1 = wx.SpinCtrl(self.slider_panel, value='100', pos=(40, 20), size=(60, -1))
        self.spin1.SetRange(1, 500)

        wx.StaticText(self.slider_panel, label='Filter Order', pos=(200, 5))
        self.spin2 = wx.SpinCtrl(self.slider_panel, value='1', pos=(200, 20), size=(60, -1))
        self.spin2.SetRange(1, 15)

        wx.StaticText(self.slider_panel, label='Filter Window', pos=(400, 5))
        self.spin3 = wx.SpinCtrl(self.slider_panel, value='111', pos=(400, 20), size=(60, -1))
        self.spin3.SetRange(1, 401)

        btn = wx.Button(self.slider_panel, label='Compute', pos=(600, 20))
        btn.Bind(wx.EVT_BUTTON, self.OnCalculateNewFilter)

        for plot in self.sub_data_plots:
            plot.initialize_figure(self.fig)

        self.graphBox = wx.BoxSizer(wx.VERTICAL)
        self.graphBox.Add(self.slider_panel, 1, flag=wx.LEFT | wx.TOP | wx.GROW)
        self.graphBox.Add(self.canvas, 10, flag=wx.LEFT | wx.TOP | wx.GROW)

        self.panel.SetSizer(self.graphBox)
        self.panel.Show()

    def OnCalculateNewFilter(self, event):
        derivative_value = self.spin1.GetValue()
        filter_order = self.spin2.GetValue()
        filter_window = self.spin3.GetValue()
        self.controller.calculate_new_filter(derivative_value, filter_order, filter_window)

