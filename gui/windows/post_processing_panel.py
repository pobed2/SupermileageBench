import wx
from gui.custom_widgets.plot_selection.plot_selector import PlotSelector
from gui.custom_widgets.reset_topbar import ResetTopbar

from gui.windows.bench_panel import BenchPanel
from gui.custom_widgets.dropbox_files_sidebar import DropboxFilesSidebar
from gui.custom_widgets.plot_canvas import PlotCanvas
from configuration.app_settings import post_processing_plot_types

class PostProcessingPanel(BenchPanel):
    def __init__(self, parent, sub_data_plots, filenames_to_compare_to, subplots_names):
        super(PostProcessingPanel, self).__init__(parent)
        self.widgets = self._init_widgets(sub_data_plots, filenames_to_compare_to, subplots_names)

    def _init_widgets(self, sub_data_plots, filenames_to_compare_to, subplots_names):
        self.listBox1 = DropboxFilesSidebar(self, filenames_to_compare_to)
        self.plot_canvas = PlotCanvas(self, sub_data_plots)
        self.reset_topbar = ResetTopbar(self)
        self.plot_selector = PlotSelector(self, post_processing_plot_types, subplots_names)

        self.topbar_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.topbar_sizer.Add(self.reset_topbar, 2, wx.GROW)
        self.topbar_sizer.Add(self.plot_selector, 1, wx.GROW)

        self.vertical_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.vertical_sizer.Add(self.listBox1, 1, wx.GROW)
        self.vertical_sizer.Add(self.plot_canvas, 5, wx.GROW)

        self.panel_sizer = wx.BoxSizer(wx.VERTICAL)
        self.panel_sizer.Add(self.topbar_sizer, 1, wx.GROW)
        self.panel_sizer.Add(self.vertical_sizer, 20, wx.GROW)

        self.SetSizer(self.panel_sizer)
        self.Show()

        return [self.listBox1, self.plot_selector, self.plot_canvas, self.reset_topbar]

    def update_subplots(self, subplots):
        self.plot_canvas.update_subplots(subplots)
        self.refresh_canvas()

    def refresh_canvas(self):
        self.plot_canvas.draw()