from __future__ import division
from math import pi
import numpy as np

class PostProcessingDatabase(object):
    def __init__(self, real_time_database):
        self.real_time_database = real_time_database
        self._initialize_data_arrays()

    def refresh(self):
        self._initialize_data_arrays()

    def _initialize_data_arrays(self):
        sorted_data_array = self._create_sorted_data_array(self.real_time_database)
        self.rpms = self._fetch_rpms(sorted_data_array)
        self.torques = self._fetch_torques(sorted_data_array)
        self.powers = self._calculate_powers(sorted_data_array)

    #TODO Not efficient...
    def _create_sorted_data_array(self, real_time_database):
        velocities = real_time_database.get_velocities()
        rpms = self._convert_velocities_to_rpms(velocities)
        torques = real_time_database.get_torques()

        sorted_index_array = self._calculate_sorted_index_array(rpms)
        sorted_rpms = rpms[sorted_index_array]
        sorted_torques = torques[sorted_index_array]

        sorted_data_array = np.vstack((sorted_rpms, sorted_torques))

        return sorted_data_array

    def _calculate_sorted_index_array(self, rpms):
        return np.argsort(rpms)

    def _convert_velocities_to_rpms(self, velocities):
        return velocities * 60 / (2 * pi)

    def _fetch_rpms(self, data_array):
        return data_array[0]

    def _fetch_torques(self, data_array):
        return data_array[1]

    def _calculate_powers(self, data_array):
        return data_array[1] * data_array[0]

    #TODO Add Powers
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



