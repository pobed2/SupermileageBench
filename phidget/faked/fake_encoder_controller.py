from phidget.encoder_controller import EncoderController
from phidget.faked.fake_data_provider import FakeDataProvider
from phidget.faked.fake_encoder import FakeEncoder

class FakeEncoderController(EncoderController):
    def _init_encoder(self):
        self.encoder = FakeEncoder()
        self.encoder.addAttachDetachObserver(self)
        self.encoder.addChangeObserver(self)

        self.fake_data_provider = FakeDataProvider(self.encoder)
        self.fake_data_provider.start_data_providing()