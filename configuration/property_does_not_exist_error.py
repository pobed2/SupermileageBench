#coding: utf-8

class PropertyDoesNotExistError(Exception):
    def __init__(self, value):
        self.value = value