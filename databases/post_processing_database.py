from __future__ import division
from math import pi
import numpy as np
from databases.real_time_database import RealTimeDatabase

class PostProcessingDatabase(object):
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state

    def refresh(self):
        self.real_time_database = RealTimeDatabase()
        self._initialize_data_arrays()

    def _initialize_data_arrays(self):
        self.rpms, self.torques = self._create_sorted_rpms_and_torques()
        self.powers = self._calculate_powers()

    #TODO Not efficient...
    def _create_sorted_rpms_and_torques(self):
        #Pour prendre seulement les points ou la vitesse augmente.
        self.max_index = self._find_end_of_data_acquisition_index(self.real_time_database)

        velocities = self.real_time_database.get_velocities()[:self.max_index]
        rpms = self._convert_velocities_to_rpms(velocities)[:self.max_index]
        torques = self.real_time_database.get_torques()[:self.max_index]

        sorted_index_array = self._calculate_sorted_index_array(rpms)
        sorted_rpms = rpms[sorted_index_array]
        sorted_torques = torques[sorted_index_array]

        return sorted_rpms, sorted_torques

    def _find_end_of_data_acquisition_index(self, real_time_database):
        return np.argmax(real_time_database.get_velocities())

    def _calculate_sorted_index_array(self, rpms):
        return np.argsort(rpms)

    def _convert_velocities_to_rpms(self, velocities):
        return velocities * 60 / (2 * pi)

    def _calculate_powers(self):
        return self.real_time_database.get_velocities()[:self.max_index] * self.torques

    def serialize_data_as_csv(self):
        data_string = ""
        data_string += "Rpms, Torques, Powers \n"

        for i in range(len(self.rpms)):
            data_string += (str(self.rpms[i]) + ",")
            data_string += (str(self.torques[i]) + ",")
            data_string += (str(self.powers[i]) + "\n")

        return data_string

    def get_rpms(self):
        return self.rpms

    def get_torques(self):
        return self.torques

    def get_powers(self):
        return self.powers



