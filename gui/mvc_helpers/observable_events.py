class FileCheckedObservableEvent(object):
    def __init__(self, filename):
        self.filename = filename


class FileUncheckedObservableEvent(object):
    def __init__(self, filename):
        self.filename = filename