#coding: utf-8

import wx

class InjectionTableDialog(wx.Dialog):
    def __init__(self, controller, injection_table):
        super(InjectionTableDialog, self).__init__(parent=None, title="Table d'injection")
        self.controller = controller
        self.injection_table = injection_table
        self._init_ui()
        self.SetSize((800, 250))
        self.Center()

    def _init_ui(self):
        dialog_sizer = wx.BoxSizer(wx.VERTICAL)

        grid_sizer = wx.GridSizer(7, 11, 10, 10)

        #line 1
        grid_sizer.Add(wx.StaticText(self, label="Load/RPM"))
        grid_sizer.Add(wx.StaticText(self, label="1000"))
        grid_sizer.Add(wx.StaticText(self, label="1500"))
        grid_sizer.Add(wx.StaticText(self, label="2000"))
        grid_sizer.Add(wx.StaticText(self, label="2500"))
        grid_sizer.Add(wx.StaticText(self, label="3000"))
        grid_sizer.Add(wx.StaticText(self, label="3500"))
        grid_sizer.Add(wx.StaticText(self, label="4000"))
        grid_sizer.Add(wx.StaticText(self, label="4500"))
        grid_sizer.Add(wx.StaticText(self, label="5000"))
        grid_sizer.Add(wx.StaticText(self, label="5500"))

        #line 2-7
        self.txt_ctrl_dict = {}
        for load in range(50, 110, 10):
            load_str = str(load) + "%"
            grid_sizer.Add(wx.StaticText(self, label=load_str))

            self.txt_ctrl_dict[load] = {}
            for rpm in range(1000, 6000, 500):
                txt_ctrl = wx.TextCtrl(self, size=(40, 20))
                txt_ctrl.AppendText(self.injection_table.get_value(rpm, load))
                grid_sizer.Add(txt_ctrl)

                self.txt_ctrl_dict[load][rpm] = txt_ctrl

        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        okButton = wx.Button(self, label='OK')
        okButton.Bind(wx.EVT_BUTTON, self.on_close)
        button_sizer.Add(okButton)
        print grid_sizer.Rows

        dialog_sizer.Add(grid_sizer, flag=wx.LEFT | wx.TOP | wx.GROW)
        dialog_sizer.Add(button_sizer, flag=wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, border=10)

        self.SetSizer(dialog_sizer)

    def create_value_dict(self):
        value_dict = {}
        for load in range(50, 110, 10):
            value_dict[load] = {}
            for rpm in range(1000, 6000, 500):
                value_dict[load][rpm] = self.txt_ctrl_dict[load][rpm].GetValue()

        return value_dict

    def on_close(self, event):
        value_dict = self.create_value_dict()
        self.controller.save_new_injection_table(value_dict)
        self.Destroy()

