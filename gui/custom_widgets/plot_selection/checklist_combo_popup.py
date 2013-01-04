import wx
from wx.combo import ComboPopup
from gui.mvc_helpers.observable import Observable
from gui.mvc_helpers.observable_events import   PlotTypesChangedObservableEvent

class CheckListComboPopup(ComboPopup, Observable):
    def __init__(self, list_of_items):
        super(CheckListComboPopup, self).__init__()
        Observable.__init__(self)
        self.list_of_items = list_of_items

    def Create(self, parent):
        self.checklistbox = wx.CheckListBox(parent, -1, choices=self.list_of_items)
        self.checklistbox.Bind(wx.EVT_CHECKLISTBOX, self.on_check_or_uncheck)

    def GetControl(self):
        return self.checklistbox

    def OnPopup(self):
        pass

    def on_check_or_uncheck(self, event):
        list_of_plots = [self.list_of_items[i] for i in self.checklistbox.GetChecked()]
        self.notify_observers(PlotTypesChangedObservableEvent(list_of_plots))