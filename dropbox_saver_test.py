from dropbox_actions.dropbox_downloader import DropboxDownloader

def main():
    dd = DropboxDownloader()
    dd.download_last_two_post_processing_files()

if __name__ == "__main__":
    main()
