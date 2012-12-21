import wx
from wx.combo import ComboPopup

class CheckListComboPopup(ComboPopup):
    def __init__(self, list_of_items):
        super(CheckListComboPopup, self).__init__()
        self.list_of_items = list_of_items

    def Create(self, parent):
        self.checklistbox = wx.CheckListBox(parent, -1, choices=self.list_of_items)

    def GetControl(self):
        return self.checklistbox

    def OnPopup(self):
        pass