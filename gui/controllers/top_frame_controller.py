from configuration.properties_parser import PropertiesParser
from gui.controllers.post_processing_panel_controller import PostProcessingPanelController
from gui.controllers.real_time_panel_controller import RealTimePanelController
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

    def on_properties_click(self, event):
        properties_dialog = PropertiesDialog(self)
        properties_dialog.ShowModal()

    def save_properties(self, inertia, friction, real_time_plots, post_processing_plots):
        parser = PropertiesParser()
        parser.save_property("Inertia", inertia)
        parser.save_property("Friction", friction)
        parser.save_property("Real-Time Plots", real_time_plots)
        parser.save_property("Post-Processing Plots", post_processing_plots)

        parser.save_to_file()

    def create_post_processing_panel(self):
        self.post_processing_controller.create_panel(self.frame)
        self.frame.Layout()

    def on_start_button_click(self, event):
        self.real_time_panel_controller.start_plotting()

    def on_stop_and_save_button_click(self, event):
        self.real_time_panel_controller.stop_plotting(save=True)
        self.post_processing_controller.create_panel(self.frame)

    def on_stop_and_delete_button_click(self, event):
        self.real_time_panel_controller.stop_plotting(save=False)

    def close_frame(self):
        self.frame.Close()


