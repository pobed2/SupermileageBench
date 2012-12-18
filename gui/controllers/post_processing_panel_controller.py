from dropbox_actions.dropbox_downloader import DropboxDownloader
from gui.mvc_helpers.observable_events import FileCheckedObservableEvent, FileUncheckedObservableEvent
from gui.windows.post_processing_panel import PostProcessingPanel

class PostProcessingPanelController(object):
    def __init__(self, sub_data_plots):
        self.sub_data_plots = sub_data_plots
        self.dropbox_downloader = DropboxDownloader()
        self.filenames_to_compare_to = self.dropbox_downloader.fetch_names_of_comparable_files()

    def create_panel(self, frame):
        self.panel = PostProcessingPanel(frame, self.sub_data_plots, self.filenames_to_compare_to)
        self.panel.add_panel_observers(self)
        self.panel.draw_plot_canvas()

    def update(self, event):
        if  isinstance(event, FileCheckedObservableEvent):
            print "Intercepted file checked event"
        elif isinstance(event, FileUncheckedObservableEvent):
            print "Intercepted file unchecked event"

        print event.filename