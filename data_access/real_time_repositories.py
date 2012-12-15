from data_access.repository import Repository

class PositionRealTimeRepository(Repository):
    def __init__(self, database):
        self.x_data_getter = database.get_time
        self.y_data_getter = database.get_positions


class VelocityRealTimeRepository(Repository):
    def __init__(self, database):
        self.x_data_getter = database.get_time
        self.y_data_getter = database.get_velocities


class AccelerationRealTimeRepository(Repository):
    def __init__(self, database):
        self.x_data_getter = database.get_time
        self.y_data_getter = database.get_accelerations


class TorqueRealTimeRepository(Repository):
    def __init__(self, database):
        self.x_data_getter = database.get_time
        self.y_data_getter = database.get_torques