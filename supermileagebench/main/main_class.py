import wx

from supermileagebench.gui.controllers.app_controller import AppController

class MainClass(wx.App):
    def OnInit(self):
        self.app_controller = AppController()
        return True

    #    def OnInit(self):
#        self.database = AccelerationDatabase(5000, 100)
#        self.real_time_subplots = self._init_real_time_subplots()
#        self.post_treatment_subplots = self._init_post_treatment_subplots()
#
#        self.encoder_controller = EncoderController(self.database)
#        self.real_time_controller = RealTimePanelController(self.encoder_controller)
#        self.post_treatment_controller = PostTreatmentPanelController(self.post_treatment_subplots)
#        self.top_frame_controller = TopFrameController(self.real_time_controller, self.post_treatment_controller)
#
#        #TODO Mettre la creation de panels dans les controlleurs?
#        self.frame = TopFrame(self.top_frame_controller)
#        self.real_time_panel = RealTimePanel(self.real_time_subplots, self.frame)
#
#        self.real_time_controller.set_panel(self.real_time_panel)
#        self.top_frame_controller.set_frame(self.frame)
#
#        self._init_encoder()
#
#        self.frame.Show(True)
#        self.frame.Centre()
#
#        return True
#
#    def _init_real_time_subplots(self):
#        subplots = []
#
#        acceleration_repository = AccelerationRepository(self.database)
#        torque_repository = TorqueRepository(self.database)
#
#        #Add subplots here
#        accelerationPlot = DataPlot(acceleration_repository, subplot_code=(211), title='Acceleration',
#            x_label='Time (s)'
#            , y_label='Acceleration (radians / seconds^2)')
#        torquePlot = DataPlot(torque_repository, subplot_code=(212), title='Torque', x_label='Time (s)'
#            , y_label='Torque')
#
#        subplots.append(accelerationPlot)
#        subplots.append(torquePlot)
#
#        return subplots
#
#    def _init_post_treatment_subplots(self):
#        subplots = []
#
#        acceleration_repository = AccelerationRepository(self.database)
#
#        #Add subplots here
#        accelerationPlot = DataPlot(acceleration_repository, subplot_code=(111), title='Acceleration',
#            x_label='Time (s)'
#            , y_label='Acceleration (radians / seconds^2)')
#
#        subplots.append(accelerationPlot)
#
#        return subplots
#
#    def _init_encoder(self):
#        self.encoder = SMEncoder()
#        self.encoder.addAttachDetachObserver(self.encoder_controller)
#        self.encoder.addChangeObserver(self.encoder_controller)


app = MainClass(0)
app.MainLoop()