from gui.mvc_helpers.cant_handle_event_error import CantHandleEventError

class Observer(object):
    #Observer pattern
    def update(self, event):
        try:
            event.execute_callback(self)
        except AttributeError as e:
            raise CantHandleEventError(e)
