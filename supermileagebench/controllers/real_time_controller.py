from supermileagebench.dropbox_actions.dropbox_saver import  DropboxSaver
import os

class RealTimeController(object):

    def __init__(self, frame, encoder_controller):
        self.frame = frame
        self.encoder_controller = encoder_controller

    def encoder_is_attached(self):
        pass

    def start_plotting(self):
        self.frame.startTimer()
        self.encoder_controller.start_data_acquisition()

    def stop_plotting(self, save):
        self.frame.stop_timer()
        self.frame.hide()
        self.encoder_controller.stop_data_acquisition()
        if save:
            self._save_data_to_dropbox()
        self.delete_data()

    def _save_data_to_dropbox(self):
        filename = self._save_to_csv()
        saver = DropboxSaver()
        saver.save_data_to_dropbox(filename)
        os.remove(filename)

    def delete_data(self):
        pass