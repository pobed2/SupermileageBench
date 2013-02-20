import pickle
from configuration.app_properties import default_properties
from configuration.property_does_not_exist_error import PropertyDoesNotExistError

class PropertiesParser(object):
    def __init__(self):
        self.FILENAME = "properties.cfg"
        self.properties = self._read_properties_file()

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
            return self._get_default_property(name)

    def _get_default_property(self, name):
        try:
            return default_properties[name]
        except KeyError:
            raise PropertyDoesNotExistError(name)
