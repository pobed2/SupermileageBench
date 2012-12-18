from data_access.dropbox_repositories import TorqueDropboxRepository, PowerDropboxRepository
from databases.dropbox_database import DropboxDatabase
from databases.real_time_database import RealTimeDatabase
from gui.data_plotting.real_time_data_plot import RealTimeDataPlot
from data_access.real_time_repositories import *
from phidget.encoder_controller import EncoderController
from gui.controllers.top_frame_controller import TopFrameController
from datetime import datetime
from dropbox_actions.dropbox_saver import  DropboxSaver
from data_access.post_processing_repositories import *
from gui.data_plotting.post_processing_data_plot import *

class AppController(object):
    def __init__(self):
        self._initializeApp()
        self.REAL_TIME_FILENAME = "RealTime.csv"
        self.POST_PROCESSING_FILENAME = "PostProcessing.csv"

    def _initializeApp(self):
        self.database = RealTimeDatabase()
        self.database.initialize_database()
        self.dropbox_database = DropboxDatabase()
        self.dropbox_database.initialize_database()

        self.real_time_subplots = self._init_real_time_subplots()
        self.post_treatment_subplots = self._init_post_processing_subplots()

        self._init_encoder_controller()
        self.top_frame_controller = TopFrameController(self.real_time_subplots, self.post_treatment_subplots, self)

        return True

    def _init_encoder_controller(self):
        self.encoder_controller = EncoderController(self.database)

    def _init_real_time_subplots(self):
        subplots = []

        position_repository = PositionRealTimeRepository()
        velocity_repository = VelocityRealTimeRepository()
        acceleration_repository = AccelerationRealTimeRepository()
        torque_repository = TorqueRealTimeRepository()

        #Add subplots here
        positionPlot = RealTimeDataPlot(position_repository, subplot_code=(221), title='Position')
        velocityPlot = RealTimeDataPlot(velocity_repository, subplot_code=(222), title='Vitesse')
        accelerationPlot = RealTimeDataPlot(acceleration_repository, subplot_code=(223), title='Acceleration',
            x_label='Temps (s)'
            , y_label='Acceleration (radians / secondes^2)')
        torquePlot = RealTimeDataPlot(torque_repository, subplot_code=(224), title='Torque', x_label='Temps (s)'
            , y_label='Torque')

        subplots.append(accelerationPlot)
        subplots.append(torquePlot)
        subplots.append(positionPlot)
        subplots.append(velocityPlot)

        return subplots

    def _init_post_processing_subplots(self):
        subplots = []

        torque_repository = TorquePostProcessingRepository()
        power_repository = PowerPostProcessingRepository()

        dropbox_torque_repository = TorqueDropboxRepository()
        dropbox_power_repository = PowerDropboxRepository()

        #Add subplots here
        torquePlot = PostProcessingDataPlot(torque_repository, dropbox_torque_repository, subplot_code=(211),
            title='Torque', x_label='RPM', y_label='Torque')

        powerPlot = PostProcessingDataPlot(power_repository, dropbox_power_repository, subplot_code=(212),
            title='Puissance', x_label='RPM', y_label='Joules?')

        subplots.append(torquePlot)
        subplots.append(powerPlot)

        return subplots

    def start_data_acquisition(self):
        self.encoder_controller.start_data_acquisition()

    def stop_data_acquisition(self, save):
        self.encoder_controller.stop_data_acquisition()
        if save:
            self.save_data_to_dropbox()
        self.top_frame_controller.create_post_processing_panel()

    def save_data_to_dropbox(self):
        directory_name = (str(datetime.now().replace(microsecond=0)))

        self.post_processing_database.refresh()
        post_processing_data_string = self.post_processing_database.serialize_data_as_csv()
        real_time_data_string = self.database.serialize_data_as_csv()

        saver = DropboxSaver()
        saver.save_data_to_dropbox(directory_name, self.REAL_TIME_FILENAME, real_time_data_string)
        saver.save_data_to_dropbox(directory_name, self.POST_PROCESSING_FILENAME, post_processing_data_string)

