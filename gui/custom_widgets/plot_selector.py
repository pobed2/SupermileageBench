import wx
from wx.combo import ComboCtrl
from gui.custom_widgets.base_widgets.checklist_combo_popup import CheckListComboPopup
from gui.mvc_helpers.observable import Observable
from gui.mvc_helpers.observer import Observer

class PlotSelector(wx.Panel, Observable, Observer):
    def __init__(self, parent, available_choices, chosen_plots):
        wx.Panel.__init__(self, parent, 0, style=wx.SIMPLE_BORDER)
        Observable.__init__(self)

        cc = wx.combo.ComboCtrl(self, -1)
        tcp = CheckListComboPopup(available_choices, chosen_plots)
        tcp.add_observer(self)

        cc.SetPopupControl(tcp)

        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(cc, 1, flag=wx.CENTER)

        self.SetSizer(self.sizer)
8