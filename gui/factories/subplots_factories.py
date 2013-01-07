#coding: utf-8

from configuration.app_settings import real_time_plots_class_dict, post_processing_plots_class_dict

class SubplotFactory(object):
    '''
    Base class for subplot factories
    '''

    def create_subplots(self, list_of_names):
        subplots = []
        number_of_plots = len(list_of_names)
        for order, name in enumerate(list_of_names):
            plot = self.create_subplot(name, order, number_of_plots)
            subplots.append(plot)
        return subplots


class RealTimeSubplotFactory(SubplotFactory):
    def create_subplot(self, name, order, number_of_plots):
        return real_time_plots_class_dict[name](order, number_of_plots)


class PostProcessingSubplotFactory(SubplotFactory):
    def create_subplot(self, name, order, number_of_plots):
        return post_processing_plots_class_dict[name](order, number_of_plots)