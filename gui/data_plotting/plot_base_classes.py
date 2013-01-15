from math import ceil, floor, sqrt

class DataPlot(object):
    '''
    Base class for every type of plots
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

        y_min = floor(data_min) - (0.1 * abs(ceil(data_min)))
        y_max = ceil(data_max) + (0.1 * abs(ceil(data_max)))

        return y_min, y_max

    def _calculate_subplot_code(self, order, number_of_plots):
        nb_rows = self._calculate_number_of_subplot_rows(number_of_plots)
        nb_colums = self._calculate_number_of_subplot_colums(nb_rows, number_of_plots)
        placement = str(order + 1)
        return  str(nb_rows) + str(nb_colums) + placement

    def _calculate_number_of_subplot_rows(self, number_of_plots):
        return int(ceil(sqrt(number_of_plots)))

    def _calculate_number_of_subplot_colums(self, nb_rows, nb_plots):
        nb_colums = 1
        while nb_colums * nb_rows < nb_plots:
            nb_colums += 1

        return nb_colums


class RealTimePlot(DataPlot):
    '''
    Base class for plots that are displayed in real-time
    '''

    def __init__(self, data_repository, subplot_code='111', x_data_range_to_display=25, x_data_before_end=5,
                 bg_color='black', title='', x_label='', y_label='', linewidth=1, color=(1, 1, 1)):
        super(RealTimePlot, self).__init__(data_repository, subplot_code, bg_color, title, x_label, y_label,
            linewidth, color)
        self.x_data_range_to_display = x_data_range_to_display
        self.x_data_before_end = x_data_before_end

    def _calculate_x_axis_bounds(self):
        x_data_max = self.data_repository.get_max_x_data()

        gap = max(x_data_max, self.x_data_range_to_display)
        x_max = gap + self.x_data_before_end
        x_min = gap - self.x_data_range_to_display

        return x_min, x_max


class ComparablePlot(DataPlot):
    '''
    Base class for comparable plots
    '''

    def __init__(self, data_repository, dropbox_repository, subplot_code='111',
                 bg_color='black', title='', x_label='', y_label='', linewidth=1, color=(1, 1, 1)):
        super(ComparablePlot, self).__init__(data_repository, subplot_code, bg_color, title, x_label, y_label,
            linewidth, color)
        self.dropbox_repository = dropbox_repository

    def prepare_plot_for_draw(self):
        self.refresh_subplots()
        self.data_repository.refresh_database()
        self._add_dropbox_lines()

        super(ComparablePlot, self).prepare_plot_for_draw()

    def _add_dropbox_lines(self):
        self.dropbox_lines = []
        data = self.dropbox_repository.get_x_data()
        number_of_lines = len(data)
        print number_of_lines
        print data
        for _ in range(number_of_lines):
            self.dropbox_lines.append(
                self.subplot.plot(
                    [],
                    linewidth=self.linewidth,
                    color=(1, 0, 0),
                )[0]
            )

    def _calculate_x_axis_bounds(self):
        x_min = 0
        x_max = self.data_repository.get_max_x_data()
        return x_min, x_max

    def _set_data(self):
        super(ComparablePlot, self)._set_data()

        x_datas = self.dropbox_repository.get_x_data()
        y_datas = self.dropbox_repository.get_y_data()

        for i in range(len(self.dropbox_lines)):
            self.dropbox_lines[i].set_data(x_datas[i], y_datas[i])
