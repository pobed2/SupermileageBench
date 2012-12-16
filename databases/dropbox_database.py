from dropbox_actions.dropbox_downloader import DropboxDownloader

class DropboxDatabase(object):
    def __init__(self):
        drobbox_downloader = DropboxDownloader()
        last_two_files = drobbox_downloader.download_last_two_post_processing_files()
        self.rpms = [last_two_files[0][0], last_two_files[1][0]]
        self.torques = [last_two_files[0][1], last_two_files[1][1]]
        self.powers = [last_two_files[0][2], last_two_files[1][2]]

    def get_rpms(self):
        return self.rpms

    def get_torques(self):
        return self.torques

    def get_powers(self):
        return self.powers
