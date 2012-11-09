
class EncoderController(object):

    def __init(self, database):
        self.database = database

    def updatePosition(self, position, time):
        self.database.addPoint(position, time)