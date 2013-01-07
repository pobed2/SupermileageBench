from data_access.repository import Repository
from databases.dropbox_database import DropboxDatabase

class DropboxRepository(Repository):
    def __init__(self):
        self.database = DropboxDatabase()

    def fetch_names_of_comparable_files(self):
        return self.database.fetch_names_of_comparable_files()

    def add_file_to_compare_to_data(self, filename):
        return self.database.add_file_to_compare_to_data(filename)

    def remove_file_to_compare_to_data(self, filename):
        self.database.remove_file_to_compare_to_data(filename)


class PositionRadiansDropboxRepository(DropboxRepository):
    def __init__(self):
        super(PositionRadiansDropboxRepository, self).__init__()
        self.x_data_getter = self.database.get_times
        self.y_data_getter = self.database.get_positions_rad_time


class PositionMetersDropboxRepository(DropboxRepository):
    def __init__(self):
        super(PositionMetersDropboxRepository, self).__init__()
        self.x_data_getter = self.database.get_times
        self.y_data_getter = self.database.get_positions_rad_time #TODO update this to meters


class SpeedRadiansDropboxRepository(DropboxRepository):
    def __init__(self):
        super(SpeedRadiansDropboxRepository, self).__init__()
        self.x_data_getter = self.database.get_times
        self.y_data_getter = self.database.get_speeds_rad_time


class SpeedMetersDropboxRepository(DropboxRepository):
    def __init__(self):
        super(SpeedMetersDropboxRepository, self).__init__()
        self.x_data_getter = self.database.get_times
        self.y_data_getter = self.database.get_speeds_rad_time #TODO update this to meters


class TorqueDropboxRepository(DropboxRepository):
    def __init__(self):
        super(TorqueDropboxRepository, self).__init__()
        self.x_data_getter = self.database.get_rpms
        self.y_data_getter = self.database.get_torques_rpms


class PowerDropboxRepository(DropboxRepository):
    def __init__(self):
        super(PowerDropboxRepository, self).__init__()
        self.x_data_getter = self.database.get_rpms
        self.y_data_getter = self.database.get_powers_rpms


