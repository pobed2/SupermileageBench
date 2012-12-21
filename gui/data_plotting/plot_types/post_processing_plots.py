from data_access.dropbox_repositories import TorqueDropboxRepository, PowerDropboxRepository
from data_access.post_processing_repositories import PowerPostProcessingRepository, TorquePostProcessingRepository
from gui.data_plotting.post_processing_data_plot import PostProcessingDataPlot


class TorquePostProcessingPlot(PostProcessingDataPlot):
    def __init__(self):
        self.data_repository = TorquePostProcessingRepository()
        self.dropbox_repository = TorqueDropboxRepository()
        super(TorquePostProcessingPlot, self).__init__(self.data_repository, self.dropbox_repository,
            subplot_code='211',
            title='Torque', x_label='RPM', y_label='Torque')


class PowerPostProcessingPlot(PostProcessingDataPlot):
    def __init__(self):
        self.data_repository = PowerPostProcessingRepository()
        self.dropbox_repository = PowerDropboxRepository()
        super(PowerPostProcessingPlot, self).__init__(self.data_repository, self.dropbox_repository, subplot_code='212',
            title='Puissance', x_label='RPM', y_label='Joules?')