from gui.windows.post_processing_panel import PostProcessingPanel

class PostProcessingPanelController(object):
    def __init__(self, sub_data_plots):
        self.sub_data_plots = sub_data_plots

    def create_panel(self, frame):
        self.panel = PostProcessingPanel(self.sub_data_plots, frame)
        self.panel.draw_plot_canvas()