from __future__ import print_function
from dropbox import client, rest, session


APP_KEY = 'b7vlkm7gkajqco7'
APP_SECRET = 'tpxewwe7xjv6jpp'
ACCESS_TYPE = 'dropbox'
FOLDER_NAME = 'SupermileageBench/'

class DropboxSaver(object):
    
    def __init__(self):
        pass
    
    def save_data_to_dropbox(self, file_name):
        self._log_in()
        return self._upload_file(file_name)
        
    def _log_in(self):
        sess = session.DropboxSession(APP_KEY, APP_SECRET, ACCESS_TYPE)
        
        try:
            with open('dropbox_token.txt') as token:
                 token_key,token_secret = token.read().split('|')
                 sess.set_token(token_key,token_secret)
        except IOError as e:
            request_token = sess.obtain_request_token()
            url = sess.build_authorize_url(request_token)
            print("url:", url)
            print("Please visit this website and press the 'Allow' button, then hit 'Enter' here.")
            raw_input()
            access_token = sess.obtain_access_token(request_token)
            
            with open ('dropbox_token.txt', 'w') as token: 
                token.write ("%s|%s" % (access_token.key,access_token.secret))
            
        self.client = client.DropboxClient(sess)
    
    def _upload_file(self, file_name):
        fileToUpload = open(file_name)
        response = self.client.put_file(FOLDER_NAME + file_name, fileToUpload)
        return response
    
    
def main():
    saver = DropboxSaver()
    saver.save_data_to_dropbox("plot.csv")

if __name__ == '__main__':
    main()