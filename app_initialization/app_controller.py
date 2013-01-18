#coding: utf-8
from configuration.app_settings import real_time_plots_property, post_processing_plots_property

from configuration.properties_parser import PropertiesParser
from databases.dropbox_database import DropboxDatabase
from databases.injection_table import InjectionTable
from databases.post_processing_database import PostProcessingDatabase
from databases.real_time_database import RealTimeDatabase
from gui.factories.subplots_factories import RealTimeSubplotFactory, PostProcessingSubplotFactory
from phidget.encoder_controller import EncoderController
from gui.controllers.top_frame_controller import TopFrameController
from datetime import datetime
from dropbox_actions.dropbox_saver import  DropboxSaver

class AppController(object):
    '''
    Used to initialize the application on startup.
    Also used as the top controller.
    '''

    def __init__(self):
        self._initializeApp()
        self.REAL_TIME_FILENAME = "RealTime.csv"
        self.POST_PROCESSING_FILENAME = "PostProcessing.csv"
        self.INJECTION_TABLE_FILENAME = "InjectionTable.csv"

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

        real_time_subplots = self._init_real_time_subplots()
        post_treatment_subplots = self._init_post_processing_subplots()

        self._init_encoder_controller()
        self.top_frame_controller = TopFrameController(real_time_subplots, post_treatment_subplots, self)

    def _init_encoder_controller(self):
        self.encoder_controller = EncoderController(self.database)

    def _init_real_time_subplots(self):
        return self._init_subplots(real_time_plots_property, RealTimeSubplotFactory())

    def _init_post_processing_subplots(self):
        return self._init_subplots(post_processing_plots_property, PostProcessingSubplotFactory())

    def _init_subplots(self, property, factory):
        plots_to_display = self.properties_parser.get_property(property)
        return factory.create_subplots(plots_to_display)

    def start_data_acquisition(self):
        self.encoder_controller.start_data_acquisition()

    def stop_data_acquisition(self, save):
        self.encoder_controller.stop_data_acquisition()
        self._save_data_to_dropbox(save)
        self.top_frame_controller.create_post_processing_panel()

    def _save_data_to_dropbox(self, save):
        if save:
            directory_name = (str(datetime.now().replace(microsecond=0)))

            self.post_processing_database.refresh()
            post_processing_data_string = self.post_processing_database.serialize_data_as_csv()
            real_time_data_string = self.database.serialize_data_as_csv()
            injection_table_string = InjectionTable().serialize_data_as_csv()

            saver = DropboxSaver()
            saver.save_data_to_dropbox(directory_name, self.REAL_TIME_FILENAME, real_time_data_string)
            saver.save_data_to_dropbox(directory_name, self.POST_PROCESSING_FILENAME, post_processing_data_string)
            saver.save_data_to_dropbox(directory_name, self.INJECTION_TABLE_FILENAME, injection_table_string)

