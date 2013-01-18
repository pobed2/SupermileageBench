#coding: utf-8

class CantHandleEventError(Exception):
    def __init__(self, value):
        self.value = value