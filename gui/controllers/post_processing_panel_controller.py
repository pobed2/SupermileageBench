from configuration.app_settings import post_processing_plots_property
from configuration.properties_parser import PropertiesParser
from data_access.dropbox_repositories import DropboxRepository
from gui.factories.subplots_factories import PostProcessingSubplotFactory
from gui.mvc_helpers.observer import Observer
from gui.windows.post_processing_panel import PostProcessingPanel

class PostProcessingPanelController(Observer):
    def __init__(self, subplots, app_controller):
        self.subplots = subplots
        self.dropbox_repository = DropboxRepository()
        self.app_controller = app_controller
        self.subplot_factory = PostProcessingSubplotFactory()
        self.property_parser = PropertiesParser()

    def create_panel(self, frame):
        names_of_comparable_files = self.dropbox_repository.fetch_names_of_comparable_files()

        self.panel = PostProcessingPanel(frame, self.subplots, names_of_comparable_files,
            self.property_parser.get_property(post_processing_plots_property))
        self.panel.add_panel_observers(self)
        self.panel.draw_plot_canvas()

    def reset_app(self):
        self.app_controller.reset_app()

    def add_file_to_compare(self, filename):
        self._add_data_line_to_canvas(filename)

    def _add_data_line_to_canvas(self, filename):
        self.dropbox_repository.add_file_to_compare_to_data(filename)
        self.panel.refresh_canvas()

    def remove_file_to_compare(self, filename):
        self._remove_line_from_canvas(filename)

    def _remove_line_from_canvas(self, filename):
        self.dropbox_repository.remove_file_to_compare_to_data(filename)
        self.panel.refresh_canvas()

    def create_subplots(self, list_of_subplots):
        self.subplots = self.subplot_factory.create_subplots(list_of_subplots)
        self.panel.update_subplots(self.subplots)




