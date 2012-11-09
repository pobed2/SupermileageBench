class DataPlot(object):

    def __init__(self, data_repository, figure, subplot_code = '111', bg_color = 'black', title = '',
                 x_label = '', y_label = '', linewidth = 1, color = (1,1,1)):

        self.data_repository = data_repository

        self.subplot = figure.add_subplot(subplot_code)
        self.subplot.set_axis_bgcolor(bg_color)
        self.subplot.set_title(title, size=12)
        self.subplot.set_xlabel(x_label, size=10)
        self.subplot.set_ylabel(y_label, size=10)
        self.data_plot = self.subplot.plot(
            [],
            linewidth=linewidth,
            color=color,
        )[0]

    def prepare_plot_for_draw(self):
        self._set_data()
        self._set_axis_bounds()

    def _set_data(self):
        self.data_plot.set_data(self.data_repository.get_time_data(), self.data_repository.get_plotting_data())

    def _set_axis_bounds(self):
        x_min, x_max = self._calculate_x_axis_bounds()
        y_min, y_max = self._calculate_y_axis_bounds()
        self.subplot.set_xbound(lower=x_min, upper=x_max)
        self.subplot.set_ybound(lower=y_min, upper=y_max)

    def _calculate_x_axis_bounds(self):
        time_max = self.data_repository.get_max_time()

        gap = max(time_max, self.time_to_display)
        x_max = gap + self.timeBeforeEnd
        x_min = gap - self.timeToDisplay

        return x_min, x_max

    def _calculate_y_axis_bounds(self):
        data_max = self.data_repository.get_max_data()
        data_min = self.data_repository.get_min_data()

        y_min = round(data_min, 0) - (0.1 * abs(round(data_min, 0)))
        y_max = round(data_max, 0) + (0.1 * round(data_max, 0))

        return y_min, y_max

class position_plot(DataPlot):
    pass

class velocity_plot(DataPlot):
    pass

class acceleration_plot(DataPlot):
    pass

class torque_plot(DataPlot):
    pass

