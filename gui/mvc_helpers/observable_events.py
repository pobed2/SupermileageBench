class FileCheckedObservableEvent(object):
    def __init__(self, filename):
        self.filename = filename


class FileUncheckedObservableEvent(object):
    def __init__(self, filename):
        self.filename = filename


class PlotTypesChangedObservableEvent(object):
    def __init__(self, list_of_plots):
        self.list_of_plots = list_of_plots