from __future__ import division
from math import pi

class PostProcessingRepository(object):
    def __init__(self, database):
        self.database = database


class TorquePostProcessingRepository(PostProcessingRepository):
    def __init__(self, database):
        super(TorquePostProcessingRepository, self).__init__(database)

    def get_x_data(self):
        #RPM
        velocities = self.database.get_velocities()
        velocities.sort()
        rpms = self._transform_rads_into_rpms(velocities)
        return rpms

    def _transform_rads_into_rpms(self, rads):
        print rads
        return [(rad * 60 / (2 * pi)) for rad in rads]

    def get_y_data(self):
        return self.database.get_torques()

    def get_max_x_data(self):
        return max(self._transform_rads_into_rpms(self.database.get_velocities()))

    def get_max_y_data(self):
        return max(list(self.database.get_torques()))

    def get_min_y_data(self):
        return min(list(self.database.get_torques()))


class PowerPostProcessingRepository(PostProcessingRepository):
    def __init__(self, database):
        pass


