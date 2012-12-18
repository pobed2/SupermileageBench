from dropbox_actions.dropbox_downloader import DropboxDownloader

drobbox_downloader = DropboxDownloader()
last_two_files = drobbox_downloader.download_last_two_post_processing_files()
rpms = [last_two_files[0][0], last_two_files[1][0]]
torques = [last_two_files[0][1], last_two_files[1][1]]
powers = [last_two_files[0][2], last_two_files[1][2]]

def get_rpms():
    return rpms


def get_torques():
    return torques


def get_powers():
    return powers