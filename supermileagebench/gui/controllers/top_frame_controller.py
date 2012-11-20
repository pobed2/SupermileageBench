
class TopFrameController(object):

    def __init__(self, plotting_controller):
        self.plotting_controller = plotting_controller

    def on_start_button_click(self, event):
        self.plotting_controller.start_plotting()

    def on_stop_and_save_button_click(self, event):
        self.plotting_controller.stop_plotting(save = True)

    def on_stop_and_delete_button_click(self, event):
        self.plotting_controller.stop_plotting(save = False)

