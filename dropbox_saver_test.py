from dropbox_actions.dropbox_downloader import DropboxDownloader

def main():
    dd = DropboxDownloader()
    dd.fetch_names_of_comparable_files()

if __name__ == "__main__":
    main()
