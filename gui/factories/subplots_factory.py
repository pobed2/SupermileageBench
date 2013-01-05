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
        if name == "Position":
            return PositionRealTimePlot(order, number_of_plots)
        elif name == "Vitesse":
            return VelocityRealTimePlot(order, number_of_plots)
        elif name == "Acceleration":
            return AccelerationRealTimePlot(order, number_of_plots)
        elif name == "Torque":
            return TorqueRealTimePlot(order, number_of_plots)


class PostProcessingSubplotFactory(SubplotFactory):
    def create_subplot(self, name, order, number_of_plots):
        if name == "Torque":
            return TorquePostProcessingPlot(order, number_of_plots)
        elif name == "Puissance":
            return PowerPostProcessingPlot(order, number_of_plots)