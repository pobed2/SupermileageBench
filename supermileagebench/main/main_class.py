import wx
import matplotlib       # Provides the graph figures
matplotlib.use('WXAgg') # matplotlib needs a GUI (layout), we use wxPython

from supermileagebench.gui.main_frame import MainFrame
from supermileagebench.gui.data_plotting.data_plot import DataPlot
from supermileagebench.gui.data_access.repositories import *
from supermileagebench.phidget.sm_encoder import SMEncoder
from supermileagebench.phidget.encoder_controller import EncoderController
from supermileagebench.data.database import AccelerationDatabase
from supermileagebench.gui.controllers.real_time_panel_controller import RealTimePanelController
from supermileagebench.gui.panels.real_time_panel import RealTimePanel

class MainClass(wx.App):
    def OnInit(self):

        self.database = AccelerationDatabase(5000, 100)
        subplots = self._init_subplots()
        self.frame = MainFrame()
        self.real_time_panel = RealTimePanel(subplots, self.frame)

        self.encoder_controller = EncoderController(self.database)
        self.real_time_controller = RealTimePanelController(self.real_time_panel, self.encoder_controller)
        self.frame.set_controller(self.real_time_controller)

        self._init_encoder()

        self.frame.Show(True)
        self.frame.Centre()

        return True

    def _init_subplots(self):
        subplots = []

        acceleration_repository = AccelerationRepository(self.database)
        torque_repository = TorqueRepository(self.database)

        #Add subplots here
        accelerationPlot = DataPlot(acceleration_repository, subplot_code=(211), title='Acceleration', x_label='Time (s)'
            , y_label= 'Acceleration (radians / seconds^2)')
        torquePlot = DataPlot(torque_repository, subplot_code=(212), title='Torque', x_label='Time (s)'
            , y_label= 'Torque')

        subplots.append(accelerationPlot)
        subplots.append(torquePlot)

        return subplots

    def _init_encoder(self):
        self.encoder = SMEncoder()
        self.encoder.addAttachDetachObserver(self.real_time_controller)
        self.encoder.addChangeObserver(self.encoder_controller)




app = MainClass(0)
app.MainLoop()