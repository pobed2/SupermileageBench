from gui.data_plotting.data_plot import DataPlot

class PostProcessingDataPlot(DataPlot):
    def __init__(self, data_repository, dropbox_repository, subplot_code='111',
                 bg_color='black', title='', x_label='', y_label='', linewidth=1, color=(1, 1, 1)):
        super(PostProcessingDataPlot, self).__init__(data_repository, subplot_code, bg_color, title, x_label, y_label,
            linewidth, color)

        self.dropbox_repository = dropbox_repository

    def initialize_figure(self, figure):
        super(PostProcessingDataPlot, self).initialize_figure(figure)

        self.dropbox_lines = []

        for data_file in self.dropbox_repository.get_x_data():
            self.dropbox_lines.append(
                self.subplot.plot(
                    [],
                    linewidth=self.linewidth,
                    color=self.color,
                )[0]
            )

    def prepare_plot_for_draw(self):
        self.data_repository.refresh_database()
        super(PostProcessingDataPlot, self).prepare_plot_for_draw()

    def _calculate_x_axis_bounds(self):
        x_min = 0
        x_max = self.data_repository.get_max_x_data()
        return x_min, x_max

    def _set_data(self):
        self.data_plot.set_data(self.data_repository.get_x_data(), self.data_repository.get_y_data())

        for i in range(len(self.dropbox_lines)):
            self.dropbox_lines[i].set_data(self.dropbox_repository.get_x_data()[i],
                self.dropbox_repository.get_y_data()[i])