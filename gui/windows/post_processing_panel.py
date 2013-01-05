import wx
from gui.custom_widgets.plot_selection.plot_selector import PlotSelector
from gui.custom_widgets.reset_topbar import ResetTopbar

from gui.windows.bench_panel import BenchPanel
from gui.custom_widgets.constants_sidebar import ConstantsSidebar
from gui.custom_widgets.dropbox_files_sidebar import DropboxFilesSidebar
from gui.custom_widgets.plot_canvas import PlotCanvas

class PostProcessingPanel(BenchPanel):
    def __init__(self, parent, sub_data_plots, filenames_to_compare_to):
        super(PostProcessingPanel, self).__init__(parent)
        self.widgets = self._init_widgets(sub_data_plots, filenames_to_compare_to)

    def _init_widgets(self, sub_data_plots, filenames_to_compare_to):
        self.listBox1 = DropboxFilesSidebar(self, filenames_to_compare_to)
        self.constants_sidebar = ConstantsSidebar(self)
        self.plot_canvas = PlotCanvas(self, sub_data_plots)
        self.reset_topbar = ResetTopbar(self)
        self.plot_selector = PlotSelector(self, ["Torque", "Puissance"])

        self.topbar_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.topbar_sizer.Add(self.reset_topbar, 2, wx.GROW)
        self.topbar_sizer.Add(self.plot_selector, 1, wx.GROW)

        self.vertical_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.vertical_sizer.Add(self.listBox1, 1, wx.GROW)
        self.vertical_sizer.Add(self.plot_canvas, 5, wx.GROW)
        self.vertical_sizer.Add(self.constants_sidebar, 1, wx.GROW)

        self.panel_sizer = wx.BoxSizer(wx.VERTICAL)
        self.panel_sizer.Add(self.topbar_sizer, 1, wx.GROW)
        self.panel_sizer.Add(self.vertical_sizer, 20, wx.GROW)

        self.SetSizer(self.panel_sizer)
        self.Show()

        return [self.listBox1, self.plot_selector, self.constants_sidebar, self.plot_canvas, self.reset_topbar]

    def update_subplots(self, subplots):
        self.plot_canvas.update_subplots(subplots)

    def refresh_canvas(self):
        self.plot_canvas.draw()