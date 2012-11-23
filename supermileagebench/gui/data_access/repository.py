class Repository(object):
    '''
    Base class for repositories. They are used to access data form the different databases
    Not for use on its own : use one of its child class
    '''

    def get_x_data(self):
        return self.x_data_getter()

    def get_y_data(self):
        return self.y_data_getter()

    def get_max_x_data(self):
        return self.x_data_getter()[-1]

    def get_min_y_data(self):
        return min(self.y_data_getter())

    def get_max_y_data(self):
        return max(self.y_data_getter())