from __future__ import division
from configuration.properties_parser import PropertiesParser
from math_functions.derivation import derivate
from math_functions.filters import savitzky_golay

import math
import numpy as np

class RealTimeDatabase(object):
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state

    def initialize_database(self):
        self.properties_parser = PropertiesParser()

        self.wheel_size_in_inches = 2
        self.m_per_inches = 0.0254
        self.DISC_INERTIA = float(self.properties_parser.get_property("Inertia"))
        #self.FRICTION_COEFF = float(self.properties_parser.get_property("Friction"))

        self.ARRAY_SIZE = 20000

        self.totalTime = 0
        self.array_index = 0

        self.time = np.empty(self.ARRAY_SIZE)
        self.positions_in_rad = np.empty(self.ARRAY_SIZE)
        self.positions_in_meters = np.empty(self.ARRAY_SIZE)
        self.velocities_in_rad = np.empty(self.ARRAY_SIZE)
        self.speed_in_kmh = np.empty(self.ARRAY_SIZE)
        self.accelerations_in_rad = np.empty(self.ARRAY_SIZE)
        self.torques = np.empty(self.ARRAY_SIZE)

        self.derivativeInterval = 0.1

        self.numberOfPulsesPerTurn = 1440
        self.started = False


    def get_time(self):
        return self.time[:self.array_index]

    def get_positions(self):
        return self.positions_in_rad[:self.array_index]

    def get_positions_in_meters(self):
        return self.positions_in_meters[:self.array_index]

    def get_velocities(self):
        return self.velocities_in_rad[:self.array_index]

    def get_speed_in_kmh(self):
        return self.speed_in_kmh[:self.array_index]

    def get_accelerations(self):
        return self.accelerations_in_rad[:self.array_index]

    def get_torques(self):
        return self.torques[:self.array_index]

    def addPoint(self, position_in_pulses, timeAfterLastPoint):
        if timeAfterLastPoint < 2147483647: #To eliminate the first point
            self._add_time_point(timeAfterLastPoint)
            self._add_position_point(position_in_pulses)
            self._add_position_in_meters_point(position_in_pulses)
            self._add_velocity_point()
            self._add_speed_point_in_kmh()
            self._add_acceleration_point()
            self._add_torque_point()
            self.array_index += 1

    def _add_time_point(self, timeAfterLastPoint):
        self.totalTime += (timeAfterLastPoint * 0.001)
        self.time[self.array_index] = self.totalTime

    def _add_position_point(self, position_in_pulses):
        position_in_radians = self._convert_pulses_to_radians(position_in_pulses)
        self.positions_in_rad[self.array_index] = position_in_radians

    def _add_position_in_meters_point(self, position_in_pulses):
        position_in_meters = self._convert_pulses_to_meters(position_in_pulses)
        self.positions_in_meters[self.array_index] = position_in_meters

    def _add_velocity_point(self):
        self.velocities_in_rad[self.array_index] = derivate(self.time[:self.array_index + 1],
            self.positions_in_rad[:self.array_index + 1],
            self.derivativeInterval)
        self.velocities_in_rad[:self.array_index + 1] = savitzky_golay(self.velocities_in_rad[:self.array_index + 1],
            41, 3, deriv=0)

    def _add_speed_point_in_kmh(self):
        self.speed_in_kmh[self.array_index] = self._convert_rads_per_seconds_to_kmh(
            self.velocities_in_rad[self.array_index])

    def _add_acceleration_point(self):
        self.accelerations_in_rad[self.array_index] = derivate(self.time[:self.array_index + 1],
            self.velocities_in_rad[:self.array_index + 1],
            self.derivativeInterval)
        self.accelerations_in_rad[:self.array_index + 1] = savitzky_golay(
            self.accelerations_in_rad[:self.array_index + 1], 41, 3,
            deriv=0)

    def _add_torque_point(self):
        #self.torques = savitzky_golay(self.accelerations[:self.array_index + 1], 101, 1, deriv=0)
        self.torques = self.accelerations_in_rad[:self.array_index + 1] * self.DISC_INERTIA

    #TODO Get the math out
    def _convert_pulses_to_radians(self, position_in_pulses):
        return (position_in_pulses / self.numberOfPulsesPerTurn) * (2 * math.pi)

    def _convert_pulses_to_meters(self, position_in_pulses):
        position_in_radians = self._convert_pulses_to_radians(position_in_pulses)
        return position_in_radians * self.m_per_inches * self.wheel_size_in_inches

    def _convert_rads_per_seconds_to_kmh(self, speed_in_rads):
        return speed_in_rads * self.wheel_size_in_inches * self.m_per_inches / 1000 * 3600

    def serialize_data_as_csv(self):
        data_string = ""
        data_string += "Time, Positions, Positions_M, Velocities, Speeds_KMH, Accelerations, Torques \n"

        for i in range(len(self.time[:self.array_index])):
            data_string += (str(self.time[i]) + ",")
            data_string += (str(self.positions_in_rad[i]) + ",")
            data_string += (str(self.positions_in_meters[i]) + ",")
            data_string += (str(self.velocities_in_rad[i]) + ",")
            data_string += (str(self.speed_in_kmh[i]) + ",")
            data_string += (str(self.accelerations_in_rad[i]) + ",")
            data_string += (str(self.torques[i]) + "\n")

        return data_string

    def reset(self):
        self.initialize_database()

