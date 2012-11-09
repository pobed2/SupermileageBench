import wx
import matplotlib       # Provides the graph figures
matplotlib.use('WXAgg') # matplotlib needs a GUI (layout), we use wxPython

from supermileagebench.gui.main_frame import MainFrame
from supermileagebench.gui.data_plot import DataPlot

from supermileagebench.phidget.sm_encoder import SMEncoder
from supermileagebench.phidget.encoder_controller import EncoderController
from supermileagebench.Data import AccelerationDatabase
from supermileagebench.controllers.real_time_controller import RealTimeController

class MainClass(wx.App):
    def OnInit(self):

        self.encoder_controller = EncoderController(self.database)
        self._init_encoder()

        self.database = AccelerationDatabase(5000, 100)

        self.real_time_controller = RealTimeController(self.encoder_controller)
        subplots = self.init_subplots()

        self.frame = MainFrame(self.real_time_controller, subplots)
        self.real_time_controller.set_frame(self.frame)


        self.frame.Show(True)
        self.frame.Centre()



        return True

    def _init_subplots(self):
        subplots = []

        acceleration_repository = ''
        torque_repository = ''

        #Add subplots here
        accelerationPlot = DataPlot(acceleration_repository, subplot_code=(121), title='Acceleration', x_label='Time (s)'
            , y_label= 'Acceleration (radians / seconds^2)')
        torquePlot = DataPlot(torque_repository, subplot_code=(122), title='Torque', x_label='Time (s)'
            , y_label= 'Torque')

        subplots.append(accelerationPlot)
        subplots.append(torquePlot)

    def _init_encoder(self):
        self.encoder = SMEncoder()
        self.encoder.addAttachDetachObserver(self.real_time_controller)
        self.encoder.addChangeObserver(self.encoder_controller)




app = MainClass(0)
app.MainLoop()