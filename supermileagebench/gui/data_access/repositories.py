class Repository(object):
    '''
    Base class for real-time repositories. They are used to access the data being added in real-time
    Not for use on its own : use one of its child class
    '''

    def get_x_data(self):
        #timeArray = np.array(self.x_data)
        #return self.x_data[len(self.y_data) - len(self.x_data):]
        return self.x_data_getter()

    def get_y_data(self):
        #return np.array(self.y_data)
        return self.y_data_getter()

    def get_max_x_data(self):
        return self.x_data_getter()[-1]

    def get_min_y_data(self):
        return min(self.y_data_getter())

    def get_max_y_data(self):
        return max(self.y_data_getter())


class PositionRepository(Repository):
    def __init__(self, database):
        self.x_data_getter = database.get_time
        self.y_data_getter = database.get_positions


class VelocityRepository(Repository):
    def __init__(self, database):
        self.x_data_getter = database.get_time
        self.y_data_getter = database.get_velocities


class AccelerationRepository(Repository):
    def __init__(self, database):
        self.x_data_getter = database.get_time
        self.y_data_getter = database.get_accelerations


class TorqueRepository(Repository):
    def __init__(self, database):
        self.x_data_getter = database.get_time
        self.y_data_getter = database.get_torques