from data_access.repository import Repository
from databases.real_time_database import RealTimeDatabase

class PositionRadiansTimewiseRepository(Repository):
    def __init__(self):
        database = RealTimeDatabase()
        self.x_data_getter = database.get_time
        self.y_data_getter = database.get_positions

    def refresh_database(self):
        pass


class PositionMetersTimewiseRepository(Repository):
    def __init__(self):
        database = RealTimeDatabase()
        self.x_data_getter = database.get_time
        self.y_data_getter = database.get_positions_in_meters


class SpeedRadiansTimewiseRepository(Repository):
    def __init__(self):
        database = RealTimeDatabase()
        self.x_data_getter = database.get_time
        self.y_data_getter = database.get_velocities


class SpeedMetersTimewiseRepository(Repository):
    def __init__(self):
        database = RealTimeDatabase()
        self.x_data_getter = database.get_time
        self.y_data_getter = database.get_speed_in_kmh


class AccelerationTimewiseRepository(Repository):
    def __init__(self):
        database = RealTimeDatabase()
        self.x_data_getter = database.get_time
        self.y_data_getter = database.get_accelerations


class TorqueTimewiseRepository(Repository):
    def __init__(self):
        database = RealTimeDatabase()
        self.x_data_getter = database.get_time
        self.y_data_getter = database.get_torques