# coding: utf-8

from data_access.real_time_repositories import PositionRealTimeRepository, VelocityRealTimeRepository, TorqueRealTimeRepository, AccelerationRealTimeRepository
from gui.data_plotting.real_time_data_plot import RealTimeDataPlot

class PositionRealTimePlot(RealTimeDataPlot):
    def __init__(self):
        self.data_repository = PositionRealTimeRepository()
        super(PositionRealTimePlot, self).__init__(self.data_repository, subplot_code='221', title=u'Position',
            x_label='Temps (s)'
            , y_label='Position (rad)')


class VelocityRealTimePlot(RealTimeDataPlot):
    def __init__(self):
        self.data_repository = VelocityRealTimeRepository()
        super(VelocityRealTimePlot, self).__init__(self.data_repository, subplot_code='222', title=u'Vitesse',
            x_label='Temps (s)'
            , y_label='Vitesse (rad / s)')


class AccelerationRealTimePlot(RealTimeDataPlot):
    def __init__(self):
        self.data_repository = AccelerationRealTimeRepository()
        super(AccelerationRealTimePlot, self).__init__(self.data_repository, subplot_code='223', title=u'Accélération',
            x_label='Temps (s)'
            , y_label=u'Accélération (rad / s\xb2)')


class TorqueRealTimePlot(RealTimeDataPlot):
    def __init__(self):
        self.data_repository = TorqueRealTimeRepository()
        super(TorqueRealTimePlot, self).__init__(self.data_repository, subplot_code='224', title=u'Torque',
            x_label='Temps (s)', y_label='Torque')