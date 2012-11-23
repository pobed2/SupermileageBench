from __future__ import division
from math import pi
import numpy as np

class PostProcessingDatabase(object):
    def __init__(self, real_time_database):
        sorted_data_array = self._create_sorted_data_array(real_time_database)

        self.rpms = self._fetch_rpms(sorted_data_array)
        self.torques = self._fetch_torques(sorted_data_array)
        self.powers = self._calculate_powers(sorted_data_array)

    #TODO Not efficient...
    def _create_sorted_data_array(self, real_time_database):
        velocities = real_time_database.get_velocities()
        rpms = self._convert_velocities_to_rpms(velocities)
        torques = real_time_database.get_torques()
        data_array = np.vstack((torques, rpms))
        sorted_data_array = np.sort(data_array)

        return sorted_data_array

    def _convert_velocities_to_rpms(self, velocities):
        return velocities * 60 / (2 * pi)

    def _fetch_rpms(self, data_array):
        return data_array[1]

    def _fetch_torques(self, data_array):
        return data_array[0]

    def _calculate_powers(self, big_array):
        pass

    #TODO Add Powers
    def serialize_data_as_csv(self):
        data_string = ""
        data_string += "Rpms, Torques \n"

        for i in range(len(self.rpms)):
            data_string += (str(self.rpms[i]) + ",")
            data_string += (str(self.torques[i]) + "\n")

        return data_string



