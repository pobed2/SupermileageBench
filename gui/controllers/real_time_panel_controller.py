from configuration.app_properties import real_time_plots_property
from configuration.properties_parser import PropertiesParser
from gui.factories.subplots_factories import RealTimeSubplotFactory
from gui.mvc_helpers.observer import Observer
from gui.windows.real_time_panel import RealTimePanel
import wx

class RealTimePanelController(Observer):
    def __init__(self, real_time_subplots, app_controller):
        self.real_time_subplots = real_time_subplots
        self.app_controller = app_controller
        self.subplot_factory = RealTimeSubplotFactory()
        self.property_parser = PropertiesParser()

    def create_panel(self, panel_parent):
        self.panel = RealTimePanel(panel_parent, self.real_time_subplots,
            self.property_parser.get_property(real_time_plots_property))
        self._init_timer(panel_parent)
        self.panel.add_panel_observers(self)

    def update_subplots(self, list_of_subplots):
        self.real_time_subplots = self.subplot_factory.create_subplots(list_of_subplots)
        self.panel.update_subplots(self.real_time_subplots)

    def _init_timer(self, parent):
        self.redraw_period = 100
        self.redraw_timer = wx.Timer(parent)
        parent.Bind(wx.EVT_TIMER, self._on_redraw_timer, self.redraw_timer)

    def _on_redraw_timer(self, event):
        try:
            self.panel.refresh_canvas()
        except RuntimeError as e:
            print e

    def start_plotting(self):
        self._start_timer()
        self.app_controller.start_data_acquisition()

    def stop_plotting(self, save=True):
        self._stop_timer()
        self.panel.Hide()
        self.app_controller.stop_data_acquisition(save)

    def _start_timer(self):
        self.redraw_timer.Start(self.redraw_period)

    def _stop_timer(self):
        self.redraw_timer.Stop()






