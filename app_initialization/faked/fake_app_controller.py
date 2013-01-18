from app_initialization.app_controller import *
from phidget.faked.fake_encoder_controller import FakeEncoderController

class FakeAppController(AppController):
    def _init_encoder_controller(self):
        self.encoder_controller = FakeEncoderController(self.database)

    def _save_data_to_dropbox(self):
        pass

