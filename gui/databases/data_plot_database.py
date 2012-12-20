class DataPlotDatabase(object):
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state

    def get_shared_axis(self):
        pass

    def reset_shared_axis(self):
        pass