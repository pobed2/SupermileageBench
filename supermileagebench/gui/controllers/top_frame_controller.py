class TopFrameController(object):
    def __init__(self, real_time_panel_controller, post_treatment_panel_controller):
        self.real_time_panel_controller = real_time_panel_controller
        self.post_treatment_panel_controller = post_treatment_panel_controller

    def set_frame(self, frame):
        self.frame = frame

    def on_start_button_click(self, event):
        self.real_time_panel_controller.start_plotting()

    def on_stop_and_save_button_click(self, event):
        self.real_time_panel_controller.stop_plotting(save=True)
        self.post_treatment_panel_controller.create_panel(self.frame)

    def on_stop_and_delete_button_click(self, event):
        self.real_time_panel_controller.stop_plotting(save=False)


