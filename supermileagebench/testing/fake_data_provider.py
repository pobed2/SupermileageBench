from threading import Thread
from time import sleep

class FakeDataProvider(object):
    def __init__(self, fake_encoder):
        self.NUMBER_OF_DATA_POINTS = 1000
        self.time = 0
        self.position = 5
        self.fake_encoder = fake_encoder

    def start_data_providing(self):
        self.fake_encoder.encoderAttached()
        t = Thread(target=self._change_position)
        t.start()

    def _change_position(self):
        for _ in range(self.NUMBER_OF_DATA_POINTS):
            self.fake_encoder.encoderPositionChange(self.position, self.time)
            self.time += 5
            self.position += 5
            sleep(0.005)

        self.fake_encoder.encoderDetached()


