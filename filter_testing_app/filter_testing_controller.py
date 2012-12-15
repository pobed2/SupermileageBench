from data_access.post_processing_repositories import *
from data_access.real_time_repositories import *
from gui.data_plotting.post_processing_data_plot import *
from filter_testing.filter_testing_database import *
from filter_testing.filter_testing_frame import *
from filter_testing.filter_testing_plot import *
from filter_testing.filter_testing_panel_controller import *
from filter_testing.unfiltered_repositories import *
from data.post_processing_database import *


class FilterTestingController(object):
    def __init__(self):
        self.DERIVATIVE_INTERVAL = 100
        self.FILTER_ORDER = 1
        self.FILTER_WINDOW = 111
        self.time, self.positions = np.loadtxt(
            "/Users/MacBook/Dropbox/SupermileageBench/2012-11-27 15:23:05/RealTime.csv", skiprows=1, usecols=(0, 1),
            delimiter=',', unpack=True)
        self.database = FilterTestingDatabase(self.time, self.positions, derivative_interval=self.DERIVATIVE_INTERVAL,
            filter_order=self.FILTER_ORDER, filter_window=self.FILTER_WINDOW)

        #        outfile = open('data.pkl', 'wb')
        #        pickle.dump(zip(tuple(time.tolist()), tuple(positions.tolist())), outfile)
        #        outfile.close()


        self.post_processing_database = PostProcessingDatabase(self.database)
        self.subplots = self._init_post_treatment_subplots()

        self.filter_testing_controller = FilterTestingPanelController(self.subplots, self)
        self.frame = FilterTestingFrame()
        self.filter_testing_controller.create_panel(self.frame)

        self.frame.Show(True)
        self.frame.Centre()

    def _init_post_treatment_subplots(self):
        subplots = []

        velocity_repository = VelocityRealTimeRepository(self.database)
        acceleration_repository = AccelerationRealTimeRepository(self.database)

        unfiltered_velocity_repository = UnfilteredVelocityRepository(self.database)
        unfiltered_acceleration_repository = UnfilteredAccelerationRepository(self.database)

        torque_repository = TorquePostProcessingRepository(self.post_processing_database)
        power_repository = PowerPostProcessingRepository(self.post_processing_database)


        #Add subplots here
        velocityPlot = FilterTestingPlot(unfiltered_velocity_repository, velocity_repository, subplot_code=(221),
            title='Velocity')
        accelerationPlot = FilterTestingPlot(unfiltered_acceleration_repository, acceleration_repository,
            subplot_code=(223), title='Acceleration')

        torquePlot = PostProcessingDataPlot(torque_repository, subplot_code=(224), title='Torque')
        powerPlot = PostProcessingDataPlot(power_repository, subplot_code=(222), title='Power')

        subplots.append(velocityPlot)
        subplots.append(accelerationPlot)
        subplots.append(torquePlot)
        subplots.append(powerPlot)
        return subplots

    def OnDerivativeIntervalScroll(self, value):
        self.DERIVATIVE_INTERVAL = value
        self._redraw_plots()

    def OnFilterOrderScroll(self, value):
        self.FILTER_ORDER = value
        self._redraw_plots()

    def OnFilterWindowScroll(self, value):
        if value % 2 == 0:
            value += 1

        self.FILTER_WINDOW = value
        self._redraw_plots()

    def calculate_new_filter(self, derivative_interval, filter_order, filter_window):
        self._redraw_plots(derivative_interval, filter_order, filter_window)

    def _redraw_plots(self, derivative_interval, filter_order, filter_window):
        fw = filter_window
        if filter_window % 2 == 0:
            fw += 1

        self.DERIVATIVE_INTERVAL = derivative_interval
        self.FILTER_ORDER = filter_order
        self.FILTER_WINDOW = fw

        self.database.reset_time_and_positions(self.time, self.positions, derivative_interval=self.DERIVATIVE_INTERVAL,
            filter_order=self.FILTER_ORDER, filter_window=self.FILTER_WINDOW)
        self.filter_testing_controller.redraw_plots()