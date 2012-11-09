
class EncoderController(object):

    def __init__(self, database):
        self.database = database
        self.started = False

    def start_data_acquisition(self):
        self.started = True

    def stop_data_acquisition(self):
        self.started = False

    def updatePosition(self, position, time):
        if self.started:
            self.database.addPoint(position, time)