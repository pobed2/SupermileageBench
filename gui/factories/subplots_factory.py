from gui.data_plotting.plot_types.real_time_plots import PositionRealTimePlot, VelocityRealTimePlot, AccelerationRealTimePlot, TorqueRealTimePlot

class SubplotFactory(object):
    def __init__(self):
        pass

    def create_subplots(self, list_of_names):
        subplots = []
        number_of_plots = len(list_of_names)
        for order, name in enumerate(list_of_names):
            plot = self.create_subplot(name, order, number_of_plots)
            subplots.append(plot)
        return subplots

    def create_subplot(self, name, order, number_of_plots):
        if name == "Position":
            return PositionRealTimePlot(order, number_of_plots)
        elif name == "Vitesse":
            return VelocityRealTimePlot(order, number_of_plots)
        elif name == "Acceleration":
            return AccelerationRealTimePlot(order, number_of_plots)
        elif name == "Torque":
            return TorqueRealTimePlot(order, number_of_plots)
