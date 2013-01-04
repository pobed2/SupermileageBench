from gui.data_plotting.data_plot import DataPlot
from math import ceil, sqrt

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

    def _calculate_subplot_code(self, order, number_of_plots):
        nb_rows = self._calculate_number_of_subplot_rows(number_of_plots)
        nb_colums = self._calculate_number_of_subplot_colums(nb_rows, number_of_plots)
        placement = str(order + 1)
        print str(nb_rows) + str(nb_colums) + placement
        return  str(nb_rows) + str(nb_colums) + placement

    def _calculate_number_of_subplot_rows(self, number_of_plots):
        return int(ceil(sqrt(number_of_plots)))

    def _calculate_number_of_subplot_colums(self, nb_rows, nb_plots):
        nb_colums = 1
        while nb_colums * nb_rows < nb_plots:
            nb_colums += 1

        return nb_colums