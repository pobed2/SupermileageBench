#coding: utf-8

import wx

class InjectionTableDialog(wx.Dialog):
    def __init__(self, controller):
        super(InjectionTableDialog, self).__init__(parent=None, title="Table d'injection")
        self._init_ui()
        self.Center()

    def _init_ui(self):
        grid_sizer = wx.GridSizer(7, 11, 5, 5)

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

        #line 2
        grid_sizer.Add(wx.StaticText(self, label="50%"))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))

        #line 3
        grid_sizer.Add(wx.StaticText(self, label="60%"))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))


        #line 4
        grid_sizer.Add(wx.StaticText(self, label="70%"))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))

        #line 5
        grid_sizer.Add(wx.StaticText(self, label="80%"))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))

        #line 6
        grid_sizer.Add(wx.StaticText(self, label="90%"))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))

        #line 7
        grid_sizer.Add(wx.StaticText(self, label="100%"))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))
        grid_sizer.Add(wx.TextCtrl(self, size=(30, 20)))

        self.SetSizer(grid_sizer)
