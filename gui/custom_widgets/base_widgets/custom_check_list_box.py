import wx
from gui.mvc_helpers.observable import Observable
from gui.mvc_helpers.observable_events import CheckboxChangedStateObservableEvent
from gui.mvc_helpers.observer import Observer

class CustomCheckListBox(wx.Panel, Observable, Observer):
    def __init__(self, parent=None, choices=[], checked=[], observer=None):
        super(CustomCheckListBox, self).__init__(parent=parent, id=-1)
        Observable.__init__(self)

        self.checkboxes = self._init_checkboxes(choices, checked)
        self.sizer = self._init_checkbox_placement(self.checkboxes)
        self.observer = observer

        self.SetSizer(self.sizer)

    def _init_checkboxes(self, choices, checked):
        checkboxes = []
        for choice in choices:
            checkbox = wx.CheckBox(self, label=choice)
            checkbox.SetValue(choice in checked)
            checkbox.Bind(wx.EVT_CHECKBOX, self._checkbox_checked)
            checkboxes.append(checkbox)
        return checkboxes

    def _init_checkbox_placement(self, checkboxes):
        sizer = wx.BoxSizer(wx.VERTICAL)
        for checkbox in checkboxes:
            sizer.Add(checkbox)
        return sizer

    def get_checked(self):
        checked = []
        for checkbox in self.checkboxes:
            if checkbox.IsChecked():
                checked.append(checkbox.GetLabel())

        return checked

    def _checkbox_checked(self, event):
        self.notify_observers(CheckboxChangedStateObservableEvent())