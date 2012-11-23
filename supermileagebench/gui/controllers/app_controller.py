from supermileagebench.gui.windows.top_frame import TopFrame
from supermileagebench.gui.data_plotting.real_time_data_plot import RealTimeDataPlot
from supermileagebench.gui.data_access.repositories import *
from supermileagebench.phidget.sm_encoder import SMEncoder
from supermileagebench.phidget.encoder_controller import EncoderController
from supermileagebench.data.database import Database
from supermileagebench.gui.controllers.real_time_panel_controller import RealTimePanelController
from supermileagebench.gui.windows.real_time_panel import RealTimePanel
from supermileagebench.gui.controllers.top_frame_controller import TopFrameController
from supermileagebench.gui.controllers.post_treatment_panel_controller import PostTreatmentPanelController
from datetime import datetime
from supermileagebench.dropbox_actions.dropbox_saver import  DropboxSaver
from supermileagebench.gui.data_access.post_processing_repositories import *
from supermileagebench.gui.data_plotting.post_processing_data_plot import *

class AppController(object):
    def __init__(self):
        self._initializeApp()

    def _initializeApp(self):
        self.database = Database()
        self.real_time_subplots = self._init_real_time_subplots()
        self.post_treatment_subplots = self._init_post_treatment_subplots()

        self.encoder_controller = EncoderController(self.database)
        self.real_time_controller = RealTimePanelController(self.encoder_controller, self)
        self.post_treatment_controller = PostTreatmentPanelController(self.post_treatment_subplots)
        self.top_frame_controller = TopFrameController(self.real_time_controller, self.post_treatment_controller)

        #TODO Mettre la creation de panels dans les controlleurs?
        self.frame = TopFrame(self.top_frame_controller)
        self.real_time_panel = RealTimePanel(self.real_time_subplots, self.frame)

        self.real_time_controller.set_panel(self.real_time_panel)
        self.top_frame_controller.set_frame(self.frame)

        self._init_encoder()

        self.frame.Show(True)
        self.frame.Centre()

        return True

    def _init_real_time_subplots(self):
        subplots = []

        acceleration_repository = VelocityRepository(self.database)
        #torque_repository = TorqueRepository(self.database)

        #Add subplots here
        accelerationPlot = RealTimeDataPlot(acceleration_repository, subplot_code=(111), title='Acceleration',
            x_label='Time (s)'
            , y_label='Acceleration (radians / seconds^2)')
        #torquePlot = RealTimeDataPlot(torque_repository, subplot_code=(212), title='Torque', x_label='Time (s)'
        #    , y_label='Torque')

        subplots.append(accelerationPlot)
        #subplots.append(torquePlot)

        return subplots

    def _init_post_treatment_subplots(self):
        subplots = []

        torque_repository = TorquePostProcessingRepository(self.database)

        #Add subplots here
        torquePlot = PostProcessingDataPlot(torque_repository, subplot_code=(111), title='Torque',
            x_label='RPM'
            , y_label='Torque')

        subplots.append(torquePlot)

        return subplots

    def _init_encoder(self):
        self.encoder = SMEncoder()
        self.encoder.addAttachDetachObserver(self.encoder_controller)
        self.encoder.addChangeObserver(self.encoder_controller)

    def save_data_to_dropbox(self):
        filename = ("%s.csv" % str(datetime.now().replace(microsecond=0)))
        data_string = self.database.serialize_data_as_csv()
        saver = DropboxSaver()
        saver.save_data_to_dropbox(filename, data_string)

