from __future__ import print_function
from dropbox import client, session

class DropboxAction(object):
    def __init__(self):
        self.APP_KEY = 'b7vlkm7gkajqco7'
        self.APP_SECRET = 'tpxewwe7xjv6jpp'
        self.ACCESS_TYPE = 'dropbox'
        self.FOLDER_NAME = 'SupermileageBench/'

    def _log_in(self):
        sess = session.DropboxSession(self.APP_KEY, self.APP_SECRET, self.ACCESS_TYPE)

        try:
            with open('dropbox_token.txt') as token:
                token_key, token_secret = token.read().split('|')
                sess.set_token(token_key, token_secret)
        except IOError as e:
            request_token = sess.obtain_request_token()
            url = sess.build_authorize_url(request_token)
            print("url:", url)
            print("Please visit this website and press the 'Allow' button, then hit 'Enter' here.")
            raw_input()
            access_token = sess.obtain_access_token(request_token)

            with open('dropbox_token.txt', 'w') as token:
                token.write("%s|%s" % (access_token.key, access_token.secret))

        self.client = client.DropboxClient(sess)