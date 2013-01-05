# coding: utf-8

from data_access.real_time_repositories import PositionRealTimeRepository, VelocityRealTimeRepository, TorqueRealTimeRepository, AccelerationRealTimeRepository
from gui.data_plotting.data_plot import DataPlot

class RealTimePlot(DataPlot):
    '''
    Base class for real time plots.
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


class PositionRealTimePlot(RealTimePlot):
    def __init__(self, order=0, number_of_plots=4):
        self.data_repository = PositionRealTimeRepository()
        super(PositionRealTimePlot, self).__init__(self.data_repository,
            subplot_code=self._calculate_subplot_code(order, number_of_plots)
            , title=u'Position',
            x_label=u'Temps (s)',
            y_label=u'Position (rad)')


class VelocityRealTimePlot(RealTimePlot):
    def __init__(self, order=1, number_of_plots=4):
        self.data_repository = VelocityRealTimeRepository()
        super(VelocityRealTimePlot, self).__init__(self.data_repository,
            subplot_code=self._calculate_subplot_code(order, number_of_plots)
            , title=u'Vitesse',
            x_label=u'Temps (s)'
            , y_label=u'Vitesse (rad / s)')


class AccelerationRealTimePlot(RealTimePlot):
    def __init__(self, order=2, number_of_plots=4):
        self.data_repository = AccelerationRealTimeRepository()
        super(AccelerationRealTimePlot, self).__init__(self.data_repository,
            subplot_code=self._calculate_subplot_code(order, number_of_plots),
            title=u'Accélération',
            x_label=u'Temps (s)'
            , y_label=u'Accélération (rad / s\xb2)')


class TorqueRealTimePlot(RealTimePlot):
    def __init__(self, order=3, number_of_plots=4):
        self.data_repository = TorqueRealTimeRepository()
        super(TorqueRealTimePlot, self).__init__(self.data_repository,
            subplot_code=self._calculate_subplot_code(order, number_of_plots)
            , title=u'Torque',
            x_label=u'Temps (s)',
            y_label=u'Torque')