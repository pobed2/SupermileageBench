from dropbox_actions.dropbox_downloader import DropboxDownloader

class DropboxDatabase(object):
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state

    def initialize_database(self):
        self.drobbox_downloader = DropboxDownloader()
        self.filenames = []
        self.rpms = []
        self.torques = []
        self.powers = []

    def add_file_to_compare_to_data(self, filename):
        self.filenames.append(filename)
        data = self.drobbox_downloader.download_file(filename)
        self.rpms.append(data[0])
        self.torques.append(data[1])
        self.powers.append(data[2])

    def remove_file_to_compare_to_data(self, filename):
        file_index = self.filenames.index(filename)
        self.rpms.pop(file_index)
        self.torques.pop(file_index)
        self.powers.pop(file_index)
        self.filenames.pop(file_index)

    def fetch_names_of_comparable_files(self):
        return self.drobbox_downloader.fetch_names_of_comparable_files()

    def get_rpms(self):
        return self.rpms

    def get_torques(self):
        return self.torques

    def get_powers(self):
        return self.powers
