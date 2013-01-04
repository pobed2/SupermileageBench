from gui.factories.subplots_factory import SubplotFactory
from gui.mvc_helpers.observable_events import PlotTypesChangedObservableEvent
from gui.mvc_helpers.observer import Observer
from gui.windows.real_time_panel import RealTimePanel

class RealTimePanelController(Observer):
    def __init__(self, real_time_subplots, app_controller):
        self.real_time_subplots = real_time_subplots
        self.app_controller = app_controller
        self.subplot_factory = SubplotFactory()

    def create_panel(self, panel_parent):
        self.panel = RealTimePanel(panel_parent, self.real_time_subplots)
        self.panel.add_panel_observers(self)

    def start_plotting(self):
        self.panel.startTimer()
        self.app_controller.start_data_acquisition()

    def stop_plotting(self, save):
        self.panel.stop_timer()
        self.panel.Hide()
        self.app_controller.stop_data_acquisition(save)


    def update(self, event):
        if event == "start":
            self.start_plotting()
        elif event == "stop":
            self.stop_plotting(True)
        elif isinstance(event, PlotTypesChangedObservableEvent):
            self._create_subplots(event.list_of_plots)

    def _create_subplots(self, list_of_subplots):
        self.real_time_subplots = self.subplot_factory.create_subplots(list_of_subplots)
        self.panel.update_subplots(self.real_time_subplots)



