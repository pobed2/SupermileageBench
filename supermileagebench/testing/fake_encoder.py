class FakeEncoder(object):
    def __init__(self):
        self.attachDetachObservers = []
        self.changeObservers = []

    def encoderAttached(self):
        self._notifyAttachDetachObserversForAttach()
        print("Encoder %i Attached!")

    def encoderDetached(self):
        self._notifyAttachDetachObserversForDetach()
        print("Encoder %i Detached!")

    def encoderError(self, e):
        pass

    def encoderPositionChange(self, position, time):
        self._notifyChangeObservers(position, time)

    def addAttachDetachObserver(self, observer):
        self.attachDetachObservers.append(observer)

    def addChangeObserver(self, observer):
        self.changeObservers.append(observer)

    def _notifyAttachDetachObserversForAttach(self):
        for observer in self.attachDetachObservers:
            observer.encoder_is_attached()

    def _notifyAttachDetachObserversForDetach(self):
        pass

    def _notifyChangeObservers(self, position, time):
        for observer in self.changeObservers:
            observer.updatePosition(position, time)