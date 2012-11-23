from __future__ import division

class PostProcessingRepository(object):
    def __init__(self, database):
        self.database = database

    def refresh_database(self):
        self.database.refresh()


class TorquePostProcessingRepository(PostProcessingRepository):
    def __init__(self, database):
        super(TorquePostProcessingRepository, self).__init__(database)

    def get_x_data(self):
        return self.database.get_rpms()

    def get_y_data(self):
        return self.database.get_torques()

    def get_max_x_data(self):
        return max((self.database.get_rpms()))

    def get_max_y_data(self):
        return max(self.database.get_torques())

    def get_min_y_data(self):
        return min(self.database.get_torques())


class PowerPostProcessingRepository(PostProcessingRepository):
    def __init__(self, database):
        pass


