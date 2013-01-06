#coding: utf-8

from configuration.properties_parser import PropertiesParser
from databases.dropbox_database import DropboxDatabase
from databases.post_processing_database import PostProcessingDatabase
from databases.real_time_database import RealTimeDatabase
from gui.factories.subplots_factories import RealTimeSubplotFactory, PostProcessingSubplotFactory
from phidget.encoder_controller import EncoderController
from gui.controllers.top_frame_controller import TopFrameController
from datetime import datetime
from dropbox_actions.dropbox_saver import  DropboxSaver

class AppController(object):
    def __init__(self):
        self._initializeApp()
        self.REAL_TIME_FILENAME = "RealTime.csv"
        self.POST_PROCESSING_FILENAME = "PostProcessing.csv"

    def reset_app(self):
        self.top_frame_controller.close_frame()
        self._initializeApp()

    def _initializeApp(self):
        self.database = RealTimeDatabase()
        self.database.initialize_database()
        self.post_processing_database = PostProcessingDatabase()
        self.dropbox_database = DropboxDatabase()
        self.dropbox_database.initialize_database()
        self.properties_parser = PropertiesParser()

        self.real_time_subplots = self._init_real_time_subplots()
        self.post_treatment_subplots = self._init_post_processing_subplots()

        self._init_encoder_controller()
        self.top_frame_controller = TopFrameController(self.real_time_subplots, self.post_treatment_subplots, self)

        return True

    def _init_encoder_controller(self):
        self.encoder_controller = EncoderController(self.database)

    def _init_real_time_subplots(self):
        plots_to_display = self.properties_parser.get_property("Real-Time Plots")

        if plots_to_display is "":
            plots_to_display = [u"Position", u"Vitesse", u"Accélération", u"Torque"]

        factory = RealTimeSubplotFactory()
        return factory.create_subplots(plots_to_display)

    def _init_post_processing_subplots(self):
        plots_to_display = self.properties_parser.get_property("Post-Processing Plots")

        if plots_to_display is "":
            plots_to_display = [u"Torque", u"Puissance"]

        factory = PostProcessingSubplotFactory()
        return factory.create_subplots(plots_to_display)

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

