# coding: utf-8

from data_access.timewise_repositories import PositionRadiansTimewiseRepository, SpeedRadiansTimewiseRepository, TorqueTimewiseRepository, AccelerationTimewiseRepository
from gui.data_plotting.data_plot import DataPlot

class TimewisePlot(DataPlot):
    '''
    Base class for plots that are function of time.
    '''

    def __init__(self, data_repository, subplot_code='111', x_data_range_to_display=25, x_data_before_end=5,
                 bg_color='black', title='', x_label='', y_label='', linewidth=1, color=(1, 1, 1)):
        super(TimewisePlot, self).__init__(data_repository, subplot_code, bg_color, title, x_label, y_label,
            linewidth, color)
        self.x_data_range_to_display = x_data_range_to_display
        self.x_data_before_end = x_data_before_end

    def _calculate_x_axis_bounds(self):
        x_data_max = self.data_repository.get_max_x_data()

        gap = max(x_data_max, self.x_data_range_to_display)
        x_max = gap + self.x_data_before_end
        x_min = gap - self.x_data_range_to_display

        return x_min, x_max


class PositionRadiansTimewisePlot(TimewisePlot):
    def __init__(self, order=0, number_of_plots=4):
        self.data_repository = PositionRadiansTimewiseRepository()
        super(PositionRadiansTimewisePlot, self).__init__(self.data_repository,
            subplot_code=self._calculate_subplot_code(order, number_of_plots)
            , title=u'Position',
            x_label=u'Temps (s)',
            y_label=u'Position (rad)')


class PositionMetersTimewisePlot(TimewisePlot):
    def __init__(self, order=0, number_of_plots=4):
        self.data_repository = PositionRadiansTimewiseRepository()
        super(PositionMetersTimewisePlot, self).__init__(self.data_repository,
            subplot_code=self._calculate_subplot_code(order, number_of_plots)
            , title=u'Position',
            x_label=u'Temps (s)',
            y_label=u'Position (m)')


class SpeedRadiansTimewisePlot(TimewisePlot):
    def __init__(self, order=1, number_of_plots=4):
        self.data_repository = SpeedRadiansTimewiseRepository()
        super(SpeedRadiansTimewisePlot, self).__init__(self.data_repository,
            subplot_code=self._calculate_subplot_code(order, number_of_plots)
            , title=u'Vitesse',
            x_label=u'Temps (s)'
            , y_label=u'Vitesse (rad / s)')


class SpeedMetersTimewisePlot(TimewisePlot):
    def __init__(self, order=1, number_of_plots=4):
        self.data_repository = SpeedRadiansTimewiseRepository()
        super(SpeedRadiansTimewisePlot, self).__init__(self.data_repository,
            subplot_code=self._calculate_subplot_code(order, number_of_plots)
            , title=u'Vitesse',
            x_label=u'Temps (s)'
            , y_label=u'Vitesse (m / s)')


class AccelerationTimewisePlot(TimewisePlot):
    def __init__(self, order=2, number_of_plots=4):
        self.data_repository = AccelerationTimewiseRepository()
        super(AccelerationTimewisePlot, self).__init__(self.data_repository,
            subplot_code=self._calculate_subplot_code(order, number_of_plots),
            title=u'Accélération',
            x_label=u'Temps (s)'
            , y_label=u'Accélération (rad / s\xb2)')


class TorqueTimewisePlot(TimewisePlot):
    def __init__(self, order=3, number_of_plots=4):
        self.data_repository = TorqueTimewiseRepository()
        super(TorqueTimewisePlot, self).__init__(self.data_repository,
            subplot_code=self._calculate_subplot_code(order, number_of_plots)
            , title=u'Torque',
            x_label=u'Temps (s)',
            y_label=u'Torque (Nm)')