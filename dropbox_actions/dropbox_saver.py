from __future__ import print_function
import tempfile
from dropbox_actions.dropbox_action import DropboxAction

class DropboxSaver(DropboxAction):
    def save_data_to_dropbox(self, directory_name, file_name, data_string):
        self._log_in()
        return self._upload_file(directory_name, file_name, data_string)

    def _upload_file(self, directory_name, file_name, data_string):
        with tempfile.NamedTemporaryFile() as file:
            file.write(data_string)
            file.seek(0)
            response = self.client.put_file(self.FOLDER_NAME + directory_name + '/' + file_name, file)
            return response