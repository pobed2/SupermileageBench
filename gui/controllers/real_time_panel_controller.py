from configuration.app_settings import real_time_plots_property
from configuration.properties_parser import PropertiesParser
from gui.factories.subplots_factories import RealTimeSubplotFactory
from gui.mvc_helpers.cant_handle_event_error import CantHandleEventError
from gui.windows.real_time_panel import RealTimePanel

class RealTimePanelController(object):
    def __init__(self, real_time_subplots, app_controller):
        self.real_time_subplots = real_time_subplots
        self.app_controller = app_controller
        self.subplot_factory = RealTimeSubplotFactory()
        self.property_parser = PropertiesParser()

    def create_panel(self, panel_parent):
        self.panel = RealTimePanel(panel_parent, self.real_time_subplots,
            self.property_parser.get_property(real_time_plots_property))
        self.panel.add_panel_observers(self)

    def start_plotting(self):
        self.panel.startTimer()
        self.app_controller.start_data_acquisition()

    def stop_plotting(self, save=True):
        self.panel.stop_timer()
        self.panel.Hide()
        self.app_controller.stop_data_acquisition(save)

    def create_subplots(self, list_of_subplots):
        self.real_time_subplots = self.subplot_factory.create_subplots(list_of_subplots)
        self.panel.update_subplots(self.real_time_subplots)

    #Observer pattern
    def update(self, event):
        try:
            event.execute_callback(self)
        except AttributeError as e:
            raise CantHandleEventError(e)





