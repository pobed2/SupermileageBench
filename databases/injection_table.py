#coding: utf-8
import cPickle as pickle

class InjectionTable(object):
    def __init__(self, dict=None):
        self.FILENAME = "inj_table.pkl"
        self.injection_table = self.load_table(dict)

    def load_table(self, dict):
        if dict == None:
            return self._read_pickled_table()
        else:
            return dict #Todo No verification is made here

    def _read_pickled_table(self):
        try:
            with open(self.FILENAME) as table:
                return pickle.loads(table.read())
        except IOError:
            return {}

    def set_value(self, rpm, load, value):
        self.injection_table[load][rpm] = value

    def get_value(self, rpm, load):
        try:
            return self.injection_table[load][rpm]
        except KeyError:
            return '0.0'

    def save_as_current(self):
        with open(self.FILENAME, "wb") as file:
            pickle.dump(self.injection_table, file)

    #FIXME Ugly...
    def serialize_data_as_csv(self):
        data_string = ""
        loads = self._get_loads()
        rpms = self._get_rpms()

        #Writing the top rpms
        data_string += "0,"
        for i, load in enumerate(rpms):
            data_string += str(load)
            if i != len(rpms) - 1:
                data_string += ","

        data_string += "\n"

        #Writing the values for every loads/rpms
        for load in loads:
            rpms = self.injection_table[load]
            list_of_rpms = []
            list_of_rpms.append(str(load))
            for rpm, value in sorted(rpms.iteritems()):
                list_of_rpms.append(str(value))

            data_string += ",".join(list_of_rpms)
            data_string += "\n"

        return data_string

    def _get_loads(self):
        return sorted(self.injection_table)

    def _get_rpms(self):
        return sorted(self.injection_table[self.injection_table.keys()[0]])

