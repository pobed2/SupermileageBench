from supermileagebench.gui.windows.post_treatment_panel import PostTreatmentPanel

class PostTreatmentPanelController(object):
    def __init__(self, sub_data_plots):
        self.sub_data_plots = sub_data_plots

    def create_panel(self, frame):
        self.panel = PostTreatmentPanel(self.sub_data_plots, frame)
        self.panel.drawPlot()