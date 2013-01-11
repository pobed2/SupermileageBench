#coding: utf-8

from data_access.dropbox_repositories import TorqueDropboxRepository, PowerDropboxRepository
from data_access.post_processing_repositories import PowerPostProcessingRepository, TorquePostProcessingRepository
from gui.data_plotting.plot_base_classes import  ComparablePlot


class TorqueRpmWiseComparablePlot(ComparablePlot):
    def __init__(self, order=0, number_of_plots=2):
        self.data_repository = TorquePostProcessingRepository()
        self.dropbox_repository = TorqueDropboxRepository()

        super(TorqueRpmWiseComparablePlot, self).__init__(self.data_repository, self.dropbox_repository,
            subplot_code=self._calculate_subplot_code(order, number_of_plots),
            title='Torque', x_label='RPM', y_label='Torque')


class PowerRpmWiseComparablePlot(ComparablePlot):
    def __init__(self, order=1, number_of_plots=2):
        self.data_repository = PowerPostProcessingRepository()
        self.dropbox_repository = PowerDropboxRepository()

        super(PowerRpmWiseComparablePlot, self).__init__(self.data_repository, self.dropbox_repository,
            subplot_code=self._calculate_subplot_code(order, number_of_plots),
            title='Puissance', x_label='RPM', y_label='Watts')