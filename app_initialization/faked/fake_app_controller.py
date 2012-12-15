from app_initialization.app_controller import *
from phidget.faked.fake_data_provider import FakeDataProvider
from phidget.faked.fake_encoder import *

class FakeAppController(AppController):
    def _initializeApp(self):
        super(FakeAppController, self)._initializeApp()
        self.fake_data_provider.start_data_providing()

    def _init_encoder(self):
        self.encoder = FakeEncoder()
        self.encoder.addAttachDetachObserver(self.encoder_controller)
        self.encoder.addChangeObserver(self.encoder_controller)

        self.fake_data_provider = FakeDataProvider(self.encoder)

    def save_data_to_dropbox(self):
        pass

