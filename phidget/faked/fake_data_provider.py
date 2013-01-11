from __future__ import division
from math import pi
from threading import Thread
from time import sleep
import numpy as np

class FakeDataProvider(object):
    def __init__(self, fake_encoder):
        self.fake_encoder = fake_encoder
        self.time, self.positions = np.loadtxt(
            "/Users/MacBook/Dropbox/SupermileageBench/2012-11-27 16:56:59/RealTime.csv", skiprows=1, usecols=(0, 1),
            delimiter=',', unpack=True)

    def start_data_providing(self):
        self.fake_encoder.encoderAttached()
        t = Thread(target=self._change_position)
        t.start()

    def _change_position(self):
        for i in range(0, len(self.time)):
            self.fake_encoder.encoderPositionChange((self.positions[i] * 1440) / (2 * pi),
                (self.time[i] - self.time[i - 1]) * 1000)
            if i == 10:
                print "Starting sleep"
                sleep(5)
                print "Stopped sleeping"


