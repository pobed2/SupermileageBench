from supermileagebench.gui.data_access.repository import Repository

class PostProcessingRepository(Repository):
    def refresh_database(self):
        self.database.refresh()


class TorquePostProcessingRepository(PostProcessingRepository):
    def __init__(self, database):
        self.database = database
        self.x_data_getter = self.database.get_rpms
        self.y_data_getter = self.database.get_torques


class PowerPostProcessingRepository(PostProcessingRepository):
    def __init__(self, database):
        self.database = database
        self.x_data_getter = self.database.get_rpms
        self.y_data_getter = self.database.get_powers


