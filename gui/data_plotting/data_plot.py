class DataPlot(object):
    '''
    Base class for every type of plots
    Not to be used on its own
    '''

    def __init__(self, data_repository, subplot_code='111',
                 bg_color='black', title='', x_label='', y_label='', linewidth=1, color=(1, 1, 1)):
        self.data_repository = data_repository
        self.subplot_code = subplot_code
        self.bg_color = bg_color
        self.title = title
        self.x_label = x_label
        self.y_label = y_label
        self.linewidth = linewidth
        self.color = color

    def initialize_figure(self, figure):
        self.figure = figure
        return self._add_subplot()

    def refresh_subplots(self):
        self.subplot.clear()
        self._add_subplot()

    def _add_subplot(self):
        self.subplot = self.figure.add_subplot(self.subplot_code)
        self.subplot.set_axis_bgcolor(self.bg_color)
        self.subplot.set_title(self.title, size=12)
        self.subplot.set_xlabel(self.x_label, size=10)
        self.subplot.set_ylabel(self.y_label, size=10)
        self.subplot.grid(True, linestyle='-', color='0.75')
        self.data_plot = self.subplot.plot(
            [],
            linewidth=self.linewidth,
            color=self.color,
        )[0]

        return self.subplot

    def prepare_plot_for_draw(self):
        self._set_data()
        self._set_axis_bounds()

    def _set_data(self):
        self.data_plot.set_data(self.data_repository.get_x_data(), self.data_repository.get_y_data())

    def _set_axis_bounds(self):
        x_min, x_max = self._calculate_x_axis_bounds()
        y_min, y_max = self._calculate_y_axis_bounds()
        self.subplot.set_xbound(lower=x_min, upper=x_max)
        self.subplot.set_ybound(lower=y_min, upper=y_max)

    def _calculate_y_axis_bounds(self):
        data_max = self.data_repository.get_max_y_data()
        data_min = self.data_repository.get_min_y_data()

        y_min = round(data_min, 0) - (0.1 * abs(round(data_min, 0)))
        y_max = round(data_max, 0) + (0.1 * round(data_max, 0))

        return y_min, y_max