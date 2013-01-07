#coding: utf-8

import wx

class InjectionTableDialog(wx.Dialog):
    def __init__(self, controller, injection_table):
        super(InjectionTableDialog, self).__init__(parent=None, title="Table d'injection")
        self.injection_table = injection_table
        self._init_ui()
        self.SetSize((550, 250))
        self.Center()

    def _init_ui(self):
        dialog_sizer = wx.BoxSizer(wx.HORIZONTAL)

        grid_sizer = wx.GridSizer(7, 11, 10, 10)

        #line 1
        grid_sizer.Add(wx.StaticText(self, label=""))
        grid_sizer.Add(wx.StaticText(self, label="10%"))
        grid_sizer.Add(wx.StaticText(self, label="20%"))
        grid_sizer.Add(wx.StaticText(self, label="30%"))
        grid_sizer.Add(wx.StaticText(self, label="40%"))
        grid_sizer.Add(wx.StaticText(self, label="50%"))
        grid_sizer.Add(wx.StaticText(self, label="60%"))
        grid_sizer.Add(wx.StaticText(self, label="70%"))
        grid_sizer.Add(wx.StaticText(self, label="80%"))
        grid_sizer.Add(wx.StaticText(self, label="90%"))
        grid_sizer.Add(wx.StaticText(self, label="100%"))

        #line 2-7
        load = 50
        for load in range(50, 110, 10):
            load_str = str(load) + "%"
            grid_sizer.Add(wx.StaticText(self, label=load_str))
            for i in range(10, 110, 10):
                txt_ctrl = wx.TextCtrl(self, size=(40, 20))
                txt_ctrl.AppendText(self.injection_table.get_value(i, load))
                grid_sizer.Add(txt_ctrl)

        dialog_sizer.Add(grid_sizer, flag=wx.LEFT | wx.TOP | wx.GROW)

        self.SetSizer(dialog_sizer)
