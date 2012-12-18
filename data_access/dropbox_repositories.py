from data_access.repository import Repository
from databases.dropbox_database import DropboxDatabase

class DropboxRepository(Repository):
    def __init__(self):
        self.database = DropboxDatabase()
        self.database.initialize_database()

    def refresh_database(self):
        self.database.refresh()


class TorqueDropboxRepository(DropboxRepository):
    def __init__(self):
        super(TorqueDropboxRepository, self).__init__()
        self.x_data_getter = self.database.get_rpms
        self.y_data_getter = self.database.get_torques


class PowerDropboxRepository(DropboxRepository):
    def __init__(self):
        super(PowerDropboxRepository, self).__init__()
        self.x_data_getter = self.database.get_rpms
        self.y_data_getter = self.database.get_powers


