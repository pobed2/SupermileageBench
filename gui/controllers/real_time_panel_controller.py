class RealTimePanelController(object):
    def __init__(self, encoder_controller, app_controller):
        self.encoder_controller = encoder_controller
        self.app_controller = app_controller

    def set_panel(self, panel):
        self.panel = panel

    def start_plotting(self):
        self.panel.startTimer()
        self.encoder_controller.start_data_acquisition()

    def stop_plotting(self, save):
        self.panel.stop_timer()
        self.panel.hide()
        self.encoder_controller.stop_data_acquisition()
        if save:
            self.app_controller.save_data_to_dropbox()

