from __future__ import division
from supermileagebench.data_math.DynoMath import derivate
from supermileagebench.data_math.filters import savitzky_golay

import math
import numpy as np

class Database(object):
    def __init__(self, derivativeInterval=100):
        self.DISC_INERTIA = 23
        self.ARRAY_SIZE = 20000

        self.totalTime = 0
        self.array_index = 0

        self.time = np.empty(self.ARRAY_SIZE)
        self.positions = np.empty(self.ARRAY_SIZE)
        self.velocities = np.empty(self.ARRAY_SIZE)
        self.accelerations = np.empty(self.ARRAY_SIZE)
        self.torques = np.empty(self.ARRAY_SIZE)

        self.derivativeInterval = derivativeInterval / 1000

        self.numberOfPulsesPerTurn = 1440
        self.started = False


    def get_time(self):
        return self.time

    def get_positions(self):
        return self.positions

    def get_velocities(self):
        return self.velocities

    def get_accelerations(self):
        return self.accelerations

    def get_torques(self):
        return self.torques

    def addPoint(self, position, timeAfterLastPoint):
        if timeAfterLastPoint < 2147483647: #To eliminate the first point
            self._add_time_point(timeAfterLastPoint)
            self._add_position_point(position)
            self._add_velocity_point()
            self._add_acceleration_point()
            self._add_torque_point()
            self.array_index += 1

    def _add_time_point(self, timeAfterLastPoint):
        self.totalTime += (timeAfterLastPoint * 0.001)
        self.time[self.array_index] = self.totalTime

    def _add_position_point(self, position):
        position_in_radians = self._convert_pulses_to_radians(position)
        self.positions[self.array_index] = position_in_radians

    def _add_velocity_point(self):
        velocity = derivate(self.time[:self.array_index], self.positions[:self.array_index], self.derivativeInterval)
        self.velocities[self.array_index] = velocity

    def _add_acceleration_point(self):
        acceleration = derivate(self.time[:self.array_index], self.velocities[:self.array_index],
            self.derivativeInterval)
        self.accelerations[self.array_index] = acceleration

    def _add_torque_point(self):
        self.torques = savitzky_golay(self.accelerations[:self.array_index], 111, 1, deriv=0)
        self.torques *= self.DISC_INERTIA

    def _convert_pulses_to_radians(self, position):
        return (position / self.numberOfPulsesPerTurn) * (2 * math.pi)

    def serialize_data_as_csv(self):
        data_string = ""
        data_string += "Time, Positions, Velocities, Accelerations, Torques \n"

        for i in range(len(self.time[:self.array_index])):
            data_string += (str(self.time[i]) + ",")
            data_string += (str(self.positions[i]) + ",")
            data_string += (str(self.velocities[i]) + ",")
            data_string += (str(self.accelerations[i]) + ",")
            data_string += (str(self.torques[i]) + "\n")

        return data_string

