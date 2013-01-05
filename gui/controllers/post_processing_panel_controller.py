from data_access.dropbox_repositories import DropboxRepository
from gui.factories.subplots_factory import PostProcessingSubplotFactory
from gui.mvc_helpers.observable_events import FileCheckedObservableEvent, FileUncheckedObservableEvent, PlotTypesChangedObservableEvent
from gui.mvc_helpers.observer import Observer
from gui.windows.post_processing_panel import PostProcessingPanel

class PostProcessingPanelController(Observer):
    def __init__(self, subplots, app_controller):
        self.subplots = subplots
        self.dropbox_repository = DropboxRepository()
        self.app_controller = app_controller
        self.subplot_factory = PostProcessingSubplotFactory()

    def create_panel(self, frame):
        names_of_comparable_files = self.dropbox_repository.fetch_names_of_comparable_files()

        self.panel = PostProcessingPanel(frame, self.subplots, names_of_comparable_files)
        self.panel.add_panel_observers(self)
        self.panel.draw_plot_canvas()

    #TODO CRAPPY CODE
    def update(self, event):
        if event == "reset":
            self.app_controller.reset_app()
        elif  isinstance(event, FileCheckedObservableEvent):
            filename = event.filename
            self._add_data_line_to_canvas(filename)
        elif isinstance(event, FileUncheckedObservableEvent):
            filename = event.filename
            self._remove_line_from_canvas(filename)
        elif isinstance(event, PlotTypesChangedObservableEvent):
            self._create_subplots(event.list_of_plots)

    def _create_subplots(self, list_of_subplots):
        self.subplots = self.subplot_factory.create_subplots(list_of_subplots)
        self.panel.update_subplots(self.subplots)

    def _add_data_line_to_canvas(self, filename):
        self.dropbox_repository.add_file_to_compare_to_data(filename)
        self.panel.refresh_canvas()

    def _remove_line_from_canvas(self, filename):
        self.dropbox_repository.remove_file_to_compare_to_data(filename)
        self.panel.refresh_canvas()

