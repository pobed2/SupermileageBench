from phidget.sm_encoder import SMEncoder

class EncoderController(object):
    def __init__(self, database):
        self.database = database
        self.started = False
        self._init_encoder()

    def encoder_is_attached(self):
        pass

    def encoder_is_detached(self):
        pass

    def start_data_acquisition(self):
        self.started = True

    def stop_data_acquisition(self):
        self.started = False

    def updatePosition(self, position, time):
        if self.started:
            self.database.addPoint(position, time)

    def _init_encoder(self):
        self.encoder = SMEncoder()
        self.encoder.addAttachDetachObserver(self)
        self.encoder.addChangeObserver(self)