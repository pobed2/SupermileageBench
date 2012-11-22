from supermileagebench.gui.data_plotting.data_plot import DataPlot

class PostProcessingDataPlot(DataPlot):
    def __init__(self, data_repository, subplot_code='111', x_data_before_end=0,
                 bg_color='black', title='', x_label='', y_label='', linewidth=1, color=(1, 1, 1)):
        super(PostProcessingDataPlot, self).__init__(data_repository, subplot_code, 0,
            x_data_before_end, bg_color, title, x_label, y_label, linewidth, color)

    def _calculate_x_axis_bounds(self):
        x_min = 0
        x_max = self.data_repository.get_max_x_data()
        return x_min, x_max