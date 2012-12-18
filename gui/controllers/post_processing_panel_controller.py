from gui.windows.post_processing_panel import PostProcessingPanel

class PostProcessingPanelController(object):
    def __init__(self, sub_data_plots, filenames_to_compare_to):
        self.sub_data_plots = sub_data_plots
        self.filenames_to_compare_to = filenames_to_compare_to

    def create_panel(self, frame):
        self.panel = PostProcessingPanel(frame, self.sub_data_plots, self.filenames_to_compare_to)
        self.panel.draw_plot_canvas()