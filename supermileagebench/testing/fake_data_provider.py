from threading import Thread
from time import sleep
import numpy as np

class FakeDataProvider(object):
    def __init__(self, fake_encoder):
        self.fake_encoder = fake_encoder
        self.time, self.positions = np.loadtxt(
            "/Users/MacBook/Dropbox/SupermileageBench/2012-11-27 15:23:05/RealTime.csv", skiprows=1, usecols=(0, 1),
            delimiter=',', unpack=True)

    def start_data_providing(self):
        self.fake_encoder.encoderAttached()
        t = Thread(target=self._change_position)
        t.start()

    def _change_position(self):
        for i in range(len(self.time)):
            self.fake_encoder.encoderPositionChange(self.positions[i], self.time[i])
            sleep(0.05)


