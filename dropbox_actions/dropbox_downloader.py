import StringIO
from dropbox_actions.dropbox_action import DropboxAction
import numpy as np

class DropboxDownloader(DropboxAction):
    def download_last_two_post_processing_files(self):
        self._log_in()
        supermileage_metadata = self.client.metadata(self.FOLDER_NAME)

        folders = []

        for file in supermileage_metadata['contents']:
            if file['is_dir']:
                folders.append(file)

        last_two_folders = folders[-2:]

        arrays = []

        for folder in last_two_folders:
            post_file = self.client.get_file(folder['path'] + '/PostProcessing.csv')
            io = StringIO.StringIO(post_file.read())
            arrays.append(np.genfromtxt(io, skiprows=1, usecols=(0, 1, 2), delimiter=',', unpack=True))

        return arrays