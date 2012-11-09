from supermileagebench.dropbox.dropbox_saver import  DropboxSaver
import os

class RealTimeController(object):

    def __init__(self, encoder_controller):
        self.encoder_controller = encoder_controller

    def set_frame(self, frame):
        self.frame = frame

    def startTimer(self):
        self.frame.startTimer()

    def start_data_aquisition(self):
        self.encoder_controller.start_data_aquisition()

    def stop_data_aquisition(self, save):
        self.encoder_controller.stop_data_aquisition()
        if save:
            self._save_data_to_dropbox()
        self.deleteData()

    def _save_data_to_dropbox(self):
        filename = self._save_to_csv()
        saver = DropboxSaver()
        saver.save_data_to_dropbox(filename)
        os.remove(filename)