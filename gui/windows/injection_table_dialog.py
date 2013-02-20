#coding: utf-8
from __future__ import division
from math import floor
import wx

from app_settings import *

class InjectionTableDialog(wx.Dialog):
    def __init__(self, controller, injection_table):
        super(InjectionTableDialog, self).__init__(parent=None, title=u"Table d'injection")
        self.controller = controller
        self.injection_table = injection_table

        self.NUMBER_OF_ROWS = floor((INJ_TABLE_MAX_LOAD - INJ_TABLE_MIN_LOAD)/INJ_TABLE_LOAD_JUMP) + 1
        self.NUMBER_OF_COLUMNS = floor((INJ_TABLE_MAX_RPM - INJ_TABLE_MIN_RPM)/INJ_TABLE_RPM_JUMP) + 2 #+1 for extra data column and +1 for load titles on the left

        #Sizes of components in pixels
        self.TEXT_CTRL_WIDTH = 40
        self.TEXT_CTRL_WIDHT_PAD = 2
        self.TEXT_CTRL_HEIGHT = 20
        self.TEXT_CTRL_HEIGHT_PAD = 2
        self.BUTTONS_HEIGHT = 80

        self.TOTAL_WIDTH = self.NUMBER_OF_COLUMNS * (self.TEXT_CTRL_WIDTH + self.TEXT_CTRL_WIDHT_PAD)
        self.TOTAL_HEIGHT = self.NUMBER_OF_ROWS * (self.TEXT_CTRL_HEIGHT + self.TEXT_CTRL_HEIGHT_PAD) + self.BUTTONS_HEIGHT

        self._init_ui()
        self.SetSize((self.TOTAL_WIDTH, self.TOTAL_HEIGHT))
        self.Center()

    def _init_ui(self):
        dialog_sizer = wx.BoxSizer(wx.VERTICAL)
        grid_sizer = wx.GridSizer(self.NUMBER_OF_ROWS, self.NUMBER_OF_COLUMNS, self.TEXT_CTRL_HEIGHT_PAD, self.TEXT_CTRL_WIDHT_PAD)

        #First line
        self._add_rpm_titles(grid_sizer)

        #Rest of the lines
        self.text_ctrl_dict = self._create_injection_value_text_controls(grid_sizer)

        okButton = wx.Button(self, label='OK')
        okButton.Bind(wx.EVT_BUTTON, self.on_close)

        dialog_sizer.Add(grid_sizer, flag=wx.GROW)
        dialog_sizer.Add(okButton, flag=wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, border=10)

        self.SetSizer(dialog_sizer)

    def _add_rpm_titles(self, grid_sizer):
        grid_sizer.Add(wx.StaticText(self, label=u"")) #To make top left corner empty
        for rpm in range(INJ_TABLE_MIN_RPM, INJ_TABLE_MAX_RPM + 1, INJ_TABLE_RPM_JUMP):
            grid_sizer.Add(wx.StaticText(self, label=str(rpm)))

    def _create_injection_value_text_controls(self, grid_sizer):
        text_ctrl_dict = {}

        for load in range(INJ_TABLE_MIN_LOAD, INJ_TABLE_MAX_LOAD + 1, INJ_TABLE_LOAD_JUMP):
            load_str = str(load) + "%"
            grid_sizer.Add(wx.StaticText(self, label=load_str))

            text_ctrl_dict[load] = {}

            for rpm in range(INJ_TABLE_MIN_RPM, INJ_TABLE_MAX_RPM + 1, INJ_TABLE_RPM_JUMP):
                txt_ctrl = wx.TextCtrl(self, size=(self.TEXT_CTRL_WIDTH, self.TEXT_CTRL_HEIGHT))
                txt_ctrl.AppendText(self.injection_table.get_value(rpm, load))
                grid_sizer.Add(txt_ctrl)

                text_ctrl_dict[load][rpm] = txt_ctrl

        return text_ctrl_dict

    def get_injection_values(self):
        value_dict = {}
        for load in range(INJ_TABLE_MIN_LOAD, INJ_TABLE_MAX_LOAD + 1, INJ_TABLE_LOAD_JUMP):
            value_dict[load] = {}
            for rpm in range(INJ_TABLE_MIN_RPM, INJ_TABLE_MAX_RPM + 1, INJ_TABLE_RPM_JUMP):
                value_dict[load][rpm] = self.text_ctrl_dict[load][rpm].GetValue()

        return value_dict

    def on_close(self, event):
        value_dict = self.get_injection_values()
        self.controller.save_new_injection_table(value_dict)
        self.Destroy()

