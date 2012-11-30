from supermileagebench.gui.data_access.repository import Repository

class UnfilteredVelocityRepository(Repository):
    def __init__(self, database):
        self.x_data_getter = database.get_time
        self.y_data_getter = database.get_unfiltered_velocities


class UnfilteredAccelerationRepository(Repository):
    def __init__(self, database):
        self.x_data_getter = database.get_time
        self.y_data_getter = database.get_unfiltered_accelerations