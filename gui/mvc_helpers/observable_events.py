class FileCheckedObservableEvent(object):
    def __init__(self, filename):
        self.filename = filename

    def execute_callback(self, observer):
        return observer.add_file_to_compare(self.filename)


class FileUncheckedObservableEvent(object):
    def __init__(self, filename):
        self.filename = filename

    def execute_callback(self, observer):
        return observer.remove_file_to_compare(self.filename)


class ResetAppClickedObservableEvent(object):
    def execute_callback(self, observer):
        return observer.reset_app()


class PlotTypesChangedObservableEvent(object):
    def __init__(self, list_of_plots):
        self.list_of_plots = list_of_plots

    def execute_callback(self, observer):
        return observer.create_subplots(self.list_of_plots)


class StartButtonClickedObservableEvent(object):
    def execute_callback(self, observer):
        return observer.start_plotting()


class StopButtonClickedObservableEvent(object):
    def execute_callback(self, observer):
        return observer.stop_plotting()