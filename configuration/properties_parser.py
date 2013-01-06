import pickle

class PropertiesParser(object):
    def __init__(self):
        self.FILENAME = "properties.cfg"
        self.properties = self._read_properties_file()
        print self.properties

    def _read_properties_file(self):
        try:
            with open(self.FILENAME) as properties:
                return pickle.loads(properties.read())
        except IOError:
            return {}

    def save_property(self, name, value):
        self.properties[name] = value

    def save_to_file(self):
        with open(self.FILENAME, 'wb') as handle:
            pickle.dump(self.properties, handle)

    def get_property(self, name):
        try:
            return self.properties[name]
        except KeyError:
            return ""
