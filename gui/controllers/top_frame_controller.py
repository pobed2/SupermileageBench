from configuration.app_settings import inertia_property, friction_property, real_time_plots_property, post_processing_plots_property
from configuration.properties_parser import PropertiesParser
from databases.injection_table import InjectionTable
from gui.controllers.post_processing_panel_controller import PostProcessingPanelController
from gui.controllers.real_time_panel_controller import RealTimePanelController
from gui.windows.injection_table_dialog import InjectionTableDialog
from gui.windows.properties_dialog import PropertiesDialog
from gui.windows.top_frame import TopFrame

class TopFrameController(object):
    def __init__(self, real_time_subplots, post_processing_subplots, app_controller):
        self.frame = TopFrame(self)

        self.real_time_controller = RealTimePanelController(real_time_subplots, app_controller)
        self.post_processing_controller = PostProcessingPanelController(post_processing_subplots, app_controller)

        self.real_time_controller.create_panel(self.frame)

        self.frame.Show(True)
        self.frame.Centre()

    def close_frame(self):
        self.frame.Close()

    def create_post_processing_panel(self):
        self.post_processing_controller.create_panel(self.frame)
        self.frame.Layout()

    #Handlers for PropertiesDialog
    def on_properties_click(self, event):
        properties_dialog = PropertiesDialog(self)
        properties_dialog.ShowModal()

    def save_properties(self, inertia, friction, real_time_plots, post_processing_plots):
        parser = PropertiesParser()
        parser.save_property(inertia_property, inertia)
        parser.save_property(friction_property, friction)
        parser.save_property(real_time_plots_property, real_time_plots)
        parser.save_property(post_processing_plots_property, post_processing_plots)

        parser.save_to_file()

    #Handlers for InjectionTable
    def on_injection_table_menu_click(self, event):
        injection_table_dialog = InjectionTableDialog(self, InjectionTable())
        injection_table_dialog.ShowModal()

    def save_new_injection_table(self, dict):
        injection_table = InjectionTable(dict)
        injection_table.save_as_current()


