from databases.database import Database
from databases.dropbox_database import DropboxDatabase
from databases.post_processing_database import PostProcessingDatabase
from dropbox_actions.dropbox_downloader import DropboxDownloader
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
        self.database = Database()
        self.post_processing_database = PostProcessingDatabase(self.database)
        self.dropbox_database = DropboxDatabase()
        self.dropbox_downloader = DropboxDownloader()
        filenames_to_compare_to = self.dropbox_downloader.fetch_names_of_comparable_files()

        self.real_time_subplots = self._init_real_time_subplots()
        self.post_treatment_subplots = self._init_post_processing_subplots()

        self._init_encoder_controller()
        self.top_frame_controller = TopFrameController(self.real_time_subplots, self.post_treatment_subplots,
            filenames_to_compare_to, self.encoder_controller, self)

        return True

    def _init_encoder_controller(self):
        self.encoder_controller = EncoderController(self.database)

    def _init_real_time_subplots(self):
        subplots = []

        position_repository = PositionRealTimeRepository(self.database)
        velocity_repository = VelocityRealTimeRepository(self.database)
        acceleration_repository = AccelerationRealTimeRepository(self.database)
        torque_repository = TorqueRealTimeRepository(self.database)

        #Add subplots here
        positionPlot = RealTimeDataPlot(position_repository, subplot_code=(221), title='Position')
        velocityPlot = RealTimeDataPlot(velocity_repository, subplot_code=(222), title='Velocity')
        accelerationPlot = RealTimeDataPlot(acceleration_repository, subplot_code=(223), title='Acceleration',
            x_label='Time (s)'
            , y_label='Acceleration (radians / seconds^2)')
        torquePlot = RealTimeDataPlot(torque_repository, subplot_code=(224), title='Torque', x_label='Time (s)'
            , y_label='Torque')

        subplots.append(accelerationPlot)
        subplots.append(torquePlot)
        subplots.append(positionPlot)
        subplots.append(velocityPlot)

        return subplots

    def _init_post_processing_subplots(self):
        subplots = []

        torque_repository = TorquePostProcessingRepository(self.post_processing_database)
        power_repository = PowerPostProcessingRepository(self.post_processing_database)

        dropbox_torque_repository = TorquePostProcessingRepository(self.dropbox_database)
        dropbox_power_repository = PowerPostProcessingRepository(self.dropbox_database)

        #Add subplots here
        torquePlot = PostProcessingDataPlot(torque_repository, dropbox_torque_repository, subplot_code=(211),
            title='Torque', x_label='RPM', y_label='Torque')

        powerPlot = PostProcessingDataPlot(power_repository, dropbox_power_repository, subplot_code=(212),
            title='Power', x_label='RPM', y_label='Joules?')

        subplots.append(torquePlot)
        subplots.append(powerPlot)

        return subplots

    def save_data_to_dropbox(self):
        directory_name = (str(datetime.now().replace(microsecond=0)))

        self.post_processing_database.refresh()
        post_processing_data_string = self.post_processing_database.serialize_data_as_csv()
        real_time_data_string = self.database.serialize_data_as_csv()

        saver = DropboxSaver()
        saver.save_data_to_dropbox(directory_name, self.REAL_TIME_FILENAME, real_time_data_string)
        saver.save_data_to_dropbox(directory_name, self.POST_PROCESSING_FILENAME, post_processing_data_string)

