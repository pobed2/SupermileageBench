#coding: utf-8

from gui.data_plotting.post_processing_plots import TorquePostProcessingPlot, PowerPostProcessingPlot
from gui.data_plotting.real_time_plots import PositionRealTimePlot, VelocityRealTimePlot, AccelerationRealTimePlot, TorqueRealTimePlot

class SubplotFactory(object):
    '''
    Base class for subplot factories
    '''

    def create_subplots(self, list_of_names):
        subplots = []
        number_of_plots = len(list_of_names)
        for order, name in enumerate(list_of_names):
            plot = self.create_subplot(name, order, number_of_plots)
            subplots.append(plot)
        return subplots


class RealTimeSubplotFactory(SubplotFactory):
    def create_subplot(self, name, order, number_of_plots):
        if name == u"Position":
            return PositionRealTimePlot(order, number_of_plots)
        elif name == u"Vitesse":
            return VelocityRealTimePlot(order, number_of_plots)
        elif name == u"Accélération":
            return AccelerationRealTimePlot(order, number_of_plots)
        elif name == u"Torque":
            return TorqueRealTimePlot(order, number_of_plots)


class PostProcessingSubplotFactory(SubplotFactory):
    def create_subplot(self, name, order, number_of_plots):
        if name == u"Torque":
            return TorquePostProcessingPlot(order, number_of_plots)
        elif name == u"Puissance":
            return PowerPostProcessingPlot(order, number_of_plots)