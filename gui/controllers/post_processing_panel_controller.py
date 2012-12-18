from data_access.dropbox_repositories import DropboxRepository
from gui.mvc_helpers.observable_events import FileCheckedObservableEvent, FileUncheckedObservableEvent
from gui.windows.post_processing_panel import PostProcessingPanel

class PostProcessingPanelController(object):
    def __init__(self, sub_data_plots):
        self.sub_data_plots = sub_data_plots
        self.dropbox_repository = DropboxRepository()

    def create_panel(self, frame):
        names_of_comparable_files = self.dropbox_repository.fetch_names_of_comparable_files()

        self.panel = PostProcessingPanel(frame, self.sub_data_plots, names_of_comparable_files)
        self.panel.add_panel_observers(self)
        self.panel.draw_plot_canvas()


    #TODO CRAPPY CODE
    def update(self, event):
        filename = event.filename

        if  isinstance(event, FileCheckedObservableEvent):
            self._add_data_line_to_canvas(filename)
        elif isinstance(event, FileUncheckedObservableEvent):
            self._remove_line_from_canvas(filename)

    def _add_data_line_to_canvas(self, filename):
        self.dropbox_repository.add_file_to_compare_to_data(filename)
        self.panel.refresh_canvas()

    def _remove_line_from_canvas(self, filename):
        self.dropbox_repository.remove_file_to_compare_to_data(filename)
        self.panel.refresh_canvas()

