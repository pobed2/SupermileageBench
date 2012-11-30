from supermileagebench.gui.data_plotting.data_plot import *

class FilterTestingPlot(DataPlot):
    def __init__(self, data_repository, second_data_repository, subplot_code='111',
                 bg_color='black', title='', x_label='', y_label='', linewidth=1, color=(1, 1, 1)):
        self.data_repository = data_repository
        self.second_data_repository = second_data_repository
        self.subplot_code = subplot_code
        self.bg_color = bg_color
        self.title = title
        self.x_label = x_label
        self.y_label = y_label
        self.linewidth = linewidth
        self.color = color

    def initialize_figure(self, figure):
        self.subplot = figure.add_subplot(self.subplot_code)
        self.subplot.set_axis_bgcolor(self.bg_color)
        self.subplot.set_title(self.title, size=12)
        self.subplot.set_xlabel(self.x_label, size=10)
        self.subplot.set_ylabel(self.y_label, size=10)
        self.data_plot = self.subplot.plot(
            [],
            linewidth=self.linewidth,
            color=self.color,
        )[0]

        self.second_data_plot = self.subplot.plot(
            [],
            linewidth=self.linewidth * 2,
            color=(0, 1, 0),
        )[0]

    def _set_data(self):
        self.data_plot.set_data(self.data_repository.get_x_data(), self.data_repository.get_y_data())
        self.second_data_plot.set_data(self.second_data_repository.get_x_data(),
            self.second_data_repository.get_y_data())

    def _calculate_x_axis_bounds(self):
        x_min = 0
        x_max = self.data_repository.get_max_x_data()
        return x_min, x_max