import wx

class CustomCheckListBox(wx.Panel):
    def __init__(self, parent=None, choices=[], checked=[]):
        super(CustomCheckListBox, self).__init__(parent=parent, id=-1)

        self.checkboxes = self._init_checkboxes(choices, checked)
        self.sizer = self._init_checkbox_placement(self.checkboxes)

        self.SetSizer(self.sizer)

    def _init_checkboxes(self, choices, checked):
        checkboxes = []
        for choice in choices:
            checkbox = wx.CheckBox(self, label=choice)
            checkbox.SetValue(choice in checked)
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
