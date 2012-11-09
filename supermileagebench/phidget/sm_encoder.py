
from Phidgets.PhidgetException import PhidgetErrorCodes, PhidgetException
from Phidgets.Devices.Encoder import *

class SMEncoder(object):

    def __init__(self):
        try:
            encoder = Encoder()
            encoder.setOnAttachHandler(self.encoderAttached)
            encoder.setOnDetachHandler(self.encoderDetached)
            encoder.setOnErrorhandler(self.encoderError)
            encoder.setOnPositionChangeHandler(self.encoderPositionChange)
            encoder.openPhidget()

            self.encoder = encoder

            self.attachDetachObservers = []
            self.changeObservers = []

        except PhidgetException as e:
            print("Phidget Error %i: %s" % (e.code, e.details))
            exit(1)
        except RuntimeError as e:
            print("Runtime Exception: %s" % e.details)
            print("Exiting....")
            exit(1)

    def encoderAttached(self, e):
        self._notifyAttachDetachObserversForAttach()
        attached = e.device
        print("Encoder %i Attached!" % (attached.getSerialNum()))

    def encoderDetached(self, e):
        self._notifyAttachDetachObserversForDetach()
        detached = e.device
        print("Encoder %i Detached!" % (detached.getSerialNum()))

    def encoderError(self, e):
        try:
            source = e.device
            print("Encoder %i: Phidget Error %i: %s" % (source.getSerialNum(), e.eCode, e.description))
        except PhidgetException as e:
            print("Phidget Exception %i: %s" % (e.code, e.details))

    def encoderPositionChange(self, e):
        self._notifyChangeObservers(self.encoder.getPosition(e.index),e.time)
        source = e.device
        print("Encoder %i: Encoder %i -- Change: %i -- Time: %i -- Position: %i" % (source.getSerialNum(), e.index, e.positionChange, e.time, self.encoder.getPosition(e.index)))

    def addAttachDetachObserver(self, observer):
        self.attachDetachObservers.append(observer)

    def addChangeObserver(self, observer):
        self.changeObservers.append(observer)

    def _notifyAttachDetachObserversForAttach(self):
        for observer in self.attachDetachObservers:
            observer.startTimer()

    def _notifyAttachDetachObserversForDetach(self):
        pass

    def _notifyChangeObservers(self, position, time):
        for observer in self.changeObservers:
            observer.updatePosition(position, time)