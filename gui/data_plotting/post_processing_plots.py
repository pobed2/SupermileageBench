from data_access.dropbox_repositories import TorqueDropboxRepository, PowerDropboxRepository
from data_access.post_processing_repositories import PowerPostProcessingRepository, TorquePostProcessingRepository
from gui.data_plotting.data_plot import DataPlot

class PostProcessingDataPlot(DataPlot):
    '''
    Base class for post processing (offline) plots
    '''

    def __init__(self, data_repository, dropbox_repository, subplot_code='111',
                 bg_color='black', title='', x_label='', y_label='', linewidth=1, color=(1, 1, 1)):
        super(PostProcessingDataPlot, self).__init__(data_repository, subplot_code, bg_color, title, x_label, y_label,
            linewidth, color)
        self.dropbox_repository = dropbox_repository

    def prepare_plot_for_draw(self):
        self.refresh_subplots()
        self.data_repository.refresh_database()
        self._add_dropbox_lines()

        super(PostProcessingDataPlot, self).prepare_plot_for_draw()

    def _add_dropbox_lines(self):
        self.dropbox_lines = []
        number_of_lines = len(self.dropbox_repository.get_x_data())
        print number_of_lines
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


class TorquePostProcessingPlot(PostProcessingDataPlot):
    def __init__(self, order=0, number_of_plots=2):
        self.data_repository = TorquePostProcessingRepository()
        self.dropbox_repository = TorqueDropboxRepository()
        super(TorquePostProcessingPlot, self).__init__(self.data_repository, self.dropbox_repository,
            subplot_code=self._calculate_subplot_code(order, number_of_plots),
            title='Torque', x_label='RPM', y_label='Torque')


class PowerPostProcessingPlot(PostProcessingDataPlot):
    def __init__(self, order=1, number_of_plots=2):
        self.data_repository = PowerPostProcessingRepository()
        self.dropbox_repository = PowerDropboxRepository()
        super(PowerPostProcessingPlot, self).__init__(self.data_repository, self.dropbox_repository,
            subplot_code=self._calculate_subplot_code(order, number_of_plots),
            title='Puissance', x_label='RPM', y_label='Joules?')