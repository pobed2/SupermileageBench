import numpy as np

class Repository(object):

    def __init__(self, database):
        self.time = database.get_time()
        self.data = []

    def get_time_data(self):
        timeArray = np.array(self.time)
        return timeArray[len(self.data)-len(timeArray):]

    def get_plotting_data(self):
        return np.array(self.data)

    def get_max_time(self):
        return self.time[-1]

    def get_min_data(self):
        return min(self.data)

    def get_max_data(self):
        return max(self.data)


class PositionRepository(Repository):

    def __init__(self, database):
        self.time = database.get_time()
        self.data = database.get_positions()

class VelocityRepository(Repository):

    def __init__(self, database):
        self.time = database.get_time()
        self.data = database.get_velocities()

class AccelerationRepository(Repository):

    def __init__(self, database):
        self.time = database.get_time()
        self.data = database.get_accelerations()

class TorqueRepository(Repository):

    def __init__(self, database):
        self.database = database
        self.time = database.get_time()
        self.data = database.get_torques()

    def get_time_data(self):
        timeArray = np.array(self.time)
        self.data = self.database.get_torques()
        return timeArray[len(self.data)-len(timeArray):]

    def get_min_data(self):
        self.data = self.database.get_torques()
        return min(list(self.data))

    def get_max_data(self):
        self.data = self.database.get_torques()
        return max(self.data)