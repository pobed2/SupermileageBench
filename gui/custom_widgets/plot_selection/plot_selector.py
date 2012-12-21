import wx
from wx.combo import ComboCtrl
from gui.custom_widgets.plot_selection.checklist_combo_popup import CheckListComboPopup
from gui.mvc_helpers.observable import Observable

class PlotSelector(wx.Panel, Observable):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, 0, style=wx.SIMPLE_BORDER)
        Observable.__init__(self)

        cc = wx.combo.ComboCtrl(self)
        tcp = CheckListComboPopup(["Position", "Vitesse", "Acceleration", "Torque"])
        cc.SetPopupControl(tcp)

        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(cc, 1, flag=wx.CENTER)

        self.SetSizer(self.sizer)
