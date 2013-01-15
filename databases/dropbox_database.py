from dropbox_actions.dropbox_downloader import DropboxDownloader

class DropboxDatabase(object):
    __shared_state = {}

    #TODO Caching (dictionnary?)
    def __init__(self):
        self.__dict__ = self.__shared_state

    def initialize_database(self):
        self.drobbox_downloader = DropboxDownloader()
        self.filenames = []

        self.times = []
        self.positions_rad_time = []
        self.positions_meters_time = []
        self.speeds_rad_time = []
        self.speeds_meters_time = []
        self.accelerations_rad_time = []
        self.torques_time = []

        self.rpms = []
        self.torques_rpm = []
        self.powers_rpm = []

    def add_file_to_compare_to_data(self, filename):
        self.filenames.append(filename)

        timewise_data = self.drobbox_downloader.download_timewise_data(filename)
        self.times.append(timewise_data["Time"])
        self.positions_rad_time.append(timewise_data["Positions"])
        self.positions_meters_time.append(timewise_data["Positions_M"])
        self.speeds_rad_time.append(timewise_data["Velocities"])
        self.speeds_meters_time.append(timewise_data["Speeds_KMH"])
        self.accelerations_rad_time.append(timewise_data["Accelerations"])
        self.torques_time.append(timewise_data["Torques"])

        rpmwise_data = self.drobbox_downloader.download_rpmwise_data(filename)
        self.rpms.append(rpmwise_data["Rpms"])
        self.torques_rpm.append(rpmwise_data["Torques"])
        self.powers_rpm.append(rpmwise_data["Powers"])

    def remove_file_to_compare_to_data(self, filename):
        file_index = self.filenames.index(filename)
        self.rpms.pop(file_index)
        self.torques_rpm.pop(file_index)
        self.powers_rpm.pop(file_index)
        self.filenames.pop(file_index)

    def fetch_names_of_comparable_files(self):
        return self.drobbox_downloader.fetch_names_of_comparable_files()

    def get_times(self):
        return self.times

    def get_positions_rad_time(self):
        return self.positions_rad_time

    def get_positions_meters_time(self):
        return self.positions_meters_time

    def get_speeds_rad_time(self):
        return self.speeds_rad_time

    def get_speeds_meters_time(self):
        return self.speeds_meters_time

    def get_accelerations_rad_time(self):
        return self.accelerations_rad_time

    def get_torques_time(self):
        return self.torques_time

    def get_rpms(self):
        return self.rpms

    def get_torques_rpms(self):
        return self.torques_rpm

    def get_powers_rpms(self):
        return self.powers_rpm
