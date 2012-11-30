from supermileagebench.filter_testing.filter_testing_panel import *

class FilterTestingPanelController(object):
    def __init__(self, sub_data_plots, testing_controller):
        self.sub_data_plots = sub_data_plots
        self.testing_controller = testing_controller

    def create_panel(self, frame):
        self.panel = FilterTestingPanel(self.testing_controller, self.sub_data_plots, frame)
        self.panel.drawPlot()

    def redraw_plots(self):
        self.panel.drawPlot()