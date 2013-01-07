#coding: utf-8
import pickle

class InjectionTable(object):
    def __init__(self):
        self.FILENAME = "inj_table.pkl"
        self.injection_table = self._read_pickled_table()

    def _read_pickled_table(self):
        try:
            with open(self.FILENAME) as table:
                return pickle.loads(table.read())
        except IOError:
            return {}

    def set_value(self, percent, load, value):
        self.injection_table[load][percent] = value

    def get_value(self, percent, load):
        try:
            return self.injection_table[load][percent]
        except KeyError:
            return '10.0'

    def init_from_csv(self):
        pass

    def write_as_csv_string(self):
        pass
