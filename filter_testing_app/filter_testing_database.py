from __future__ import division
from data_math.derivation import derivate
from data_math.filters import savitzky_golay

import math
import numpy as np

class FilterTestingDatabase(object):
    def __init__(self, time, positions, derivative_interval=100, filter_order=1, filter_window=111):
        self.DERIVATIVE_INTERVAL = derivative_interval / 1000
        self.FILTER_ORDER = filter_order
        self.FILTER_WINDOW = filter_window

        self.DISC_INERTIA = 0.258064
        self.ARRAY_SIZE = 20000
        self.NUMBER_OF_PULSES_PER_TURN = 1440

        self.totalTime = 0
        self.array_index = 0

        self.velocities = np.empty(self.ARRAY_SIZE)
        self.unfiltered_velocities = np.empty(self.ARRAY_SIZE)
        self.accelerations = np.empty(self.ARRAY_SIZE)
        self.unfiltered_accelerations = np.empty(self.ARRAY_SIZE)
        self.torques = np.empty(self.ARRAY_SIZE)

        self.time = time
        self.positions = positions

        self._populate_remaining_arrays()

    def reset_time_and_positions(self, time, positions, derivative_interval, filter_order, filter_window):
        self.DERIVATIVE_INTERVAL = derivative_interval / 1000
        self.FILTER_ORDER = filter_order
        self.FILTER_WINDOW = filter_window

        self.unfiltered_velocities = np.empty(self.ARRAY_SIZE)
        self.unfiltered_accelerations = np.empty(self.ARRAY_SIZE)
        self.array_index = 0

        self.time = time
        self.positions = positions

        self._populate_remaining_arrays()

    def _populate_remaining_arrays(self):
        for i in range(len(self.time)):
            self.add_point(self.time[i], self.positions[i])

        self._filter_arrays()

    def _filter_arrays(self):
        self.velocities = savitzky_golay(self.unfiltered_velocities[:self.array_index],
            self.FILTER_WINDOW, self.FILTER_ORDER, deriv=0)
        self.accelerations = savitzky_golay(self.unfiltered_accelerations[:self.array_index],
            self.FILTER_WINDOW, self.FILTER_ORDER, deriv=0)
        self.torques = self.accelerations[:self.array_index] * self.DISC_INERTIA

    def add_point(self, time, position):
        self._add_velocity_point()
        self._add_acceleration_point()
        self.array_index += 1

    def _add_velocity_point(self):
        self.unfiltered_velocities[self.array_index] = derivate(self.time[:self.array_index + 1],
            self.positions[:self.array_index + 1], self.DERIVATIVE_INTERVAL)


    def _add_acceleration_point(self):
        self.unfiltered_accelerations[self.array_index] = derivate(self.time[:self.array_index + 1],
            self.unfiltered_velocities[:self.array_index + 1], self.DERIVATIVE_INTERVAL)

    def _convert_pulses_to_radians(self, position):
        return (position / self.NUMBER_OF_PULSES_PER_TURN) * (2 * math.pi)

    def get_time(self):
        return self.time[:self.array_index]

    def get_positions(self):
        return self.positions[:self.array_index]

    def get_velocities(self):
        return self.velocities[:self.array_index]

    def get_unfiltered_velocities(self):
        return self.unfiltered_velocities[:self.array_index]

    def get_accelerations(self):
        return self.accelerations[:self.array_index]

    def get_unfiltered_accelerations(self):
        return self.unfiltered_accelerations[:self.array_index]

    def get_torques(self):
        return self.torques[:self.array_index]
