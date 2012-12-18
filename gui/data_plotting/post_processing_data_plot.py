from gui.data_plotting.data_plot import DataPlot

class PostProcessingDataPlot(DataPlot):
    def __init__(self, data_repository, dropbox_repository, subplot_code='111',
                 bg_color='black', title='', x_label='', y_label='', linewidth=1, color=(1, 1, 1)):
        super(PostProcessingDataPlot, self).__init__(data_repository, subplot_code, bg_color, title, x_label, y_label,
            linewidth, color)
        self.dropbox_repository = dropbox_repository

    def prepare_plot_for_draw(self):
        self.data_repository.refresh_database()
        #self.dropbox_repository.refresh_database()
        self._add_dropbox_lines()

        super(PostProcessingDataPlot, self).prepare_plot_for_draw()

    def _add_dropbox_lines(self):
        self.dropbox_lines = []
        number_of_lines = len(self.dropbox_repository.get_x_data())
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
        super(PostProcessingDataPlot, self)._set_data()

        x_datas = self.dropbox_repository.get_x_data()
        y_datas = self.dropbox_repository.get_y_data()

        for i in range(len(self.dropbox_lines)):
            self.dropbox_lines[i].set_data(x_datas[i], y_datas[i])