import os
from supermileagebench.dropbox_actions.dropbox_saver import  DropboxSaver


class RealTimePanelController(object):
    def __init__(self, encoder_controller):
        self.encoder_controller = encoder_controller

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
            self._save_data_to_dropbox()

    def _save_data_to_dropbox(self):
        filename = self._save_to_csv()
        saver = DropboxSaver()
        saver.save_data_to_dropbox(filename)
        os.remove(filename)