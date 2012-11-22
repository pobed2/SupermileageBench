from supermileagebench.gui.data_plotting.data_plot import DataPlot

class RealTimeDataPlot(DataPlot):
    def __init__(self, data_repository, subplot_code='111', x_data_range_to_display=25, x_data_before_end=5,
                 bg_color='black', title='', x_label='', y_label='', linewidth=1, color=(1, 1, 1)):
        super(RealTimeDataPlot, self).__init__(data_repository, subplot_code, bg_color, title, x_label, y_label,
            linewidth, color)
        self.x_data_range_to_display = x_data_range_to_display
        self.x_data_before_end = x_data_before_end

    def _calculate_x_axis_bounds(self):
        x_data_max = self.data_repository.get_max_x_data()

        gap = max(x_data_max, self.x_data_range_to_display)
        x_max = gap + self.x_data_before_end
        x_min = gap - self.x_data_range_to_display

        return x_min, x_max